from rest_framework import serializers
from event.models import event,  EventReservation, Reservation


class eventSerializer(serializers.ModelSerializer):
    class Meta:
        model = event
        fields = ('id', 'everyName',  'price')


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('id', 'guestid', 'checkin',
                  'chekout', 'iscreated', 'isupdated')


class EventReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventReservation
        fields = ('id', 'userid', 'eventid', 'ReservationId', 'numberofguest',
                  'totalprice', 'purposeDescribe')
