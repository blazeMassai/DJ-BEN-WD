from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    name="Johnny"
    return render(request, 'base.html', {"name":name} )