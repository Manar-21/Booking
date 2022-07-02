"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index.html', index),
    path('', index),
    path('index/index.html', index),
    path('index/Appointment.html', Appointment),
    path('index/Saturday.html', Saturday),
    path('index/Sunday.html', Sunday),
    path('index/Monday.html', Monday),
    path('index/Tuesday.html', Tuesday),
    path('index/Wednesday.html', Wednesday),
    path('index/Thursday.html', Thursday),
    path('index/Review.html', ReviewView),
    path('index/ApppintmentReviews.html', ApppintmentReviews),
    path('index/Login.html', admin.site.urls),
    path('index/contact.html', contact),
    path('index/Login_Report.html', login_report),
    path('index/report_index.html', report), 
    path('index/report_weekly.html', report_weekly),
    path('index/report_daily.html', report_daily),
    path('index/idSat.html', idSaturday),
    path('index/idSun.html', idSunday),
    path('index/idMon.html', idMonday),
    path('index/idTue.html', idTuesday),
    path('index/idWed.html', idWednesdayy),
    path('index/idThr.html', idThursday),
]
