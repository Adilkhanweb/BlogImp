from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    page = Page.objects.first()
    context = {
        "page": page
    }
    return render(request, 'streamblocks/home.html', context)
