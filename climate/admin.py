from django.contrib import admin
from climate.models import Climate
import csv
from django.http import StreamingHttpResponse

def stream_csv_export(description="Export selected objects as CSV file", fields=None, exclude=None, header=True):
    def export_as_csv(modeladmin, request, queryset):
        class Echo(object):
            def write(self, value): return value

        opts = modeladmin.model._meta

        def csv_output():
            if header:
                head = []
                for field in modeladmin.list_display:
                    head.append(str(field).replace('_', ' ').title())
                yield head
            for obj in queryset:
                row = []
                for field in modeladmin.list_display:
                    if hasattr(modeladmin, str(field)):
                        row.append(unicode(getattr(modeladmin, str(field))(obj)).encode("utf-8", "replace"))
                    else:
                        row.append(unicode(getattr(obj, str(field))).encode("utf-8", "replace"))
                yield row

        writer = csv.writer(Echo())
        response = StreamingHttpResponse((writer.writerow(row) for row in csv_output()), content_type="text/csv")
        response['Content-Disposition'] = 'attachment; filename=%s.csv' % unicode(opts).replace('.', '_')

        return response

    export_as_csv.short_description = description
    return export_as_csv

class ClimateAdmin(admin.ModelAdmin):

	list_display = ('name', 'year', 'sevoflurane', 'isofluroane', 'desflurane', 'n2o')
	actions = [stream_csv_export(),]

admin.site.register(Climate, ClimateAdmin)