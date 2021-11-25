from django.shortcuts import render
from django.http import HttpResponse
from django.forms import modelformset_factory

from indeterminatebeam import Beam,Support
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
    SupportFormSet = modelformset_factory(SupportModel, form=SupportForm, extra=3) 
    PointLoadFormSet = modelformset_factory(PointLoadModel, form = PointLoadForm, extra = 3)
    PointTorqueFormSet = modelformset_factory(PointTorqueModel, form = PointTorqueForm, extra = 3)
    DistributedLoadFormSet = modelformset_factory(DistributedLoadModel, form = DistributedLoadForm, extra = 3)
    QueryFormSet = modelformset_factory(QueryModel, form = QueryForm, extra = 1)


    if request.method == 'GET':
        beam_form = BeamForm()
        
        support_formset = SupportFormSet(queryset=SupportModel.objects.none())
        pointload_formset = PointLoadFormSet(queryset=PointLoadModel.objects.none())
        pointtorque_formset = PointTorqueFormSet(queryset= PointTorqueModel.objects.none())
        distributedload_formset = DistributedLoadFormSet(queryset = DistributedLoadModel.objects.none())
        query_formset = QueryFormSet(queryset = QueryModel.objects.none())

        unitoptions_form = UnitOptionsForm()

        # TO DO -- properly implement the beam creation (more for post request i guess, but get may be important for when there is already data present)
        empty_beam = Beam()
        empty_beam.add_supports(Support(0,(1,1,1)))
        empty_beam.analyse()

        plot_int = empty_beam.plot_beam_internal()
        plot_int.update_layout(autosize=True)
        plot_int = plot_int.to_html()

        plot_ext = empty_beam.plot_beam_diagram()
        plot_ext.update_layout(autosize=True)
        plot_ext = plot_ext.to_html()
        
        return render(request, 'beam/index.html', {
            'beam_form' : beam_form,            
            'support_formset' : support_formset,
            'pointload_formset' : pointload_formset,
            'pointtorque_formset' : pointtorque_formset,
            'distributedload_formset' : distributedload_formset,
            'query_formset' : query_formset,
            'unitoptions_form' : unitoptions_form,
            'beam': empty_beam,
            'plot_int': plot_int,
            'plot_ext': plot_ext,
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
