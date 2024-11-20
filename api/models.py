from django.db import models

class Office(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Room(models.Model):
    office = models.ForeignKey(Office, related_name='rooms', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    room = models.ForeignKey(Room, related_name='bookings', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user_id = models.IntegerField()

    def __str__(self):
        return f"Booking by User {self.user_id} in {self.room.name}"
