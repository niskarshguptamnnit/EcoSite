
from django.contrib import admin
from django.urls import path
from file1 import views
urlpatterns = [
    path("",views.home,name='home'),
    path("quiz",views.quiz,name='quiz'),
    path("contest",views.contest,name='contest'),
    path("issues",views.issues,name='issus'),
    path("sustain",views.sustain,name='sust'),
    path("effects",views.effects,name='eff'),
    path("disaster",views.disaster,name='disaster'),
    path("shop",views.shop,name='shop'),
    path("form",views.form,name='form'),

]
