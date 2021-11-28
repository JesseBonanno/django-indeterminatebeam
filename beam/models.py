from django.db import models

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

class UnitOptionsModel(models.Model):
    units = models.CharField(max_length=64, default='SI')
    length= models.CharField(max_length=64, default = 'm')
    force = models.CharField(max_length=64, default = 'N')
    moment = models.CharField(max_length=64, default = 'N.m')
    distributed = models.CharField(max_length=64, default = 'N/m')
    stiffness = models.CharField(max_length=64, default = 'N/m')
    A = models.CharField(max_length=64, default='m2')
    E = models.CharField(max_length=64, default = 'Pa')
    I = models.CharField(max_length=64, default = 'm4')
    deflection = models.CharField(max_length=64, default = 'm')

    beam = models.OneToOneField(
        BeamModel,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='units'
    )






