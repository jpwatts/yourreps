from django.contrib.gis import admin
from yourreps.models import Layer, District, Representative

admin.site.register(Layer, admin.ModelAdmin)
admin.site.register(District, admin.GeoModelAdmin)
admin.site.register(Representative, admin.ModelAdmin)
