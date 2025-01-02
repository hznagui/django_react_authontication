from django.shortcuts import render

#heaeder that was adding 
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerialazers, NoteSerialazers
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

# Create your views here.
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerialazers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author = user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author = self.request.user)
        else:
            print(serializer.errors)


class NoteDelete(generics.DestroyAPIView):
    serializer_class=NoteSerialazers
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author = user)


        

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialazers
    permission_classes = [AllowAny]
