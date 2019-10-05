from rest_framework import serializers

from main.models import BigParking, Parkomat, Parking, Car


class BigParkingSerializer(serializers.ModelSerializer):
    number = serializers.IntegerField(required=True)

    class Meta:
        model = BigParking
        fields = ['id', 'number', ]


class ParkingSerializer(serializers.ModelSerializer):
    big_parking = BigParkingSerializer

    class Meta:
        model = Parking
        fields = ['id', 'number', 'address', 'cost', 'current_places', 'big_parking', 'work_time', 'x0', 'y0', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3' ]


class ParkomatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parkomat
        fields = ['id', 'number', 'address', 'x', 'y' ]


class CarSerializer(serializers.ModelSerializer):
    parking_place = ParkingSerializer

    class Meta:
        model = Car
        fields = ['id', 'state_number', 'time_count', 'parking_place']
