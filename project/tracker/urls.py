from django.urls import path
from . import views

urlpatterns = [
        path('sightings/', views.sightings),
        path('map/',views.map),
        path('sightings/<str:unique_id>/', views.update),
<<<<<<< HEAD
]
=======
        path('sightings/add',views.create),
        path('sightings/stats',views.view_stats),
        
      ]
>>>>>>> 6adfa0b1aaf26fad6fe7a25368b7e0d32f7e3782
