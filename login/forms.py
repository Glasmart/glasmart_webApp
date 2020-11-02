''' User profile form '''

# Django
from django import forms

class ProfileForm(forms.Form):
    ''' Profile Form '''

    website = forms.URLField(max_length=200, required=True)
    bio = forms.CharField (max_length=500, required=False)
    picture = forms.ImageField()