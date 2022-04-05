from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from backend.models import  *
from backend.serializers import *
# Create your views here.




class todoListView(generics.ListCreateAPIView):

    def get(self, request, format=None):
        do = todo.objects.all()
        serializer = todoSerializer(do, many= True)
        return Response(serializer.data)

    def post(self, request):
        serializer = todoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class todoUpdateView(generics.UpdateAPIView):

    def put(self, request, pk, format=None):
        do = todo.objects.get(pk=pk)
        serializer = todoSerializer(do, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class todoDeleteView(generics.DestroyAPIView):

    serializer_class = todoSerializer
    queryset = todo.objects.all()