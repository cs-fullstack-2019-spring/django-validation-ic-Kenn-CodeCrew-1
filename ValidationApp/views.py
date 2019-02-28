from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm


# Create your views here.
def index(request):
    form = UserForm()
    context = {
        "form": form
    }
    return render(request, "ValidationApp/index.html", context)