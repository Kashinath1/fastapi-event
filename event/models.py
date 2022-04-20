from django.db import models
from user.models import user

# Create your models here.


class event(models.Model):
    everyName = models .CharField(max_length=255,blank=True,null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.everyName


class Reservation(models.Model):
    guestid = models.IntegerField()
    checkin = models.DateTimeField(auto_now=False, auto_now_add=False)
    chekout = models.DateTimeField(auto_now=False, auto_now_add=False)
    iscreated = models.DateField(blank=True,null=True)
    isupdated = models.DateField(blank=True,null=True)


class EventReservation(models.Model):
    userid = models.ForeignKey(user, on_delete=models.CASCADE)
    eventid = models.ForeignKey(event, on_delete=models.CASCADE)
    ReservationId = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    numberofguest = models.IntegerField()
    totalprice = models .CharField(max_length=255)
    purposeDescribe = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.purposeDescribe
