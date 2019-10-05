from django.contrib import admin

from main.models import BigParking, Parkomat, Parking, Car


@admin.register(BigParking)
class BigParkAdmin(admin.ModelAdmin):
    list_display = ['id','number', ]


@admin.register(Parking)
class ParkingAdmin(admin.ModelAdmin):
    list_display = ['id','number', 'address', 'cost', 'current_places',  ]


@admin.register(Parkomat)
class ParkomatAdmin(admin.ModelAdmin):
    list_display = ['id','number', 'address', ]


@admin.register(Car)
class CarkAdmin(admin.ModelAdmin):
    list_display = ['id','state_number', 'time_count', ]


