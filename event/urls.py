from django.urls import include, path
# import routers
from rest_framework import routers

from user.views import userViewSet
  
# import everything from views
from .views import *

# define the router
router = routers.DefaultRouter()

router.register(r'event', eventViewSet, basename='event')
router.register(r'Reservation', ReservationViewset, basename= 'Reservation')
router.register(r'eventReservation', EventReservationViewSet, basename='EventReservation')
router.register(r'user', userViewSet, basename='user')


urlpatterns = [

]

urlpatterns += router.urls
