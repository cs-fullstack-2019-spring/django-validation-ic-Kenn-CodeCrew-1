from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm, CocktailForm
from .models import UserModel, CocktailModel


# Create your views here.
def index(request):

    if(request.method == "POST"):
        form = UserForm(request.POST)

        # If your form has clean data, create a new entry
        if(form.is_valid()):
            UserModel.objects.create(username = request.POST["username"], password = request.POST["password"], age = request.POST["age"])
        else:
            print(form.errors)
            allEntries = UserModel.objects.all()
            context = {
                "someErrors": form.errors,
                "allEntries": allEntries,
                'form': UserForm(),
            }
            return render(request, "ValidationApp/index.html", context)

    allEntries = UserModel.objects.all()
    form = UserForm()
    context = {
        "requestMethod": request.method,
        "allEntries": allEntries,
        "form": form,
    }
    return render(request, "ValidationApp/index.html", context)

def cocktails(request):
    if(request.method == "POST"):
        form = CocktailForm(request.POST)
        if(form.is_valid()):
            CocktailModel.objects.create(name=request.POST["name"], alcoholContent = request.POST["alcoholContent"], servingContainer = request.POST["servingContainer"])
        else:
            context = {
                "errors": form.errors,
                "form": form,
                "allEntries": CocktailModel.objects.all(),
            }
            return render(request, "ValidationApp/cocktail.html", context)

    context = {
        "allEntries": CocktailModel.objects.all(),
        "form": CocktailForm(),
    }
    return render(request, "ValidationApp/cocktail.html", context)
