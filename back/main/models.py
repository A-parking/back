from django.db import models


class BigParking(models.Model):
    number = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Big_Parking'
        verbose_name_plural = 'Big_Parkings'

    def __str__(self):
        return f'BigParking: {self.number}'


class Parking(models.Model):
    number = models.IntegerField(default=0)
    address = models.CharField(max_length=255)
    current_places = models.IntegerField(default=0)
    busy_places = models.IntegerField(default=0)
    cost = models.FloatField(default=100)
    work_time = models.CharField(max_length=255,default='8:00-19:00')
    big_parking = models.ForeignKey(BigParking, on_delete=models.CASCADE, related_name='big_parking')
    x1 = models.FloatField(default=0)
    y1 = models.FloatField(default=0)
    x2 = models.FloatField(default=0)
    y2 = models.FloatField(default=0)
    x3 = models.FloatField(default=0)
    y3 = models.FloatField(default=0)
    x4 = models.FloatField(default=0)
    y4 = models.FloatField(default=0)

    class Meta:
        verbose_name = 'Parking'
        verbose_name_plural = 'Parkings'

    def __str__(self):
        return f'Parking: number--{self.number} Address--{self.address} Count---{self.current_places}'


class Parkomat(models.Model):
    number = models.IntegerField(default=0)
    address = models.CharField(max_length=255)
    x = models.FloatField(default=0)
    y = models.FloatField(default=0)

    def __str__(self):
        return f'Parkomat: {self.number}-{self.address}'


class Car(models.Model):
    time_count = models.TimeField(auto_now_add=True)
    state_number = models.CharField(max_length=255)
    parking_place = models.ForeignKey(Parking, on_delete=models.CASCADE, related_name='parking_place')

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return f'Parking: {self.state_number}-{self.time_count}'
