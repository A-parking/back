from rest_framework import serializers

from main.models import BigParking, Parkomat, Parking, Car


class BigParkingSerializer(serializers.ModelSerializer):
    number = serializers.IntegerField(required=True)

    class Meta:
        model = BigParking
        fields = ['id', 'number', ]


class ParkingSerializer(serializers.ModelSerializer):
    big_parking = BigParkingSerializer(required=False)
    # number = serializers.IntegerField(required=False)
    # address = serializers.CharField(required=False)
    # cost = serializers.FloatField(required=False)
    # current_places = serializers.IntegerField(required=False)

    class Meta:
        model = Parking
        fields = ['id', 'number', 'address', 'cost', 'current_places','busy_places', 'big_parking', 'work_time',  'x1', 'y1', 'x2', 'y2', 'x3', 'y3','x4', 'y4',]


class ParkomatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parkomat
        fields = ['id', 'number', 'address', 'x', 'y' ]


class CarSerializer(serializers.ModelSerializer):
    parking_place = ParkingSerializer(required=False)

    class Meta:
        model = Car
        fields = ['id', 'state_number', 'time_count', 'parking_place']
