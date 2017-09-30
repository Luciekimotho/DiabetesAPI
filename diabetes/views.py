from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Profile
from .models import Reading
from .serializers import ProfileSerializer, ReadingSerializer, UserInlineSerializer
from rest_framework.parsers import JSONParser

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the diabetes index.")

class ProfileList(APIView):
    def get(self, request):
        users = Profile.objects.all()
        userserializer = ProfileSerializer(users,many=True)
        return Response(userserializer.data)


    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileDetail(APIView):
    def get_object(self, pk):
            return Profile.objects.get(pk=pk)
        

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = ProfileSerializer(user)
        return Response(serializer.data)


class ReadingsList(APIView):
    def get(self, request):
        readings = Reading.objects.all()
        readingsSerializer = ReadingSerializer(readings,many=True)
        return Response(readingsSerializer.data)


    def post(self):
        pass

class ReadingDetail(APIView):
    def get_object(self, pk):
            return Reading.objects.get(pk=pk)
               
    def get(self, request, pk, format=None):
        reading = self.get_object(pk)
        readingSerializer = ReadingSerializer(reading)
        return Response(readingSerializer.data)

class UserReadingsList(APIView):
    def get(self, request):
        userreadings = Profile.objects.all()
        userreadingsSerializer = UserInlineSerializer(userreadings,many=True)
        return Response(userreadingsSerializer.data)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = UserInlineSerializer(data=data)
        if serializer.is_valid():
            serializer.save()   
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class UserReading(APIView):
    def get_object(self, pk):
         return Profile.objects.get(pk=pk)

    def get(self, request, pk, format=None):
        reading = self.get_object(pk)
        userreadingSerializer = UserInlineSerializer(reading)
        return Response(userreadingSerializer.data)
