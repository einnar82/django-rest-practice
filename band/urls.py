from django.urls import path
from band import views

urlpatterns = [
    path('band', views.snippet_list),
    path('band/<int:pk>', views.snippet_detail),
]
