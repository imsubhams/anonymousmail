from django import forms
from anonmail import models

class sendEmailForm(forms.ModelForm):
    to= forms.EmailField(max_length=50, required = True, label='to_email')
    subject = forms.CharField(max_length=50, required = True)
    message = forms.CharField(max_length = 100, required=True, widget = forms.Textarea(attrs={'class' : 'textinput', 'rows':'10'}))
    class Meta:
        model = models.sendEmailModel
        fields = [
            'to',
            'subject',
            'message',
        ]