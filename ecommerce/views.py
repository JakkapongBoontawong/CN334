from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ecommerce_index_view(request):
    '''This function render index page of ecommerce views'''
    return HttpResponse('Welcome to 6410742339 jakkapong Boontawong views!')

def item_view(request, item_id):
    context_data = {
        "item_id": item_id   
    }
    return render(request, 'index.html',context= context_data)

def Home_view(request):
    
    return render(request, 'HomePage.html')

def Category_view(request):
    
    return render(request, 'categoryPage.html')

def Product_view(request):
    
    return render(request, 'ProductPage.html')

def Checkout_view(request):
    
    return render(request, 'checkoutPage.html')

def Contact_view(request):
    
    return render(request, 'contactPage.html')