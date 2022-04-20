# from django.shortcuts import render
# from rest_framework.response import Response
# from user.serializers import userSerailizer
# from rest_framework.views import APIView

# # Create your views here.
# class userView(APIView):
#     def get(self,request):
#         serializer = userSerailizer()
#         return Response(serializer.data)
    
# import viewsets
from rest_framework import viewsets
  
# import local data
from .serializers import userSerailizer
from .models import user
  
# create a viewset
class userViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = user.objects.all()
      
    # specify serializer to be used
    serializer_class = userSerailizer