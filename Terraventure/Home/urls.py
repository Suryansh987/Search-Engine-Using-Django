from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='Home'),
    path('query-search/', views.query_search, name="searching")
]
