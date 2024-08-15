from django.contrib import admin
from .models import Contacts, MessageFromCustomer


# Register your models here.
admin.site.register(Contacts)
admin.site.register(MessageFromCustomer)