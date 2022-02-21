from django.shortcuts import render

# Create your views here.

def shop(request):
    ''' View to return the shop page '''
    return render(request, 'shop/shop.html')