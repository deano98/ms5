from django.shortcuts import render
from .models import SubType, SubFeatures
from .forms import TdeeForm
from django.views.generic.edit import View
import stripe
from djstripe.models import Product
import os
from flask import Flask, redirect, jsonify, json, request, current_app
from django.conf import settings


# Create your views here.

def subscription(request):
    ''' View to return the subscription page '''
    if request.method == 'POST':
        tdee_data = request.POST
        gender = tdee_data.get("gender")
        weight = float(tdee_data.get("weight"))
        height = float(tdee_data.get("height"))
        age = float(tdee_data.get("age"))
        activity = tdee_data.get("activity")
        multiplier = 1

        print(tdee_data)

        if gender == "male":
            BMR = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
        else:
            BMR = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)

        if activity == "sedentary":
            multiplier = 1.2
        elif activity == "light":
            multiplier = 1.375
        elif activity == "moderate":
            multiplier = 1.55
        elif activity == "heavy":
            multiplier = 1.725
        else:
            multiplier = 1.9

        user_tdee = BMR * multiplier
        print(BMR)
        print(multiplier)
        print(user_tdee)

    return render(request, 'subscription/subscription.html', {
        'tdee_form': TdeeForm(),
        'products': Product.objects.all()
    })

def subscribe(request):
    ''' View to return the subscribe page '''
    
    return render(request, 'subscription/checkout.html', {
        'stripe_public_key': 'pk_test_51KPpqoJAp5w3wtxOcLHWfFgiHHtZGpp0tNj4ecSzSQSWJiCZoKIZxcLN06mdCEFAMRyTuIu9qVDaXH0NMxF1Yur1009lNv4heh',
        'client_secret': 'test client secret',
    })

# stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

# class CreateCheckoutSession(View):
#     ''' Checkout session view'''
#     def post(self, request, *args, **kwargs):
#         ''' post function '''
#         price_id = '{{PRICE_ID}}'

#         session = stripe.checkout.Session.create(
#         success_url='https://example.com/success.html?session_id={CHECKOUT_SESSION_ID}',
#         cancel_url='https://example.com/canceled.html',
#         mode='subscription',
#         line_items=[{
#             'price': price_id,
#             # For metered billing, do not pass quantity
#             'quantity': 1
#         }],
#         )