from django.urls import path,include
from .views import SignupView,GetCSRFToken,LoginView,LogoutView,DeleteView,GetUsersView

urlpatterns=[
    path('register/',SignupView.as_view()),
    path('csrf_cookie/',GetCSRFToken.as_view()),
    path('login/',LoginView.as_view()),
    path('logout/',LogoutView.as_view()),
    path('delete/',DeleteView.as_view()),
    path('logout/',LogoutView.as_view()),
    path('get_users/',GetUsersView.as_view()),
]