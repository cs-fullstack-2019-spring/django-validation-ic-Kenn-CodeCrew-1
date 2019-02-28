from django import forms
from .models import UserModel

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
