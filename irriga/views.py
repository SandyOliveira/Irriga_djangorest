from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Usuario
from .serializers import UsuarioSerializer
from  django.shortcuts import  get_object_or_404

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import CreateModelMixin
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView


class UsuarioView(ListModelMixin, GenericAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)

class UsuarioView(CreateAPIView, ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()



class UsuarioView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)




class UsuarioView(CreateAPIView, ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()

class UsuarioView(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()

class SingleUsuarioView(RetrieveAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class SingleUsuarioView(RetrieveUpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer