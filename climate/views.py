from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import StreamingHttpResponse, HttpResponseRedirect
from .models import Climate

def view(request):

	context = {}

	if request.method == 'POST':
		name = request.POST['name']
		year = request.POST['year']
		sevoflurane = request.POST['sevoflurane']
		isofluroane = request.POST['isofluroane']
		desflurane = request.POST['desflurane']
		n2o = request.POST['n2o']

		Climate.objects.create(
			name=name,
			year=year,
			sevoflurane=sevoflurane,
			isofluroane=isofluroane,
			desflurane=desflurane,
			n2o=n2o,
		)

		context = {
			'footprint': int(year) * int(n2o),
		}


	return TemplateResponse(request, 'climate.html', context)
