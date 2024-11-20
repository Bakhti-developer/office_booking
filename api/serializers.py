from rest_framework import serializers
from .models import Office, Room, Booking

class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, data):
        # Check for overlapping bookings
        room = data['room']
        start_time = data['start_time']
        end_time = data['end_time']
        overlapping_bookings = Booking.objects.filter(
            room=room,
            start_time__lt=end_time,
            end_time__gt=start_time
        )
        if overlapping_bookings.exists():
            raise serializers.ValidationError("This room is already booked for the given time range.")
        return data
