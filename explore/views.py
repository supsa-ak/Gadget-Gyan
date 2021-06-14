from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'explore/index.html')

def about(request):
    return render(request, 'explore/about.html')

def contact(request):
    return render(request, 'explore/compare.html')

def search(request):
    return render(request, 'explore/contact.html')

def prodView(request):
    return render(request, 'explore/product.html')

def Compare(request):
    return render(request, 'explore/search.html')