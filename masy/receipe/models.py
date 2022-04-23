from datetime import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField
import functools

# # Create your models here.

class Receipe(models.Model):
    version = 1 #atr. klasowy
    class Choices(models.TextChoices):
        EASY = "easy", _("Easy to make")
        MEDIUM = "medium", _("Not so hard")
        HARD = "hard", _("A bit harder than others receipes")
    name = models.CharField(max_length=150)
    make_time = models.IntegerField(null=True)
    hard_level = models.CharField(max_length=6, choices=Choices.choices) # atrybut złożony
    kcal = models.IntegerField(null=True) # atr. opcjonalny
    receipe = models.TextField(null=True)
    alergens = ArrayField(models.CharField(max_length=200), blank=True, null=True) # atr. powtarzalny
    for_children = models.BooleanField(default=True)
    make_date = models.DateField() 
    days_from_add = models.DurationField(null=True) # wyliczalny atrybut pochodny
    
    # def clean(self):
    #     if self.kcal < 0:
    #         raise ValidationError("It must contains kcal")

    class Meta:
        abstract = True
    
    def __str__(self):
        return f"Receipe {self.name}"

    def save(self, *args, **kwargs):
        self.days_from_add = self.make_date - datetime.now().date()
        super(Receipe, self).save(*args, **kwargs)


class MeatReceipe(Receipe):
    meat_kind = models.CharField(max_length=200)
    meat_type = models.CharField(max_length=200)
    # meat_kind_counter
    def __str__(self):                                # przesłonięcie metody
        return f"Meat receipe {self.name}"

class VegeReceipe(Receipe):
    protein_type = models.CharField(max_length=200)
    vege_type = models.CharField(max_length=200)
    def __str__(self):
        return f"Vege receipe {self.name}"

    @classmethod
    def _(cls,protein_type, vege_type, receipe): # classmethod
        name_tmp = protein_type + vege_type
        return VegeReceipe(
                protein_type=protein_type,
                vege_type=vege_type,
                receipe =receipe,
                name = name_tmp,
                for_children=True,
                create_date=datetime.now().date()
                )
    
    @functools.singledispatchmethod # przeciążanie metod
    def find_receipe(self, args):
        raise NotImplementedError()
    @find_receipe.register
    def _(self, arg: int):
        return VegeReceipe.objects.get(pk=arg)
    @find_receipe.register
    def _(self, arg: str):
        return VegeReceipe.objects.get(name=arg)


