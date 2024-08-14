from django.urls import path
from core.views import home, contact, sobre

urlpatterns = [
    path('', home),
    path('contato', contact),
    path('sobre', sobre),
]
