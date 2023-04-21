from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from user_profile.models import UserProfile
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_exempt,csrf_protect
from django.contrib.auth.models import User
from django.contrib import auth
from .serializers import UserSerializer
# Create your views here.

@method_decorator(csrf_protect,name="dispatch")
class checkAuthenticated(APIView):
    def get(self,request,format=None):
        try:
            isAuthenticated=User.is_authenticated
            if isAuthenticated:
                return Response({'isAuthenticated':'success'})
            else:
                return Response({'isAuthenticated':'error'})
        except:
            return Response({'error':"something wh=ent wrong while a=checking for the authentication"})


@method_decorator(csrf_protect,name="dispatch")
class SignupView(APIView):
    permission_classes=(permissions.AllowAny,)


    def post(self,request):
        data=self.request.data
        username=data['username']
        password=data['password']
        re_password=data['re_password']
        if password== re_password:
            try:
                if User.objects.filter(username=username).exists():
                    return Response({'error':'usrname already exists'})
                else:
                    if len(password)<6:
                        return Response({'error':'password less than 6'})
                    else:
                        user=User.objects.create_user(username=username,password=password)
                        user.save()
                        user_profile=UserProfile.objects.create(user=user,first_name='',last_name='',phone='',city='')
                        user_profile.save()
                        return Response({'success':'user created successfully'})
            except:
                return Response({'error':'something went wrong while creating the user'})
        else:
            return Response({'error':'passwords do not match'})   
                 
@method_decorator(ensure_csrf_cookie,name='dispatch')
class GetCSRFToken(APIView):
    permission_classes=(permissions.AllowAny,)
    def get(self,request,format=None):
        return Response({'success':'csrf cokkie set'})
    

@method_decorator(ensure_csrf_cookie,name='dispatch')
class LoginView(APIView):
    permission_classes=(permissions.AllowAny,)
    def post(self,request,format=None):
        data=self.request.data
        username=data['username']
        password=data['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return Response({'success':'User authenticated','username':username})
        else:
            return Response({'error':'Error authenticated'})
        
class LogoutView(APIView):
    def post(self,request,format=None):
        try:
            auth.logout(request)
            return Response({'success':'logout success'})
        except:
            return Response({'error':'Something went wrong when logging out'})
        

class DeleteView(APIView):
    def delete(self,request,format=None):
        user=self.request.user
        try:
            user=User.objects.filter(id=user.id).delete()

            return Response({'success':'User deleted successfully'})
        except:
            return Response({'error':'somethung went wrong when trying to delete user'})

class GetUsersView(APIView):
    permission_classes=(permissions.AllowAny,)

    def get(self,request,format=None):
        users=User.objects.all()
        users=UserSerializer(users,many=True)
        return Response(users.data)






