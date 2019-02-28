from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from .models import UserModel


# Create your views here.
def index(request):

    # if(request.method == "POST"):

    allEntries = UserModel.objects.all()
    form = UserForm()
    context = {
        "requestMethod": request.method,
        "allEntries": allEntries,
        "form": form,
    }
    return render(request, "ValidationApp/index.html", context)