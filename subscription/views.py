from django.shortcuts import render
from .models import SubType, SubFeatures
from .forms import TdeeForm

# Create your views here.

def subscription(request):
    ''' View to return the subscription page '''


    return render(request, 'subscription/subscription.html', {
        'tdee_form': TdeeForm(),
    })