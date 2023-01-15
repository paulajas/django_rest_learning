from django.db import models

# Create your models here.


class Cookbook(models.Model):
    name = models.CharField(max_length=500)
    rate=models.PositiveIntegerField(null=True,blank=True)
    creation_date=models.DateTimeField(auto_created=True)
    receipe=models.ManyToManyField("Receipe", through="ReceipeCookbook")

class Receipe(models.Model):
    name = models.CharField(max_length=500)
    alcohol = models.BooleanField(null=True,blank=True)
    text_receipe = models.TextField()
    creation_date=models.DateTimeField(auto_created=True)

class ReceipeCookbook(models.Model):
    receipe=models.ForeignKey("Receipe", on_delete=models.CASCADE)
    cookbook=models.ForeignKey("Cookbook", on_delete=models.CASCADE)
    rate=models.PositiveIntegerField()
    make_date=models.DateField(null=True,blank=True)