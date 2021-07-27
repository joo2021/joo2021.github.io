"""bday2021p URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import bday2021.views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bday2021.views.first, name="first"),
    path('index/', bday2021.views.index, name="index"),
    path('party/', bday2021.views.party, name="party"),
    path('about/', bday2021.views.about, name="about"),
    path('cel/', bday2021.views.cel, name="cel"),
    path('letter/', bday2021.views.letter, name="letter"),
    path('food/', bday2021.views.food, name="food"),
    path('blog/create/', bday2021.views.create, name='create'),
]
