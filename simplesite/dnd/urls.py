"""simplesite URL Configuration

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

from .views import roll_dice, SpellView, get_spell, character, todo

urlpatterns = [
    path('roll/', roll_dice, name='roll'),
    path('spells/', SpellView.as_view(), name='spells'),
    path('spells/<int:spell_id>/', get_spell, name='spell'),
    path('character/', character, name='character'),
    path('todo/', todo, name='todo'),
]
