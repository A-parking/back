from django.urls import path
from main import views


urlpatterns = [
    path('setNum/', views.SetCatInDb.as_view()),
    path('getParkings/', views.getAParking.as_view()),
    path('getParkomat/', views.getAParkomat.as_view())

]