from django.contrib import admin
from django.urls import path,include
from review import views

app_name = "review"

urlpatterns = [
    # Review
    path("review/api/v1/list/", views.GetAllReview.as_view()),
    path("review/api/v1/create/", views.CreateReview.as_view()),
    path("review/api/v1/get/<int:pk>/", views.GetReview.as_view()),
    path("review/api/v1/update/<int:pk>/", views.UpdateReview.as_view()),
    path("review/api/v1/delete/<int:pk>/", views.DeleteReview.as_view())

]