from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('', ),
    path('',views.showHomePage, name='homePage' ),
    path('add/',views.addWords, name='addWords' ),
    path('show/',views.showWords, name='showWords' ),
    path('search/',views.searchWords, name='searchWords' ),
    path('show/detail/<int:WordId>/',views.wordsDetail, name='wordsDetail' ),

]