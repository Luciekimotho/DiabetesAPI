from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Profile
from .models import Readings
from .serializers import ProfileSerializer

# Create your views here.
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the diabetes index.")

class ProfileList(APIView):
    def get(self, request):
        users = Profile.objects.all()
        userserializer = ProfileSerializer(users,many=True)
        return Response(userserializer.data)


    def post(self):
        pass
