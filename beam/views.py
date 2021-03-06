from django.http.response import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import modelformset_factory

import base64
from plotly.io import to_json, from_json

from .utils import render_to_pdf

from indeterminatebeam import (
    Beam,
    Support,
    PointLoad,
    PointTorque,
    TrapezoidalLoadV,
    )

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
def report(request):
    # if session
    if request.session.get('plot_int_json') and request.session.get('plot_ext_json'):
            
            plot_ext = from_json(request.session.get('plot_ext_json'))
            plot_ext_image = plot_ext.to_image(format='png')

            plot_int = from_json(request.session.get('plot_int_json'))
            plot_int_image = plot_int.to_image(format='png')

            pdf = render_to_pdf('beam/report.html', context_dict={
                'plot_ext': str(base64.b64encode(plot_ext_image)),
                'plot_int': str(base64.b64encode(plot_int_image)),
            })

            response = HttpResponse(pdf, content_type='application/pdf')

            if request.GET.get('download') == 'pdf':

                filename = 'beam_report.pdf'
                content = f"attachment; filename={filename}"
                response['Content-Disposition'] = content

            elif request.GET.get('download') == 'html':
                filename = 'beam_report.html'

                html = render(request, 'beam/report_html.html', {
                    'plot_ext': plot_ext.to_html(),
                    'plot_int': plot_int.to_html(),
                })

                response = HttpResponse(html, content_type='text/html')
                content = f"attachment; filename={filename}"
                response['Content-Disposition'] = content

            return response

    else:
        return Http404('Could not generate a report')


def index(request):
    # create formset
    SupportFormSet = modelformset_factory(SupportModel, form=SupportForm, extra=1) 
    PointLoadFormSet = modelformset_factory(PointLoadModel, form = PointLoadForm, extra = 1)
    PointTorqueFormSet = modelformset_factory(PointTorqueModel, form = PointTorqueForm, extra = 1)
    DistributedLoadFormSet = modelformset_factory(DistributedLoadModel, form = DistributedLoadForm, extra = 1)
    QueryFormSet = modelformset_factory(QueryModel, form = QueryForm, extra = 1)


    if request.method == 'GET':
        # if forms have been saved initialise with previous data, otherwise reset.
        # if clear form button has been called then also dont use previous and use default.
        if request.session.get('forms'):

            previous_forms = request.session.get('forms')
            # try load up the previous form information
            # if there is an error it is probably due to a version change.
            # clearing the beam will help rectify the issue.
            try:
                beam_form = BeamForm(previous_forms, prefix='beam', label_suffix=' ()')
                support_formset = SupportFormSet(previous_forms, prefix='support')
                pointload_formset = PointLoadFormSet(previous_forms, prefix='point_load')
                pointtorque_formset = PointTorqueFormSet(previous_forms, prefix='point_torque')
                distributedload_formset = DistributedLoadFormSet(previous_forms, prefix='distributed_load')
                query_formset = QueryFormSet(previous_forms,prefix = 'query')
                unitoptions_form = UnitOptionsForm(previous_forms, prefix='units')
            except:
                return redirect('reset')

        else:
            beam_form = BeamForm(prefix='beam', label_suffix=' ()')
        
            support_formset = SupportFormSet(queryset=SupportModel.objects.none(), prefix='support')
            pointload_formset = PointLoadFormSet(queryset=PointLoadModel.objects.none(), prefix = 'point_load')
            pointtorque_formset = PointTorqueFormSet(queryset= PointTorqueModel.objects.none(), prefix = 'point_torque')
            distributedload_formset = DistributedLoadFormSet(queryset = DistributedLoadModel.objects.none(), prefix='distributed_load')
            query_formset = QueryFormSet(queryset = QueryModel.objects.none(), prefix='query')

            unitoptions_form = UnitOptionsForm(prefix = 'units')

        beam = Beam()
        beam.add_supports(Support(0,(1,1,1)))
        beam.analyse()

        # restore graphs from previous session if available otherwise generate new graph
        if request.session.get('plot_int') and request.session.get('plot_ext'):
            plot_int = request.session.get('plot_int')
            plot_ext = request.session.get('plot_ext')
        else:
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
            ],
        })

    elif request.method == 'POST':
        # initialize form objects with POST information

        beam_form = BeamForm(request.POST, prefix='beam', label_suffix=' ()')
        
        support_formset = SupportFormSet(request.POST, prefix='support')
        pointload_formset = PointLoadFormSet(request.POST, prefix='point_load')
        pointtorque_formset = PointTorqueFormSet(request.POST, prefix='point_torque')
        distributedload_formset = DistributedLoadFormSet(request.POST, prefix='distributed_load')
        query_formset = QueryFormSet(request.POST,prefix = 'query')

        unitoptions_form = UnitOptionsForm(request.POST, prefix='units')

        form_list = [
            beam_form,
            support_formset,
            pointload_formset,
            pointtorque_formset,
            distributedload_formset,
            query_formset,
            unitoptions_form,
        ]

        # check is valid
        valid = True
        for a in form_list:
            valid *= a.is_valid()
        
        # if form is valid
        if valid:
            # save session client side
            request.session['forms']=request.POST

            beam = create_beam(*form_list)

            plot_int = beam.plot_beam_internal().update_layout(width=900).to_html()
            plot_ext = beam.plot_beam_external().update_layout(width=900).to_html()

            request.session['plot_int'] = plot_int
            request.session['plot_ext'] = plot_ext

            request.session['plot_int_json'] = beam.plot_beam_internal().update_layout(width=900).to_json()
            request.session['plot_ext_json'] = beam.plot_beam_external().update_layout(width=900).to_json()

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
                ],
            })
        # should really through up an error message to let the user know something is wrong without deleting
        else:
            return HttpResponse('Error with information')

def reset(request):
    # remove all saved information to allow the form to reset to default parameters
    request.session['forms']=[]
    request.session['plot_int']=[]
    request.session['plot_ext']=[]
    request.session['plot_ext_json']=[]
    request.session['plot_int_json']=[]
    # get request the main page, however now session information is set to none meaning
    # that the default values are returned to the user.
    return redirect('index')

def create_beam(
    beam_form,
    support_formset,
    pointload_formset,
    pointtorque_formset,
    distributedload_formset,
    query_formset,
    unitoptions_form
    ):

    # create beam object
    beam = Beam(
        span= beam_form.cleaned_data['length'],
        E =  beam_form.cleaned_data['E'],
        I =  beam_form.cleaned_data['I'],
        A =  beam_form.cleaned_data['A'],
    )

    # get imperial or metric based on first part of form
    if unitoptions_form.cleaned_data['units'] == 'metric':
        suffix = 'm'
    else:
        suffix = 'i'

    #set units
    beam.update_units('length', unitoptions_form.cleaned_data[f'length_{suffix}'])
    beam.update_units('force', unitoptions_form.cleaned_data[f'force_{suffix}'])
    beam.update_units('moment', unitoptions_form.cleaned_data[f'moment_{suffix}'])
    beam.update_units('distributed', unitoptions_form.cleaned_data[f'distributed_{suffix}'])
    beam.update_units('stiffness', unitoptions_form.cleaned_data[f'stiffness_{suffix}'])
    beam.update_units('A', unitoptions_form.cleaned_data[f'A_{suffix}'])
    beam.update_units('E', unitoptions_form.cleaned_data[f'E_{suffix}'])
    beam.update_units('I', unitoptions_form.cleaned_data[f'I_{suffix}'])
    beam.update_units('deflection', unitoptions_form.cleaned_data[f'deflection_{suffix}'])

    # add supports to beam
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

    # add point loads to beam
    for pointload_form in pointload_formset.cleaned_data:
        if pointload_form:
            beam.add_loads(
                PointLoad(
                    force = pointload_form['force'],
                    coord = pointload_form['coordinate'],
                    angle = pointload_form['angle'],
                )
            )
    
    # add point torques to beam
    for pointtorque_form in pointtorque_formset.cleaned_data:
        if pointtorque_form:
            beam.add_loads(
                PointTorque(
                    force = pointtorque_form['torque'],
                    coord = pointtorque_form['coordinate'],
                )
            )

    # add distributed loads to beam
    for distributedload_form in distributedload_formset.cleaned_data:
        if distributedload_form:
            beam.add_loads(
                TrapezoidalLoadV(
                    force = (distributedload_form['start_load'],distributedload_form['end_load']),
                    span = (distributedload_form['start_coordinate'],distributedload_form['end_coordinate'])
                )
            )
    
    # add query to beam
    for query_form in query_formset.cleaned_data:
        if query_form:
            beam.add_query_points(query_form['query'])

    # analyse beam
    beam.analyse()

    return beam