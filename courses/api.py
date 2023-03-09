from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import CourseSerializer, ModuleSerializer
from .models import Course, Module

@api_view(["GET", "POST"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def rest_course(request):
    if request.method == "GET":
        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        data = request.data
        ser = CourseSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        
@api_view(["GET", "POST"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def rest_module(request):
    if request.method == "GET":
        queryset = Module.objects.all()
        serializer = ModuleSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        data = request.data
        ser = Module(data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)