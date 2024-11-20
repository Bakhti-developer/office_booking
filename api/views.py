from rest_framework import viewsets, filters
from .models import Office, Room, Booking
from .serializers import OfficeSerializer, RoomSerializer, BookingSerializer

class OfficeViewSet(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['location']


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['office__name', 'capacity']


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user_id', 'room__name', 'start_time', 'end_time']
