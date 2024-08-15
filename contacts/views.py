from django.shortcuts import render
from .models import Contacts
from .forms import MessageFromCustomerForm


# Create your views here.
def index(request):
    context = {
        'message_form': MessageFromCustomerForm(),
        'contacts': Contacts.objects.first()
    }
    return render(request, 'contacts.html', context=context)