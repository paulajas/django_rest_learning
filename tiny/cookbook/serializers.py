from rest_framework import serializers
from datetime import datetime

from .models import Receipe, Cookbook, ReceipeCookbook
from .request_mixin import ModelAdminRequestMixin
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


class ReceipeSerializer(serializers.Serializer):

    pk = serializers.IntegerField(read_only=True)
    text_receipe=serializers.CharField(style={'base_template': 'textarea.html'}, required=True)
    alcohol=serializers.BooleanField()
    name=serializers.CharField(required=True)
    creation_date = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        print(validated_data)
        if validated_data['alcohol'] == 'None':
            validated_data['alcohol'] = None
        validated_data['creation_date'] = datetime.now()
        print(validated_data)
        return Receipe.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.text_receipe = validated_data.get('text_receipe', instance.text_receipe)
        instance.alcohol = validated_data.get('alcohol', instance.alcohol)
        instance.save()
        return instance


class ReceipeCookbookNewSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReceipeCookbook
        fields="__all__"

    # receip = serializers.SerializerMethodField('_is_my_receip')
    # cook = serializers.SerializerMethodField('_is_my_cook')

    # def _is_my_receip(self, obj):
    #     receip = self.context.get("receip")
    #     return receip
    # def _is_my_cook(self, obj):
    #     cook = self.context.get("cook")
    #     return cook

    def create(self, validated_data):
        receip = self.context.get("receip")
        cook = self.context.get("cook")
        validated_data['receipe'] = Receipe.objects.get(pk=receip)
        validated_data['cookbook'] = Cookbook.objects.get(pk=cook)
        print(validated_data.__dict__)
        return ReceipeCookbook.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.rate = validated_data.get('name', instance.rate)
        instance.make_date = validated_data.get('name', instance.make_date)
        instance.save()
        return instance


class CookbookSerializer(serializers.Serializer):

    # def validate_name(self, value):
    #     if len(value) > 500:
    #         raise serializers.ValidationError("Name is to long!")
    #     else:
    #         return value

    pk=serializers.IntegerField(read_only=True)
    name=serializers.CharField(required=True)
    rate=serializers.IntegerField(required=False)
    # receipecookbook = ReceipeCookbookSerializer(many=True, read_only=True)
    
    def create(self, validated_data):
        validated_data['creation_date'] = datetime.now()
        return Cookbook.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.rate_cookbook = validated_data.get('rate_cookbook', instance.rate_cookbook)
        instance.save()
        return instance


class ReceipeCookbookSerializer(serializers.Serializer):


    pk=serializers.IntegerField(read_only=True)
    rate=serializers.IntegerField()
    make_date=serializers.DateField()
    receipe = serializers.PrimaryKeyRelatedField(read_only=True, default=ReceipeSerializer())
    cookbook = serializers.PrimaryKeyRelatedField(read_only=True, default=CookbookSerializer())

    def _is_my_find(self, obj):
        extra_data = self.context.get("extra_data")
        return extra_data

    def create(self, validated_data):
        receip = self.context.get("receip")
        cook = self.context.get("cook")
        validated_data['receipe'] = Receipe.objects.get(pk=receip)
        validated_data['cookbook'] = Cookbook.objects.get(pk=cook)
        return ReceipeCookbook.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.rate = validated_data.get('name', instance.rate)
        instance.make_date = validated_data.get('name', instance.make_date)
        instance.save()
        return instance

class ReceipeReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipe
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
                max_length=32,
                validators=[UniqueValidator(queryset=User.objects.all())]
                )
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
                                        validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
