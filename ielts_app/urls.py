from django.urls import path,include
from . import views

urlpatterns = [
    path('v1/<int:pk>/', views.BookView.as_view()),
]