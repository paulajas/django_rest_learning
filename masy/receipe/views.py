from curses.ascii import US
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from receipe.models import Country, Picture
from .serializers import CountrySerializer, PictureSerializer

# from receipe.serializers import CookBookSerializer
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from receipe.models import CookBook
from rest_framework.views import APIView


class CountryAV(APIView):

    def get(self,request):
        country = Country.objects.all()
        serializer = CountrySerializer(country, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class CountryDetailAV(APIView):

    def get(rself, request, pk):
        country = Country.objects.get(pk=pk)
        serializer = CountrySerializer(country)
        return Response(serializer.data)
    
    def put(self, request, pk):
        country = Country.objects.get(pk=pk)
        serializer = CountrySerializer(country, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        country = Country.objects.get(pk=pk)
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
        

# Create your views here.
def register(response):
    form=RegisterForm()
    if response.method == "POST":
        form=RegisterForm(response.POST)
        if form.is_valid():
            form.save_form()
            return redirect("/receipe/")
        else:
            form = RegisterForm()
    return render(response, "receipe/register.html", {"form":form})


# function base views (FBV)
# @api_view(['GET', 'POST'])
# def country_list(request):
#     if request.method == 'GET':
#         countries = Country.objects.all()
#         serializer = CountrySerializer(countries, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = CountrySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET', 'PUT', 'DELETE'])
# def country_detail(request, pk):
#     if request.method == 'GET':
#         try:
#             country = Country.objects.get(pk=pk)
#         except Country.DoesNotExist:
#             # return Response(status=status.HTTP_404_NOT_FOUND)
#             return Response({'error': 'Country not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = CountrySerializer(country)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         country = Country.objects.get(pk=pk)
#         serializer = CountrySerializer(country, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         country = Country.objects.get(pk=pk)
#         country.delete()
#         return Response({'delete': 'Country succesfully deleted'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def picture_list(request):
    if request == 'GET':
        pictures = Picture.objects.all()
        serializer = PictureSerializer(pictures, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request == 'POST':
        serializer = PictureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def picture_detail(request, pk):
    if request == 'GET':
        try:
            picture = Picture.objects.get(pk=pk)
        except Picture.DoesNotExist:
            return Response({'error': 'Picture does not exist'}, status=status.HTTP_204_NO_CONTENT)
        serializer = PictureSerializer(picture)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request == 'PUT':
        picture = Picture.objects.get(pk=pk)
        serializer = PictureSerializer(picture, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({},status=status.HTTP_400_BAD_REQUEST)

    elif request == 'DELETE':
        instance = Picture.objects.get(pk=pk)
        instance.delete()
        return Response({'information': 'Object deleted'}, status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET',])
# def cookbook_list(request):
#     cookbooks = CookBook.objects.all().last()
#     serializer = CookBookSerializer(cookbooks)
#     return Response(serializer.data)
