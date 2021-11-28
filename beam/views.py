from sys import prefix
from django.db.models import query
from django.shortcuts import render
from django.http import HttpResponse
from django.forms import modelformset_factory

from indeterminatebeam import (
    Beam,
    Support,
    PointLoad,
    PointTorque,
    TrapezoidalLoadV,
    )

from numpy import empty

from .models import (
    BeamModel,
    SupportModel,
    PointLoadModel,
    PointTorqueModel,
    DistributedLoadModel,
    QueryModel,
    UnitOptionsModel,
)

from .forms import (
    BeamForm,
    SupportForm,
    PointLoadForm,
    PointTorqueForm,
    DistributedLoadForm,
    QueryForm,
    UnitOptionsForm,
)

# Create your views here.

def index(request):
    SupportFormSet = modelformset_factory(SupportModel, form=SupportForm, extra=1) 
    PointLoadFormSet = modelformset_factory(PointLoadModel, form = PointLoadForm, extra = 1)
    PointTorqueFormSet = modelformset_factory(PointTorqueModel, form = PointTorqueForm, extra = 1)
    DistributedLoadFormSet = modelformset_factory(DistributedLoadModel, form = DistributedLoadForm, extra = 1)
    QueryFormSet = modelformset_factory(QueryModel, form = QueryForm, extra = 1)


    if request.method == 'GET':
        beam_form = BeamForm(prefix='beam')
        
        support_formset = SupportFormSet(queryset=SupportModel.objects.none(), prefix='support')
        pointload_formset = PointLoadFormSet(queryset=PointLoadModel.objects.none(), prefix = 'point_load')
        pointtorque_formset = PointTorqueFormSet(queryset= PointTorqueModel.objects.none(), prefix = 'point_torque')
        distributedload_formset = DistributedLoadFormSet(queryset = DistributedLoadModel.objects.none(), prefix='distributed_load')
        query_formset = QueryFormSet(queryset = QueryModel.objects.none(), prefix='query')

        unitoptions_form = UnitOptionsForm(prefix = 'units')


        # TO DO -- properly implement the beam creation (more for post request i guess, but get may be important for when there is already data present)
        beam = Beam()
        beam.add_supports(Support(0,(1,1,1)))
        beam.analyse()

        plot_int = beam.plot_beam_internal().update_layout(width=900).to_html()
        plot_ext = beam.plot_beam_external().update_layout(width=900).to_html()

        
        return render(request, 'beam/index.html', {
            'beam_form' : beam_form,            
            'support_formset' : support_formset,
            'pointload_formset' : pointload_formset,
            'pointtorque_formset' : pointtorque_formset,
            'distributedload_formset' : distributedload_formset,
            'query_formset' : query_formset,
            'unitoptions_form' : unitoptions_form,
            'beam': beam,
            'plot_int': plot_int,
            'plot_ext': plot_ext,
            'forms': [
                ('Beam', beam_form, 'form'),
                ('Supports', support_formset, 'formset'),
                ('Point-Loads', pointload_formset, 'formset'),
                ('Point-Torques', pointtorque_formset, 'formset'),
                ('Distributed-Loads', distributedload_formset, 'formset'),
                ('Query', query_formset, 'formset'),
                ('Units', unitoptions_form, 'form'),
            ]
        })

    elif request.method == 'POST':
        beam_form = BeamForm(request.POST, prefix='beam')
        
        support_formset = SupportFormSet(request.POST, prefix='support')
        pointload_formset = PointLoadFormSet(request.POST, prefix='point_load')
        pointtorque_formset = PointTorqueFormSet(request.POST, prefix='point_torque')
        distributedload_formset = DistributedLoadFormSet(request.POST, prefix='distributed_load')
        query_formset = QueryFormSet(request.POST,prefix = 'query')

        unitoptions_form = UnitOptionsForm(request.POST, prefix='units')

        # check is valid
        valid = True
        for a in [
            beam_form,
            support_formset,
            pointload_formset,
            pointtorque_formset,
            distributedload_formset,
            query_formset,
            unitoptions_form,
            ]:
            valid *= a.is_valid()
        
        if valid:
            beam = Beam(
                span= beam_form.cleaned_data['length'],
                E =  beam_form.cleaned_data['E'],
                I =  beam_form.cleaned_data['I'],
                A =  beam_form.cleaned_data['A'],
            )

            beam.update_units('length', unitoptions_form.cleaned_data['length'])
            beam.update_units('force', unitoptions_form.cleaned_data['force'])
            beam.update_units('moment', unitoptions_form.cleaned_data['moment'])
            beam.update_units('distributed', unitoptions_form.cleaned_data['distributed'])
            beam.update_units('stiffness', unitoptions_form.cleaned_data['stiffness'])
            beam.update_units('A', unitoptions_form.cleaned_data['A'])
            beam.update_units('E', unitoptions_form.cleaned_data['E'])
            beam.update_units('I', unitoptions_form.cleaned_data['I'])
            beam.update_units('deflection', unitoptions_form.cleaned_data['deflection'])

            for support_form in support_formset.cleaned_data:
                support_dict = {
                    'Fixed':(1,1,1),
                    'Roller':(0,1,0),
                    'Pinned':(1,1,0),
                }
                if support_form:
                    beam.add_supports(Support(support_form['coordinate'], support_dict[support_form['support']]))
                else:
                    beam.add_supports(Support(0,(1,1,1)))

            for pointload_form in pointload_formset.cleaned_data:
                if pointload_form:
                    beam.add_loads(
                        PointLoad(
                            force = pointload_form['force'],
                            coord = pointload_form['coordinate'],
                            angle = pointload_form['angle'],
                        )
                    )
            
            for pointtorque_form in pointtorque_formset.cleaned_data:
                if pointtorque_form:
                    beam.add_loads(
                        PointTorque(
                            force = pointtorque_form['torque'],
                            coord = pointtorque_form['coordinate'],
                        )
                    )

            for distributedload_form in distributedload_formset.cleaned_data:
                if distributedload_form:
                    beam.add_loads(
                        TrapezoidalLoadV(
                            force = (distributedload_form['start_load'],distributedload_form['end_load']),
                            span = (distributedload_form['start_coordinate'],distributedload_form['end_coordinate'])
                        )
                    )
            
            for query_form in query_formset.cleaned_data:
                if query_form:
                    beam.add_query_points(query_form['query'])

            beam.analyse()

            plot_int = beam.plot_beam_internal().update_layout(width=900).to_html()
            plot_ext = beam.plot_beam_external().update_layout(width=900).to_html()

            return render(request, 'beam/index.html', {
                'beam_form' : beam_form,            
                'support_formset' : support_formset,
                'pointload_formset' : pointload_formset,
                'pointtorque_formset' : pointtorque_formset,
                'distributedload_formset' : distributedload_formset,
                'query_formset' : query_formset,
                'unitoptions_form' : unitoptions_form,
                'beam': beam,
                'plot_int': plot_int,
                'plot_ext': plot_ext,
                'forms': [
                    ('Beam', beam_form, 'form'),
                    ('Supports', support_formset, 'formset'),
                    ('Point-Loads', pointload_formset, 'formset'),
                    ('Point-Torques', pointtorque_formset, 'formset'),
                    ('Distributed-Loads', distributedload_formset, 'formset'),
                    ('Query', query_formset, 'formset'),
                    ('Units', unitoptions_form, 'form'),
                ]
            })

    # elif request.method == 'POST':
    #     pet_form = PetForm(request.POST)
    #     formset = ImageFormSet(request.POST, request.FILES)

    #     if pet_form.is_valid and formset.is_valid():
    #         pet_obj = pet_form.save()

    #         for form in formset.cleaned_data:
    #             if form:
    #                 image = form['image']
    #                 Image.objects.create(image=image, pet=pet_obj)
    #         return HttpResponseRedirect('/')
    #     else:
    #         print(pet_form.errors, formset.errors)




    return render(request, 'beam/hello.html')
