from datetime import datetime
from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField
import functools
from polymorphic.models import PolymorphicModel
from polymorphic.query import PolymorphicQuerySet

# # Create your models here.

class CookBookReceipe(models.Model):
    cookbook = models.ForeignKey("CookBook", on_delete=models.CASCADE) 
    receipe = models.ForeignKey("Receipe", on_delete=models.CASCADE)
    class RatioChoice(models.IntegerChoices):
        BAD = 1
        LOWER_MEDIUM = 2
        MEDIUM =3
        LOWER_GOOD = 4
        GOOD = 5
        EXCELENT = 6
    ratio = models.IntegerField(choices=RatioChoice.choices) # asocjacja z atrybutem


# class CountryReceipe(models.Model):
#     to_receipe = models.ForeignKey("Receipe", on_delete=models.CASCADE)
#     to_country = models.ForeignKey("Country", on_delete=models.CASCADE)

# class PictureReceipe(models.Model):
#     picture = models.ForeignKey("Picture", to_field="image_no", on_delete=models.CASCADE)
#     receipe = models.ForeignKey("Receipe", on_delete=models.CASCADE) 


class ReceipeQuerySet(PolymorphicQuerySet):

    def delete(self, *args, **kwargs):
        for obj in self:
            if Receipe.objects.filter(country=obj.country):
                super(ReceipeQuerySet, self).delete(*args, **kwargs)
            else:
                obj.country.delete()
                super(ReceipeQuerySet, self).delete(*args, **kwargs)


class Receipe(PolymorphicModel):
    objects = ReceipeQuerySet.as_manager()
    version = 1 #atr. klasowy
    class Choices(models.TextChoices):
        EASY = "easy", _("Easy to make")
        MEDIUM = "medium", _("Not so hard")
        HARD = "hard", _("A bit harder than others receipes")
    name = models.CharField(max_length=150)
    make_time = models.IntegerField(null=True)
    hard_level = models.CharField(max_length=6, choices=Choices.choices) # atrybut złożony
    kcal = models.IntegerField(null=True) # atr. opcjonalny
    text_receipe = models.TextField(null=True)
    alergens = ArrayField(models.CharField(max_length=200), blank=True, null=True) # atr. powtarzalny
    for_children = models.BooleanField(default=True)
    make_date = models.DateField() 
    days_from_add = models.DurationField(null=True) # wyliczalny atrybut pochodny
    
    picture=models.ForeignKey("Picture", on_delete=models.SET_NULL, null=True, blank=True, to_field="image_no") #asocjacja kwalifikowana
    cookbook = models.ManyToManyField("CookBook", through="CookBookReceipe") # asocjacja z atrybutem
    country = models.ForeignKey("Country", on_delete=models.CASCADE) #kompozycja
    # część nie może być współdzielona - foreign key,
    # część nie może istnieć bez całości - nie dopuszczam null,
    # gdy usuwam całość usuwają się również jej części - on_delete= CASCADE

    def delete(self, *args, **kwargs):
        if Receipe.objects.filter(country=self.country):
            super(ReceipeQuerySet, self).delete(*args, **kwargs)
        else:
            self.country.delete()
            super(ReceipeQuerySet, self).delete(*args, **kwargs)

    # def clean(self):
    #     if self.kcal < 0:
    #         raise ValidationError("It must contains kcal")

    # class Meta:
    #     abstract = True
    
    def __str__(self):
        return f"Receipe {self.name}"

    def save(self, *args, **kwargs):
        self.days_from_add = self.make_date - datetime.now().date()
        super(Receipe, self).save(*args, **kwargs)


class MeatReceipe(Receipe):
    meat_kind = models.CharField(max_length=200)
    meat_type = models.CharField(max_length=200)
    tag = models.ManyToManyField("Tag") # zwykła
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


# class BreakfastReceipe(Receipe):
#     sweet = models.BooleanField(default=False)


# class LunchReceipe(Receipe):
#     digest_hard=models.BooleanField(default=False)


# class DinnerReceipe(Receipe):
#     before_bed_time = models.TimeField()


# class SnackReceipe(Receipe):
#     sweet = models.BooleanField()
#     boiled = models.BooleanField()


class Picture(models.Model):
    image = models.ImageField(null=True, blank=True) #add directory for upload
    # to_receipe = models.ManyToManyField("Receipe", through=PictureReceipe)
    image_no = models.CharField(max_length=10, unique=True) # asocjacja kwalifikowana


class CookBook(models.Model):
    name = models.CharField(max_length=30)
    public = models.BooleanField(default=False)
    # receipe = models.ManyToManyField(Receipe, through=CookBookReceipe)
    # many to many via class


class Country(models.Model):
    # to_receipe = models.ManyToManyField("CountryReceipe")
    # one to many with receipe - agregation -> Composition, because of lack of null, on_delete=CASCADE and ForeignKey
    name = models.CharField(max_length=300)


class Tag(models.Model):
    # receipe = models.ManyToManyField("MeatReceipe") #zwykła
    name = models.CharField(max_length=300)
