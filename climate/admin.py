from django.contrib import admin
from climate.models import Climate

# Register your models here.

class ClimateAdmin(admin.ModelAdmin):

	list_display = ('name', 'year', 'sevoflurane', 'isofluroane', 'desflurane', 'n2o')

admin.site.register(Climate, ClimateAdmin)