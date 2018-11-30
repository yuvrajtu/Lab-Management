"""LabApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path,include
from App import views


urlpatterns = [
    path('',views.index,name="index"),
    path('admin/', admin.site.urls),
    path('login/', include('App.urls')),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('dashboard/<int:pk>/',views.DeleteComplains.as_view(),name="DeleteComplains"),
    path('dashboard/create', views.ComplainsCreateView.as_view(), name='ComplainCreate'),
    path('Notice/',views.NoticeBoard.as_view(),name="Notice"),
    path('Notice/create', views.NoticeCreateView.as_view(), name='NoticeCreate'),
    path('Attendent/',views.AttendentDetails.as_view(),name="Attendent"),
    path('Faculty/',views.FacultyDetails.as_view(),name="Faculty"),
    path('TimeTable/',views.TimeTable.as_view(),name="TimeTable"),
    path('Attendent_dashboard/<int:pk>/',views.StatusUpdate.as_view(),name="StatusUpdate"),
    path('dashboard_Att/',views.Dash.as_view(),name="dashboard_Att"),

]
