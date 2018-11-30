from django.conf.urls import url
from django.urls import path,include
from App import views

app_name='App'

urlpatterns=[
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),

]