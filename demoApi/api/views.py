from django.shortcuts import render
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .models import profile
from .serializers import profileSerializer
from rest_framework import viewsets

# Create your views here.

# --------------- get and post api ----------------

# class profileView(APIView):
#     def post(self, request):
#         serializer = profileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def get(self,request):
#         data = profile.objects.all()
#         serializers = profileSerializer(data, many=True)
#         return Response(serializers.data, status=200)

# -------------------- viewset -----------------

class profileViewSet(viewsets.ViewSet):

    def post(self, request):
        serializer = profileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        p = profile.objects.all()
        serializer = profileSerializer(p, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        id = pk
        print("🚀 ~ file: views.py ~ line 47 ~ id", id)
        if pk is not None:
          p = profile.objects.get(id=pk)
          print("🚀 ~ file: views.py ~ line 25 ~ P", p)
          serializer = profileSerializer(p)
          return Response(serializer.data)

    def update(self, request, pk):
        id = pk
        print("🚀 ~ file: views.py ~ line 56 ~ id", id)
        p = profile.objects.get(id=pk)
        serializer = profileSerializer(p, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Data updated'})
        return Response({'message':'Data created'}, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        id = pk
        p = profile.objects.get(id=pk)
        serializer = profileSerializer(p, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Data updated'})
        return Response(serializer.errors)
    
    def destroy(self, request, pk):
        id = pk 
        p = profile.objects.get(id=pk)
        p.delete()
        return Response({'msg':'data deleted'})