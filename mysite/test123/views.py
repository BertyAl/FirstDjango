from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def shop_detail(request):
    return render(request, 'shop-detail.html')

def shop_listing(request):
    return render(request, 'shop-listing.html')