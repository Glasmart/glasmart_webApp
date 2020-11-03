''' User  form '''

# Django
from django import forms

class UserProfileForm(forms.Form):

    id_profile  = forms.NumberInput()
    id_user     = forms.NumberInput()
