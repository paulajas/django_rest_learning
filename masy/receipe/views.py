from curses.ascii import US
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(response):
    if response.method == "POST":
        form=UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/receipe/")
        else:
            form = UserCreationForm()


    form=UserCreationForm
    return render(response, "receipe/register.html", {"form":form})
