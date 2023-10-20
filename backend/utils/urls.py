from django.urls import path
from . import views

urlpatterns = [
    path('api/search/<str:search_content>/', views.search, name='search')
]