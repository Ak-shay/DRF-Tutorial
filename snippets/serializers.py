from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
	"""Class defines the fields that get serialized/deserialized"""
	#serializer.ModelSerializer is simple implementation for create() and update() 
	
	class Meta:
		model = Snippet
		fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
