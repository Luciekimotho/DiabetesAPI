from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Profile
from .models import Readings
from .serializers import ProfileSerializer, ReadingsSerializer, UserReadingSerializer
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


    def post(self):
        pass

class ProfileDetail(APIView):
    def get_object(self, pk):
            return Profile.objects.get(pk=pk)
        

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = ProfileSerializer(user)
        return Response(serializer.data)


class ReadingsList(APIView):
    def get(self, request):
        readings = Readings.objects.all()
        readingsSerializer = ReadingsSerializer(readings,many=True)
        return Response(readingsSerializer.data)


    def post(self):
        pass

class ReadingDetail(APIView):
    def get_object(self, pk):
            return Readings.objects.get(pk=pk)
               
    def get(self, request, pk, format=None):
        reading = self.get_object(pk)
        readingSerializer = ReadingsSerializer(reading)
        return Response(readingSerializer.data)

class UserReadingsList(APIView):
    def get(self, request):
        userreadings = Profile.objects.all()
        userreadingsSerializer = UserReadingSerializer(userreadings,many=True)
        return Response(userreadingsSerializer.data)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = UserReadingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class UserReading(APIView):
    def get_object(self, pk):
         return Profile.objects.get(pk=pk)

    def get(self, request, pk, format=None):
        reading = self.get_object(pk)
        userreadingSerializer = UserReadingSerializer(reading)
        return Response(userreadingSerializer.data)
