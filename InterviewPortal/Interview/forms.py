from django import forms
from .models import Interview

class InterviewForm(forms.Form):

    class Meta:
        model = Interview
        fields = '__all__'
