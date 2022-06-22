from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

    def save_form(self, *args, **kwargs):
        save_object = super(RegisterForm, self).save(*args, **kwargs)
        save_object.is_staff=True
        save_object.save()
        my_group = Group.objects.get(name='masy') 
        my_group.user_set.add(save_object)