from .serializers import TodoSerializer
from django.shortcuts import render
from .models import Todo
from rest_framework import viewsets
# Create your views here.


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()