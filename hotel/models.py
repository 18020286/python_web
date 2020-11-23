from django.db import models


class Room(models.Model):
    room_type = models.CharField(max_length=200)
    price = models.PositiveSmallIntegerField(default=0)
    num_room = models.PositiveSmallIntegerField(default=0)
    description = models.TextField()
    picture = models.ImageField(upload_to='room_pictures')

    def __str__(self):
        return self.room_type


class HotelInfo(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
