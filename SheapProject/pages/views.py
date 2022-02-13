from django.shortcuts import render
from django.http import HttpResponse
#from django.template import render_to_response
# Create your views here.

def base(request):
    return render(request, 'templates/index.html')
    #return render_to_response('index.html',{},context_instance=RequestContext(request))
