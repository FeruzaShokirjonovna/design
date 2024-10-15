from django.shortcuts import render

def home(request):
    return render(request, 'products/home.html')

def product_detail(request, id):
    return render(request, 'products/product_detail.html')
