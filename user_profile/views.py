from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_exempt,csrf_protect
from django.contrib.auth.models import User
from django.contrib import auth
from .serializers import UserProfileSerializer
from .models import UserProfile


class GetUserProfileView(APIView):
    def get(self,request,format=None):
        try:
            user=self.request.user
            user=User.objects.get(id=user.id)
            user_profile=UserProfile.objects.get(user=user)
            user_profile=UserProfileSerializer(user_profile)
            return Response({'profile':user_profile.data,'username':str(user.username)})
        except:
            return Response({'error':'something went wrong when retreiving profile'})

class UpdateUserProfileView(APIView):
    def put(self,request,format=None):
        try:
            user=self.request.user
            username=user.username
            user=User.objects.get(id=user.id)
            
            data=self.request.data
            first_name=data['first_name']
            last_name=data['last_name']
            phone=data['phone']
            city=data['city']
            user =User.objects.get(id=user.id)
            UserProfile.objects.filter(user=user).update(first_name=first_name,last_name=last_name,phone=phone,city=city)
            user_profile=UserProfile.objects.get(user=user)
            user_profile=UserProfileSerializer(user_profile)
            return Response({'profile':user_profile.data,'username':str(username)})
        except:
            return Response({'error':'something went wrong when retreiving profile'})
        
    
