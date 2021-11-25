from django.contrib import admin
from .models import (
    BeamModel,
    SupportModel,
    PointLoadModel,
    PointTorqueModel,
    DistributedLoadModel,
    QueryModel,
    UnitOptionsModel,
)

# Register your models here.
admin.site.register(BeamModel)
admin.site.register(SupportModel)
admin.site.register(PointLoadModel)
admin.site.register(PointTorqueModel)
admin.site.register(DistributedLoadModel)
admin.site.register(QueryModel)
admin.site.register(UnitOptionsModel)
