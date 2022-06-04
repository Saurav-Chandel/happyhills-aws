from django.db import models
from upcoming_treks.models import Upcoming_Road_Trips
from package.models import Package
# Create your models here.

class State(models.Model):
  
    image = models.ImageField(upload_to ='state/',null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    overview=models.CharField(max_length=3000,null=True,blank=True)

    def __str__(self):
        return str(self.name)


class District(models.Model):
    image = models.ImageField(upload_to ='district/',null=True,blank=True)
    overview=models.CharField(max_length=3000,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    state=models.ForeignKey(State,on_delete=models.CASCADE, related_name="state",null=True,blank=True)
    route = models.CharField(max_length=200,null=True,blank=True)
    altitude = models.CharField(max_length=200,null=True,blank=True)
    trek_length = models.CharField(max_length=100,null=True,blank=True)
    duration = models.CharField(max_length=100,null=True,blank=True)
    best_season = models.CharField(max_length=100,null=True,blank=True)
    difficulty_level = models.CharField(max_length=100,null=True,blank=True)
    

    def __str__(self):
        return self.name


class Destination(models.Model):
    package=models.ForeignKey(Package,on_delete=models.CASCADE,related_name="destination_package",null=True,blank=True)
    
    overview=models.CharField(max_length=3000,null=True,blank=True)
    image = models.ImageField(upload_to ='destination/',null=True,blank=True)
    
    name = models.CharField(max_length=100,null=True,blank=True)
    district = models.ForeignKey(District,on_delete=models.CASCADE,related_name="district")
    route = models.CharField(max_length=200,null=True,blank=True)
    altitude = models.CharField(max_length=200,null=True,blank=True)
    trek_length = models.CharField(max_length=100,null=True,blank=True)
    duration = models.CharField(max_length=100,null=True,blank=True)
    best_season = models.CharField(max_length=100,null=True,blank=True)
    difficulty_level = models.CharField(max_length=100,null=True,blank=True)
    

    def __str__(self):
        return self.name

