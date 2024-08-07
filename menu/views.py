from django.shortcuts import render
from django.http import HttpResponse
from .models import Category


# Create your views here.
def index(request):
    categories = Category.objects.all().order_by('-sort')
    return HttpResponse(categories)