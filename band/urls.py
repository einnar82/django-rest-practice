from django.urls import path
from band import views

urlpatterns = [
    path('band/', views.BandList.as_view()),
    path('band/<int:pk>/', views.BandDetail.as_view()),
]
