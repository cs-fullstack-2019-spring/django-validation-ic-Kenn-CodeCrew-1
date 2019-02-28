from django import forms
from .models import UserModel, CocktailModel

class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = "__all__"

    def clean_username(self):
        usernameData = self.cleaned_data["username"]

        validateData = str(usernameData).lower()
        if "poop" in validateData:
            raise forms.ValidationError("Please don't use poop...")

        return usernameData

    def clean_age(self):
        ageData = self.cleaned_data["age"]

        if ageData < 13:
            raise forms.ValidationError("Go back to Barney!!!!")

        return ageData


class CocktailForm(forms.ModelForm):
    class Meta:
        model = CocktailModel
        fields = "__all__"
        # labels = {"alcoholContent": "Alcohol Content (in %)"}

    def clean_alcoholContent(self):
        boozeData = self.cleaned_data["alcoholContent"]

        if boozeData<5:
            raise forms.ValidationError("Not enough!!")

        if boozeData> 70:
            raise forms.ValidationError("It's too strong")

        return boozeData
