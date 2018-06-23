from django.shortcuts import render, redirect
# from .models import Contact
# from .forms import ContactForm


# Create your views here.


def index(request):
    return render(request, 'index.html')


# Create your views here.
