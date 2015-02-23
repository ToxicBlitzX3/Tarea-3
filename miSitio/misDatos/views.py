from django.shortcuts import render
from django.template import RequestContext

from .models import MisDatos

def home(request):
	misdatos = MisDatos.objects.all()
	ctx = { 'misdatos': misdatos }
	print ctx
	return render(request, 'index.html', ctx,
		context_instance=RequestContext(request))