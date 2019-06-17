from django.contrib.auth.models import User
from rest_framework import mixins, generics, permissions, renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly

@api_view(['GET'])
def api_root(request, format=None):
	return Response({
		'users': reverse('user-list', request=request, format=format),
		'snippets': reverse('snippet-list', request=request, format=format)
		})


class SnippetHighlight(generics.GenericAPIView):
	queryset = Snippet.objects.all()
	renderer_class = (renderers.StaticHTMLRenderer,)

	def get(self, request, *args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)

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