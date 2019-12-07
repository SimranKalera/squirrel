from django.urls import path
from . import views

urlpatterns = [
        path('sightings', views.sightings),
        path('map',views.map),
        path('sightings/<str:unique_id>/', views.update),
        path('sightings/add',views.create),
        path('sightings/stats',views.view_stats),
        
      ]
