from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class Upcoming_Treks(models.Model):
    image = models.ImageField(upload_to ='trek/',null=True,blank=True)
    trek_name = models.CharField(max_length=100,null=True,blank=True)
    trip_duration = models.CharField(max_length=100,null=True,blank=True)
    trip_type = models.CharField(max_length=100,null=True,blank=True)
    activities = models.CharField(max_length=300,null=True,blank=True)
    group_size = models.CharField(max_length=100,null=True,blank=True)
    price = models.PositiveBigIntegerField(
        validators=[MaxValueValidator(9999999)], blank=True, null=True, unique=False)
    route = models.CharField(max_length=300,null=True,blank=True)     
    altitude = models.CharField(max_length=200,null=True,blank=True)
    trek_length = models.CharField(max_length=200,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.trek_name



class Upcoming_Road_Trips(models.Model):
    image = models.ImageField(upload_to ='road_trip/',null=True,blank=True)
    trip_name = models.CharField(max_length=100,null=True,blank=True)
    trip_duration = models.CharField(max_length=100,null=True,blank=True)
    trip_type = models.CharField(max_length=100,null=True,blank=True)
    activities = models.CharField(max_length=300,null=True,blank=True)
    group_size = models.CharField(max_length=100,null=True,blank=True)
    price = models.PositiveBigIntegerField(
        validators=[MaxValueValidator(9999999)], blank=True, null=True, unique=False)
    route = models.CharField(max_length=300,null=True,blank=True)  
    altitude = models.CharField(max_length=200,null=True,blank=True)
    total_distance_covered = models.CharField(max_length=200,null=True,blank=True)
    fixed_departure = models.CharField(max_length=200,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.trip_name     




