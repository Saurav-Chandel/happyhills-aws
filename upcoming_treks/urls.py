from django.contrib import admin
from django.urls import path,include
from upcoming_treks import views

app_name = "upcoming_trips"

urlpatterns = [
    # Upcoming_Treks
    path("upcoming_treks/api/v1/list/", views.GetAllUpcomingTreks.as_view()),
    path("upcoming_treks/api/v1/create/", views.CreateUpcomingTreks.as_view()),
    path("upcoming_treks/api/v1/get/<int:pk>/", views.GetUpcomingTreks.as_view()),
    path("upcoming_treks/api/v1/update/<int:pk>/", views.UpdateUpcomingTreks.as_view()),
    path("upcoming_treks/api/v1/delete/<int:pk>/", views.DeleteUpcomingTreks.as_view()),
    # Upcoming_Road_Trips
    path("upcoming_road_trips/api/v1/list/", views.GetAllUpcomingRoadTrips.as_view()),
    path("upcoming_road_trips/api/v1/create/", views.CreateUpcomingRoadTrips.as_view()),
    path("upcoming_road_trips/api/v1/get/<int:pk>/", views.GetUpcomingRoadTrips.as_view()),
    path("upcoming_road_trips/api/v1/update/<int:pk>/", views.UpdateUpcomingRoadTrips.as_view()),
    path("upcoming_road_trips/api/v1/delete/<int:pk>/", views.DeleteUpcomingRoadTrips.as_view()),
]