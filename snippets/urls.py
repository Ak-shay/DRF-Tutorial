from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from . import views


#Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

schema_view = get_schema_view(title='Pastebin API')

#The API URLS are now determined automatically by the router.
urlpatterns = [
	path('', include(router.urls)),
	path('schema/', schema_view),
]