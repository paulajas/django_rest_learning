from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .serializers import CookbookSerializer, ReceipeCookbookNewSerializer, ReceipeSerializer, ReceipeCookbookSerializer
from .models import Receipe, Cookbook, ReceipeCookbook

# Create your views here.

class Mainpage(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        return Response(status=status.HTTP_200_OK)


class CookbookAV(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cookbook.html'
    
    def get(self, request):
        try:
            cookbook=Cookbook.objects.all()
            serializer = CookbookSerializer(cookbook,  many=True,context={'request': request})
            return Response({'items':serializer.data},status=status.HTTP_200_OK)
        except Cookbook.DoesNotExist:
            return Response({"error: Nothing to show"}, status=status.HTTP_404_NOT_FOUND)

    def post(self,request):
        serializer=CookbookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        pass
    def put(self,request,pk):
        cookbook = Cookbook.objects.get(pk=pk)
        serializer = CookbookSerializer(cookbook, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        cookbook = Cookbook.objects.get(pk=pk)
        cookbook.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

class CookbookNewAV(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cookbook_new.html'
    def get(self, request):
        return Response({"error": "Nothing to show"}, status=status.HTTP_200_OK)

    def post(self,request):
        serializer=CookbookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('cookbook-list')
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

class ReceipeAV(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'receipe.html'
    def get(self, request):
        try:
            receipe=Receipe.objects.all()
            serializer = ReceipeSerializer(receipe, many=True,context={'request': request})
            return Response({'receipies': serializer.data}, status=status.HTTP_200_OK)
        except Receipe.DoesNotExist:
            return Response({"error: Nothing to show"}, status=status.HTTP_404_NOT_FOUND)

    def post(self,request):
        serializer=ReceipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_200_ACCEPTED)

    def put(self,request,pk):
        receipe = Receipe.objects.get(pk=pk)
        serializer = ReceipeSerializer(receipe, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        receipe = Receipe.objects.get(pk=pk)
        receipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReceipeNewAV(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'receipe_new.html'
    def get(self, request):
        return Response({"error": "Nothing to show"}, status=status.HTTP_200_OK)

    def post(self,request):
        serializer=ReceipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('receipe-list')
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

class ReceipeCookbookAV(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cr.html'
    def get(self, request):
        try:
            receipe=ReceipeCookbook.objects.all()
            serializer = ReceipeCookbookSerializer(receipe, many=True,context={'request': request})
            return Response({'items':serializer.data}, status=status.HTTP_200_OK)
        except ReceipeCookbook.DoesNotExist:
            return Response({"error: Nothing to show"}, status=status.HTTP_404_NOT_FOUND)

    def post(self,request):
        serializer=ReceipeCookbookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        pass
    def put(self,request,pk):
        receipe = ReceipeCookbook.objects.get(pk=pk)
        serializer = ReceipeCookbookSerializer(receipe, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        receipe = ReceipeCookbook.objects.get(pk=pk)
        receipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CookbookDetailAV(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cookbook-detail.html'

    def get(self, request, pk):
        cookbook = get_object_or_404(Cookbook, pk=pk)
        serializer = CookbookSerializer(cookbook)
        return Response({'serializer': serializer, 'cookbook': cookbook})
    
    def put(self, request, pk):
        country = Cookbook.objects.get(pk=pk)
        serializer = CookbookSerializer(country, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cookbook = Cookbook.objects.get(pk=pk)
        cookbook.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

    def post(self, request, pk):
        if request._full_data['_METHOD'] == 'PUT':
            self.put(request,pk)
        elif request._full_data['_METHOD'] == 'DELETE':
            self.delete(request, pk)
        else: 
            cookbook = get_object_or_404(Cookbook, pk=pk)
            serializer = CookbookSerializer(cookbook, data=request.data)
            if not serializer.is_valid():
                return Response({'serializer': serializer, 'cookbook': cookbook})
            serializer.save()
        return redirect('cookbook-list')


class ReceipeDetailAV(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'receipe-detail.html'


    def get(self, request, pk):
        profile = get_object_or_404(Receipe, pk=pk)
        serializer = ReceipeSerializer(profile)
        return Response({'serializer': serializer, 'profile': profile})

    def put(self, request, pk):
        country = Receipe.objects.get(pk=pk)
        serializer = ReceipeSerializer(country, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'item':serializer.data}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        country = Receipe.objects.get(pk=pk)
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

    def post(self, request, pk):
        if request._full_data['_METHOD'] == 'PUT':
            self.put(request,pk)
        elif request._full_data['_METHOD'] == 'DELETE':
            self.delete(request, pk)
        else: 
            profile = get_object_or_404(Receipe, pk=pk)
            serializer = ReceipeSerializer(profile, data=request.data)
            if not serializer.is_valid():
                return Response({'serializer': serializer, 'profile': profile})
            serializer.save()
        return redirect('receipe-list')


class ReceipeCookbookDetailAV(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cr-details.html'

    def get(self, request, pk):
        item = ReceipeCookbook.objects.get(pk=pk)
        serializer = ReceipeCookbookSerializer(item)
        return Response({'serializer':serializer, 'item': item})

    def post(self, request, pk):
        item = ReceipeCookbook.objects.get(pk=pk)
        serializer = ReceipeCookbookSerializer(item, data=request.data, context={'request': request})
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'profile': item})
        serializer.save()
        return redirect('receipe-cookbook-list')
    
    def put(self, request, pk):
        country = ReceipeCookbook.objects.get(pk=pk)
        serializer = ReceipeCookbookSerializer(country, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        country = ReceipeCookbook.objects.get(pk=pk)
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReceipeCookbookNewAV(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cr-new.html'
    def get(self, request):
        return Response({"error": "Nothing to show"}, status=status.HTTP_200_OK)

    def post(self,request):
        serializer=ReceipeCookbookSerializer(data=request.data, context={'receip': request.data['receipe'], 'cook':request.data['cookbook']})
        if serializer.is_valid():
            serializer.save()
            return redirect('receipe-cookbook-list')
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)