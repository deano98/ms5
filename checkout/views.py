from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your bag")
        return redirect(reverse("shop"))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KPpqoJAp5w3wtxOcLHWfFgiHHtZGpp0tNj4ecSzSQSWJiCZoKIZxcLN06mdCEFAMRyTuIu9qVDaXH0NMxF1Yur1009lNv4heh',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)