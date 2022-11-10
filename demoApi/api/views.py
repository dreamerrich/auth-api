from django.shortcuts import render
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .models import profile
from .serializers import profileSerializer
from rest_framework import viewsets

# Create your views here.

# --------------- get and post api ----------------

class profileView(APIView):
    def post(self, request):
        serializer = profileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self,request):
        data = profile.objects.all()
        serializers = profileSerializer(data, many=True)
        return Response(serializers.data, status=200)

# -------------------- viewset -----------------

class profileViewset(viewsets.ViewSet):

    def post(self, request):
        pass