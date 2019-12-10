from django.urls import path
from . import views

urlpatterns = [
        path('',views.beauty),
        path('sightings/', views.sightings),
        path('map/',views.map),
        path('sightings/add/',views.create),
        path('sightings/stats/',views.view_stats),
        path('sightings/<str:unique_id>/', views.update),
      ]
