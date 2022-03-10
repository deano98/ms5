from django.shortcuts import render
from .models import SubType, SubFeatures
from .forms import TdeeForm

# Create your views here.

def subscription(request):
    ''' View to return the subscription page '''
    tdee = request.POST
    gender = tdee.get("gender")
    weight = float(tdee.get("weight"))
    height = float(tdee.get("height"))
    age = float(tdee.get("age"))
    print(tdee)
    if gender == "male":
        BMR = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
    else:
        BMR = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)

    print(BMR)

    return render(request, 'subscription/subscription.html', {
        'tdee_form': TdeeForm(),
    })