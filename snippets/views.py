from django.contrib.auth.models import User
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly

class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class SnippetList(generics.ListCreateAPIView):
	"""List all code snippets, or create a new snippet"""

	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_class = (permissions.IsAuthenticatedOrReadOnly, )

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):	
	"""Retrieve, update or delete a code snippet."""
	
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_class = (permissions.IsAuthenticatedOrReadOnly,
						IsOwnerOrReadOnly,)