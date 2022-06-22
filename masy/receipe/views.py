from curses.ascii import US
from django.shortcuts import redirect, render
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm


# Create your views here.
def register(response):
    form=RegisterForm()
    if response.method == "POST":
        form=RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/receipe/")
        else:
            form = RegisterForm()
    return render(response, "receipe/register.html", {"form":form})
