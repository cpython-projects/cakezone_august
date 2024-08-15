from django import forms
from .models import MessageFromCustomer


class MessageFromCustomerForm(forms.ModelForm):
    class Meta:
        model = MessageFromCustomer
        fields = ('name', 'email', 'subject', 'message')