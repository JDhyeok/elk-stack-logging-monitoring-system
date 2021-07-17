from django.http.response import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello World");

def hello(request):
    raise Http404("404 error")
    return render(request)