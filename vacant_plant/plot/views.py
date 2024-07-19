from django.shortcuts import render
from .models import PlotDetail
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import PlotDetailSerializer
from rest_framework.response import Response
from rest_framework import status


class PlotDetailView(APIView):
    permission_classes = [AllowAny,]
    
    def post(self, request):
        serializer = PlotDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)