from django.urls import path
from main import views


urlpatterns = [
    path('setNum/', views.SetCatInDb.as_view()),
    path('getParkings/', views.getAParking.as_view()),
    path('getParkomats/', views.getAParkomat.as_view()),
    path('getCarData/', views.sendCarInfo.as_view()),
    path('placeInfo/', views.PlaceInfo.as_view()),
    path('ppp/',views.PPP.as_view())

]
