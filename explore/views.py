from django.shortcuts import render
from .models import Product

from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'explore/index.html')

def about(request):
    return render(request, 'explore/about.html')

def contact(request):
    return render(request, 'explore/contact.html')

def search(request):
    return render(request, 'explore/search.html')

def prodView(request):
    products = Product.objects.all()
    # print(products)
    n = len(products)
    params = {'range': range(1,n), 'product': products}
    return render(request, 'explore/product.html', params)

def Compare(request):
    return render(request, 'explore/search.html')