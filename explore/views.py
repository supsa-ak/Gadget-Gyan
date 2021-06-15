from django.shortcuts import render
from .models import Product
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.contrib import auth, messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request, 'explore/index.html')

def about(request):
    return render(request, 'explore/about.html')

def contact(request):
    return render(request, 'explore/contact.html')

def searchMatch(query, item):
    return False

def search(request):
    if request.method == 'POST':
        srch = request.POST['srh']
        if srch:
            match = Product.objects.filter(Q(product_name__icontains=srch))
            if match:
                return render(request, 'explore/search.html', {'sr':match})
            else:
                messages.error(request, 'no result found')
        else:
            return HttpResponseRedirect('/search/')
    return render(request, 'explore/search.html')

def prodView(request):
    products = Product.objects.all()
    # print(products)
    n = len(products)
    params = {'range': range(1,n), 'product': products}
    return render(request, 'explore/product.html', params)

def compare(request):
    if request.method == 'POST':
        cmp = request.POST['cmpr']
        if cmp:
            c = Product.objects.get(id=cmp)
            params = c
        else:
            return HttpResponseRedirect('/compare/')
        return render(request, 'explore/compare.html', params)