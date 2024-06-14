from django.shortcuts import render, redirect
from authentication import forms
from django.contrib.auth import login, authenticate, logout
from django.conf import settings

# Create your views here.


def login_page(request):
    """
    on gère la view de connection à partir du formulaire LoginForm

    Args:
        request (object): requete http

    Returns:
        httpresponse: on retourne la requete http, le template visé avec les variables de gabarit
    """
    form = forms.LoginForm()
    message = ""
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                pass
            else:
                message = "identifiants ou mot de passe invalide"
    if request.user.is_authenticated:
        pass
    return render(
        request, "", context={"form": form, "message": message}
    )


def logout_user(request):
    logout(request)
    return redirect("login")


def signup_page(request):
    """
    on gère la view d'inscription à partir du formulaire LoginForm

    Args:
        request (object): requete http

    Returns:
        httpresponse: on retourne la requete http, le template visé avec les variables de gabarit
    """
    form = forms.SignupForm()
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, "", context={"form": form})