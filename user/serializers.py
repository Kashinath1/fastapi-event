
from rest_framework import serializers
from user.models import user
from event.models import event,EventReservation,Reservation

class userSerailizer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('email','first_name','last_name','profile_pic','is_verified','auth_provided','is_active')


class eventSerializer(serializers.ModelSerializer):
    class Meta:
        model = event
        fields =('id','everyName','price')

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields =('id','guestid','checkin','chekout','iscreated','isupdated')

class EventReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventReservation
        fields = ('id','userid','eventid','ReservationId','numberofguest','totalprice','purposeDescribe') 