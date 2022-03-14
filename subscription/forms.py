from django import forms


GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
]

ACTIVITY_CHOICES = [
    ('sedentary', 'Sedentary (office job)'),
    ('light', 'Light Exercise (1-2 days per week)'),
    ('moderate', 'Moderate Exercise (3-5 days per week)'),
    ('heavy', 'Heavy Exercise (6-7 days per week)'),
    ('athlete', 'Athlete (2x per day)')
]

class TdeeForm(forms.Form):
    ''' Total daily energy expenditure form '''
    gender = forms.ChoiceField(label='Gender', widget=forms.RadioSelect, choices=GENDER_CHOICES)
    age = forms.IntegerField(required=True)
    weight = forms.IntegerField(required=True)
    height = forms.IntegerField(required=True)
    activity = forms.MultipleChoiceField(
        required=True,
        widget=forms.Select,
        choices=ACTIVITY_CHOICES,
    )
