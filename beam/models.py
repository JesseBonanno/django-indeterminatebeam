from django.db import models
from indeterminatebeam.units import IMPERIAL_UNITS, METRIC_UNITS, UNIT_KEYS, UNIT_VALUES, default_units


def create_unit_field(unit='length', metric=True):
    if metric:
        choices = [(k,k) for k in METRIC_UNITS[unit].keys()]
        default = default_units['metric'][unit]
    else:
        choices = [(k,k) for k in IMPERIAL_UNITS[unit].keys()]
        default = default_units['imperial'][unit]

    return models.CharField(
        max_length=10,
        choices=choices,
        default=default,
    )

# Create your models here.
class BeamModel(models.Model):
    # id = models.AutoField(primary_key=True)

    length = models.FloatField(default=5.0)
    E = models.FloatField(default = 200*10**9)
    I = models.FloatField(default = 0.00000905)
    A = models.FloatField(default = 0.23)

    def __str__(self):
        return f'beam-{self.id}'

class SupportModel(models.Model):
    support_choices = (
        ('Fixed', 'Fixed'),
        ('Pinned', 'Pinned'),
        ('Roller', 'Roller')
    )
    coordinate = models.FloatField(default=0)
    support = models.CharField(max_length = 10, choices=support_choices, default='Fixed')

    beam = models.ForeignKey(BeamModel, on_delete=models.CASCADE, related_name='supports')

class PointLoadModel(models.Model):
    coordinate = models.FloatField(default=0)
    force = models.FloatField(default=0)
    angle = models.FloatField(default = 90)

    beam = models.ForeignKey(BeamModel, on_delete=models.CASCADE, related_name='point_loads')

class PointTorqueModel(models.Model):
    coordinate = models.FloatField(default=0)
    torque = models.FloatField(default=0)

    beam = models.ForeignKey(BeamModel, on_delete=models.CASCADE, related_name='point_torques')

class DistributedLoadModel(models.Model):
    start_coordinate = models.FloatField(default=0)
    end_coordinate = models.FloatField(default=0)
    start_load = models.FloatField(default=0)
    end_load = models.FloatField(default=0)

    beam = models.ForeignKey(BeamModel, on_delete=models.CASCADE, related_name='distributed_loads')

class QueryModel(models.Model):
    query = models.FloatField(default = 0)

    beam = models.ForeignKey(BeamModel, on_delete=models.CASCADE, related_name='queries')

# add class for unit choice
# seperate metric and imperial,
# hide one or the other with js or whatever
# 

class UnitOptionsModel(models.Model):

    units = models.CharField(
        max_length=64,
        choices=(
            ('metric','metric'),
            ('imperial','imperial'),
        ),
        default='SI'
    )

    length_m = create_unit_field('length')
    force_m = create_unit_field('force')
    moment_m = create_unit_field('moment')
    distributed_m = create_unit_field('distributed')
    stiffness_m = create_unit_field('stiffness')
    A_m = create_unit_field('A')
    E_m = create_unit_field('E')
    I_m = create_unit_field('I')
    deflection_m = create_unit_field('deflection')

    length_i = create_unit_field('length', metric=False)
    force_i = create_unit_field('force', metric=False)
    moment_i = create_unit_field('moment', metric=False)
    distributed_i = create_unit_field('distributed', metric=False)
    stiffness_i = create_unit_field('stiffness', metric=False)
    A_i = create_unit_field('A', metric=False)
    E_i = create_unit_field('E', metric=False)
    I_i = create_unit_field('I', metric=False)
    deflection_i = create_unit_field('deflection', metric=False)

    beam = models.OneToOneField(
        BeamModel,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='units'
    )





