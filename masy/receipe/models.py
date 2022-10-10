from datetime import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField
import functools
from polymorphic.models import PolymorphicModel
from polymorphic.query import PolymorphicQuerySet
from django.conf import settings


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


class Receipe(PolymorphicModel):
    version = 1 #atr. klasowy
    class Choices(models.TextChoices):
        EASY = "easy", _("Easy to make")
        MEDIUM = "medium", _("Not so hard")
        HARD = "hard", _("A bit harder than others receipes")
    name = models.CharField(max_length=150)
    make_time = models.IntegerField(null=True)
    hard_level = models.CharField(max_length=6, choices=Choices.choices) # atrybut złożony
    kcal = models.IntegerField(null=True) # atr. opcjonalny
    text_receipe = models.TextField()
    alergens = ArrayField(models.CharField(max_length=200), blank=True, null=True) # atr. powtarzalny
    for_children = models.BooleanField(default=True)
    make_date = models.DateField(null=True, blank=True) 
    days_from_add = models.DurationField(null=True, blank=True) # wyliczalny atrybut pochodny
    
    picture=models.ForeignKey("Picture", on_delete=models.SET_NULL, null=True, blank=True, to_field="image_no") #asocjacja kwalifikowana
    cookbook = models.ManyToManyField("CookBook", through="CookBookReceipe")
    country = models.ForeignKey("Country", on_delete=models.CASCADE) #kompozycja
    tag = models.ManyToManyField("TagCountry", related_name="tag_country_id", blank=True) # zwykła
    # część nie może być współdzielona - foreign key,
    # część nie może istnieć bez całości - nie dopuszczam null,
    # gdy usuwam całość usuwają się również jej części - on_delete= CASCADE

    def __str__(self):
        return f"Receipe {self.name}"

    def save(self, *args, **kwargs):
        self.days_from_add = self.make_date - datetime.now().date()
        super(Receipe, self).save(*args, **kwargs)


class MeatReceipe(Receipe):
    meat_kind = models.CharField(max_length=200, null=True, blank=True)
    meat_type = models.CharField(max_length=200, null=True, blank=True)
     # asocjacja z atrybutem
    def __str__(self):                                # przesłonięcie metody
        return f"Meat receipe {self.name}"

    
    @functools.singledispatchmethod # przeciążanie metod
    def find_receipe(self, args):
        raise NotImplementedError()
    @find_receipe.register
    def _(self, arg: int):
        return MeatReceipe.objects.get(pk=arg)
    @find_receipe.register
    def _(self, arg: str):
        return MeatReceipe.objects.get(meat_kind=arg)

class VegeReceipe(Receipe):
    protein_type = models.CharField(max_length=200, null=True)
    vege_type = models.CharField(max_length=200, blank=True)

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


class BreakfastReceipe(Receipe):
    sweet = models.BooleanField(default=False)
    class ChoiceBreakfast(models.TextChoices): # dynamic inheritance
        DAIRY = "dairy", _("Including dairy")
        MEAT = "meat", _("Including meat")
    kind = models.CharField(max_length=6, choices=ChoiceBreakfast.choices)


class LunchReceipe(Receipe):
    digest_hard=models.BooleanField(default=False)
    to_microwave=models.BooleanField(default=False)


class DinnerReceipe(Receipe):
    before_bed_time = models.TimeField()


class SnackReceipe(Receipe):
    sweet = models.BooleanField()
    boiled = models.BooleanField()


class Picture(models.Model):
    image = models.ImageField(null=True, blank=True) #add directory for upload
    image_no = models.CharField(max_length=10, unique=True) # asocjacja kwalifikowana


class CookBook(models.Model):
    name = models.CharField(max_length=30)
    public = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    class Meta:
        permissions = (
            ('change_book', 'Can change book'),
        )


class Country(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self):
        return f"{self.name}"




class Tag(models.Model):
    tag_text = models.CharField(max_length=300)
    class Meta:
        abstract=True

class TagCountry(Tag):
    name_in_country_language = models.CharField(max_length=300)
    name_in_english = models.CharField(max_length=300)
    country = models.ForeignKey("Country", on_delete=models.CASCADE)

    @classmethod
    def search_name_in_country(cls, country_id):
        return Receipe.objects.filter(country=country_id)

    @classmethod
    def search_name_in_english(cls, obj):
        return Receipe.objects.filter(tag=obj)


class City(models.Model):
    name=models.TextField()
    country=models.ForeignKey("Country", on_delete=models.CASCADE)


class Animal(models.Model):
    kind=models.TextField()
    