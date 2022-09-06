from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women
from .serializers import WomenSerializer


class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer




# возвращает список записей по GET запросу
# добавляет новую запись по POST запросу
# class WomenAPIList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# # изменение по PUT или PATCH запросу
# class WomenAPIUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()      #возвращает одно значение
#     serializer_class = WomenSerializer
#
#
# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()      #возвращает одно значение
#     serializer_class = WomenSerializer
