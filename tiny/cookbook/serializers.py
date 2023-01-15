from rest_framework import serializers
from datetime import datetime

from .models import Receipe, Cookbook, ReceipeCookbook
from .request_mixin import ModelAdminRequestMixin
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status

global COOKBOOK_GLOB
global RECEIPE_GLOB

class ReceipeSerializer(serializers.Serializer):

    pk = serializers.IntegerField(read_only=True)
    text_receipe=serializers.CharField(required=True)
    alcohol=serializers.BooleanField(required=False)
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


class ReceipeCookbookNewAV(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cr-new.html'
    def get(self, request):
        return Response({"error": "Nothing to show"}, status=status.HTTP_200_OK)

    def post(self,request):
        COOKBOOK_GLOB = request.data['cookbook']
        RECEIPE_GLOB = request.data['receipe']
        serializer=ReceipeCookbookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('receipe-cookbook-list')
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


class ReceipeCookbookSerializer(serializers.Serializer):

    pk=serializers.IntegerField(read_only=True)
    rate=serializers.IntegerField()
    make_date=serializers.DateField()
    receipe = serializers.PrimaryKeyRelatedField(read_only=True)
    cookbook = serializers.PrimaryKeyRelatedField(read_only=True)

    def create(self, validated_data):
        print(self)
        validated_data['cookbook'] = COOKBOOK_GLOB
        validated_data['receipe'] = RECEIPE_GLOB
        

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
    receipecookbook = ReceipeCookbookSerializer(many=True, read_only=True)
    
    def create(self, validated_data):
        validated_data['creation_date'] = datetime.now()
        return Cookbook.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.rate_cookbook = validated_data.get('rate_cookbook', instance.rate_cookbook)
        instance.save()
        return instance
