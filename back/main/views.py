from main.models import BigParking, Parking, Parkomat, Car
from main.serializers import BigParkingSerializer, ParkingSerializer, ParkomatSerializer, CarSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class SetCatInDb(APIView):

    def post(self, request):
        locationX = request.data.get('x')
        locationY = request.data.get('y')
        num = request.data.get('state_number')
        parking = Parking.objects.get(id=1)
        if checkNum(num):
            Car.objects.create(parking_place=parking, state_number=num)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(f'This state_number exist in DB')

    def get(self,request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)


def checkNum(num):
    car_numbers = Car.objects.all()
    flag = 0
    for car in car_numbers:
        if car.state_number == num:
            flag +=1
    if flag == 0:
        return True
    elif flag > 0:
        return False

# def findArea(x,y):
#     # TODO


class getAParking(APIView):
    def get(self,request):
        parkings = Parking.objects.all()
        serializer = ParkingSerializer(parkings, many=True)
        return Response(serializer.data)


class getAParkomat(APIView):
    def get(self,request):
        parkings = Parkomat.objects.all()
        serializer = ParkomatSerializer(parkings, many=True)
        return Response(serializer.data)