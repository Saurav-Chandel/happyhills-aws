from django.contrib import admin
from .models import *

# Register your models here.

# class StateAdmin(admin.ModelAdmin):
#     list_display = (
#         "id",
#         "name",
#     )
#     list_display_links = ("id",)
#     list_per_page = 50


# class DistrictAdmin(admin.ModelAdmin):
#     list_display = (
#         "id",
#         "name",
#         "state"
#     )
#     list_display_links = ("id",)
#     list_per_page = 50

# class DestinationAdmin(admin.ModelAdmin):
#     list_display = (
#         "id",
#         "name",
#         "district"
#     )
#     list_display_links = ("id",)
#     list_per_page = 50

admin.site.register(State)
admin.site.register(District)
admin.site.register(Destination)