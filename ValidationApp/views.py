from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from .models import UserModel


# Create your views here.
def index(request):

    if(request.method == "POST"):
        print(request.POST)
        UserModel.objects.create(username = request.POST["username"], password = request.POST["password"], age = request.POST["age"])

    allEntries = UserModel.objects.all()
    form = UserForm()
    context = {
        "requestMethod": request.method,
        "allEntries": allEntries,
        "form": form,
    }
    return render(request, "ValidationApp/index.html", context)
