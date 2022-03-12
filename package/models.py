from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.


class Images(models.Model):
    image=models.ImageField(upload_to='describe_destination',null=True,blank=True)
    descritption=models.CharField(max_length=200,null=True,blank=True)

class Package(models.Model):
    package_name=models.CharField(max_length=100,null=True,blank=True)
    images = models.ForeignKey(Images,on_delete=models.CASCADE,related_name="images_package",null=True,blank=True)
    description=models.CharField(max_length=500,null=True,blank=True)
    total_price= models.PositiveBigIntegerField(
        validators=[MaxValueValidator(9999999)], blank=True, null=True, unique=False)

    discount_price = models.PositiveBigIntegerField(
        validators=[MaxValueValidator(9999999)], blank=True, null=True, unique=False)   
    actual_price=models.PositiveBigIntegerField(
        validators=[MaxValueValidator(9999999)], blank=True, null=True, unique=False)     
    # rating = models.PositiveBigIntegerField(
    #     validators=[MaxValueValidator(9999999)], blank=True, null=True, unique=False)
    time = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.package_name


    def save(self, *args, **kwargs):
        self.discount=self.total_price*self.discount_price/100
        self.actual_price=self.total_price-self.discount

        super(Package, self).save(*args, **kwargs) # Call the "real" save() method.      






