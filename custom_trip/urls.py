from django.contrib import admin
from django.urls import path,include
from custom_trip import views

app_name = "custom_trip"

urlpatterns = [
    
    # State
    path("state/api/v1/list/", views.GetAllState.as_view()),
    path("state/api/v1/create/", views.CreateState.as_view()),
    path("state/api/v1/get/<int:pk>/", views.GetState.as_view()),
    path("state/api/v1/update/<int:pk>/", views.UpdateState.as_view()),
    path("state/api/v1/delete/<int:pk>/", views.DeleteState.as_view()),
    # District
    path("district/api/v1/list/", views.GetAllDistrict.as_view()),
    path("district/api/v1/create/", views.CreateDistrict.as_view()),
    path("district/api/v1/get/<int:pk>/", views.GetDistrict.as_view()),
    path("district/api/v1/update/<int:pk>/", views.UpdateDistrict.as_view()),
    path("district/api/v1/delete/<int:pk>/", views.DeleteDistrict.as_view()),
    # Destination
    path("destination/api/v1/list/", views.GetAllDestination.as_view()),
    path("destination/api/v1/create/", views.CreateDestination.as_view()),
    path("destination/api/v1/get/<int:pk>/", views.GetDestination.as_view()),
    path("destination/api/v1/update/<int:pk>/", views.UpdateDestination.as_view()),
    path("destination/api/v1/delete/<int:pk>/", views.DeleteDestination.as_view()),
]