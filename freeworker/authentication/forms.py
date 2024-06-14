from  django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class LoginFrom(forms.Form):
          
     """
     on créé notre model de formulaire LoginForm

     Args:
        forms (object): on hérite du model de formulaire de django
     """
     username = forms.CharField(max_length=63, label="Nom d'utilisateur")
     password = forms.CharField(
         max_length=63, widget=forms.PasswordInput, label="mot de passe"
    )


class SignupForm(UserCreationForm):
    """
    on créé nôtre model de formulaire SignupForm

    Args:
        UserCreationForm (object): on hérite du model de formulaire d'authentification de django
    """

class Meta(UserCreationForm.Meta):
    model = get_user_model()
    fields = ["username"]
    labels = {
            "username": "Nom d'utilisteur",
        }