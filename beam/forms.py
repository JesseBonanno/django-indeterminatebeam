from django import forms
from .models import (
    BeamModel,
    SupportModel,
    PointLoadModel,
    PointTorqueModel,
    DistributedLoadModel,
    QueryModel,
    UnitOptionsModel,
)

class BeamForm(forms.ModelForm):
    class Meta:
        model = BeamModel
        fields = ('length','E','I','A')

class SupportForm(forms.ModelForm):
    class Meta:
        model = SupportModel
        fields = ('coordinate', 'support')

class PointLoadForm(forms.ModelForm):
    class Meta:
        model = PointLoadModel
        fields = ('coordinate', 'force','angle')

class PointTorqueForm(forms.ModelForm):
    class Meta:
        model = PointTorqueModel
        fields = ('coordinate', 'torque')

class DistributedLoadForm(forms.ModelForm):
    class Meta:
        model = DistributedLoadModel
        fields =('start_coordinate', 'end_coordinate', 'start_load', 'end_load')

class QueryForm(forms.ModelForm):
    class Meta:
        model = QueryModel
        fields =('query',)

# could potentiall change units options model to be
# a part of the Beam model, and then split into two forms
class UnitOptionsForm(forms.ModelForm):
    class Meta:
        model = UnitOptionsModel
        fields = ('units', 'length', 'force','moment','distributed', 'stiffness', 'A','E','I','deflection')