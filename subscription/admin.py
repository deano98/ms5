from django.contrib import admin
from .models import SubType, SubFeatures

# Register your models here.

class SubTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
    )

class SubFeaturesAdmin(admin.ModelAdmin):
    list_display = (
        'plan_name',
    )    

admin.site.register(SubType, SubTypeAdmin)
admin.site.register(SubFeatures, SubFeaturesAdmin)