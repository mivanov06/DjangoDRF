from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women, Category
from .serializers import WomenSerializer


class WomenViewSet(viewsets.ModelViewSet):
    # queryset = Women.objects.all()
    serializer_class = WomenSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
            return Women.objects.all()[:3]

        return Women.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})




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
