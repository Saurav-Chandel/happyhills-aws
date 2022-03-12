from django.contrib import admin
from django.urls import path,include
from package import views

app_name = "package"

urlpatterns = [
    
    # Package
    path("package/api/v1/list/", views.GetAllPackage.as_view()),
    path("package/api/v1/create/", views.CreatePackage.as_view()),
    path("package/api/v1/get/<int:pk>/", views.GetPackage.as_view()),
    path("package/api/v1/update/<int:pk>/", views.UpdatePackage.as_view()),
    path("package/api/v1/delete/<int:pk>/", views.DeletePackage.as_view())
]