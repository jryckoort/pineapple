from django.contrib import admin
from .models import Wine, Vine, WineRegion, WineCountry

admin.site.register(Wine)
admin.site.register(Vine)
admin.site.register(WineRegion)
admin.site.register(WineCountry)
