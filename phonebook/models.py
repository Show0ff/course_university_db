from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=255, null=False)


class Position(models.Model):
    title = models.CharField(max_length=255, null=False)


class PhoneType(models.Model):
    type = models.CharField(max_length=255, null=False)


class Room(models.Model):
    room_number = models.CharField(max_length=255, null=False)


class Phone(models.Model):
    number = models.CharField(max_length=255, null=False)
    phone_type = models.ForeignKey(PhoneType, on_delete=models.CASCADE)


class Subscriber(models.Model):
    name = models.CharField(max_length=255, null=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    phone = models.OneToOneField(Phone, on_delete=models.CASCADE)
