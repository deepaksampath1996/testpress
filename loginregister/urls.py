from django.urls import path
from . import views

urlpatterns = [
    path('',views.login, name='login'),
    path('login/register/',views.register,name='register'),
    path('register/',views.register, name='register'),
    path('logout/',views.logout,name='logout'),
    # path('home/',views.home, name='home'),
    path('test/',views.test,name='test'),
    path('result/',views.result, name='result'),
    path('start/',views.start,name='start'),
    path('api/',views.QuizApiView.as_view()),
]