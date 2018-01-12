from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Profile, Doctor, Caregiver, Reading, Reminder
from .serializers import ProfileSerializer, ReadingSerializer, UserInlineSerializer, DoctorSerializer, CaregiverSerializer, ReminderSerializer
from rest_framework.parsers import JSONParser
from rest_framework import generics
from rest_framework.decorators import api_view
from django.utils import timezone

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'diabetes/index.html')

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

class DoctorList(APIView):
    def get(self, request):
        doctorlist = Doctor.objects.all()
        doctorSerializer = DoctorSerializer(doctorlist,many=True)
        return Response(doctorSerializer.data)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = DoctorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()   
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class DoctorProfile(APIView):
    def get_object(self, pk):
         return Doctor.objects.get(pk=pk)

    def get(self, request, pk, format=None):
        doctor = self.get_object(pk)
        doctorSerializer = DoctorSerializer(doctor)
        return Response(doctorSerializer.data)

class CaregiverList(APIView):
    def get(self, request):
        caregiverlist = Caregiver.objects.all()
        caregiverSerializer = CaregiverSerializer(caregiverlist,many=True)
        return Response(caregiverSerializer.data)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = CaregiverSerializer(data=data)
        if serializer.is_valid():
            serializer.save()   
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class CaregiverProfile(APIView):
    def get_object(self, pk):
         return Caregiver.objects.get(pk=pk)

    def get(self, request, pk, format=None):
        caregiver = self.get_object(pk)
        caregiverSerializer = CaregiverSerializer(caregiver)
        return Response(caregiverSerializer.data)

def caregiver_list(request):
        caregivers =	Caregiver.objects.all
        return render(request, 'diabetes/caregiver.html', {'caregivers' : caregivers})

class ReminderListAPIView(generics.ListCreateAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

    def get_queryset(self):
        user = self.request.user
        return Reminder.objects.all()

    def perform_create(self, serializer):   
        serializer.save(user=self.request.user)

    
        
    # def get(self, request):
    #     reminderlist = Reminder.objects.all()
    #     reminderSerializer = ReminderSerializer(reminderlist,many=True)
    #     return Response(reminderSerializer.data)

    # def post(self, request):
    #     data = JSONParser().parse(request)
    #     serializer = ReminderSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()   
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)

class ReadingCreateView(generics.CreateAPIView):
    serializer_class = ReadingSerializer

    @api_view(["POST"])
    def new_reading(request):
        serializer = ReadingSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "New reading"}) 
        else:
            data = {
            "error": True,
            "errors": serializer.errors,          
            }
            return Response(data)

