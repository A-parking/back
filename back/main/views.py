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
        if findParking(locationX, locationY):
            myPark = findParking(locationX, locationY)
            if checkNum(num):
                Car.objects.create(parking_place=myPark, state_number=num)
                myPark.busy_places += 1
                myPark.save()
                return Response(f'Car Detected', status=status.HTTP_200_OK)
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


class sendCarInfo(APIView):
    def get(self, request):
        num = request.data.pop('state_number')
        car = Car.objects.get(state_number=num)
        serializer = CarSerializer(car)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self,request):
        pk = request.data.pop('id')
        car = Car.objects.get(id=pk)
        park = Parking.objects.get(id=car.parking_place.id)
        park.busy_places -= 1
        park.save()
        car.delete()
        return Response(f'Car deleted!!', status=status.HTTP_202_ACCEPTED)


class PlaceInfo(APIView):
    def get(self, request):
        cnt = 0
        parks = Parking.objects.all()
        for park in parks:
            for car in park.parking_place.all():
                cnt+=1
            print(cnt)
            print(park)
            serializer = ParkingSerializer(park)
            cnt = 0
            return Response(serializer.data)

def carInfo(state_number):
    cars = Car.objects.all()
    for car in cars:
        if(car.state_number == state_number):
            return True
    return False


def findParking(x, y):
    # 0.000012205128205 - 1 metr
    parkings = Parking.objects.all()
    point = Point(x,y)
    for parking in parkings:
        polygon = Polygon([(parking.x1, parking.y1), (parking.x2, parking.y2), (parking.x3, parking.y3), (parking.x3, parking.y3)])

        myarg = 5 * 0.000012205128205

        point1 = Point(x, y + myarg)
        point2 = Point(x + myarg, y)
        point3 = Point(x, y - myarg)
        point4 = Point(x - myarg, y)

        if polygon.contains(point1) == True:
            return parking
        if polygon.contains(point2) == True:
            return parking
        if polygon.contains(point3) == True:
            return parking
        if polygon.contains(point4) == True:
            return parking
        return False
#
#


