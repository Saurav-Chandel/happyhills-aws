from django.db import models
from django.core.validators import MaxValueValidator

from package.models import *
from exploreapp.models import *
# Create your models here.
class Review(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, blank=True, null=True, related_name="review_package")

    rating = models.PositiveBigIntegerField(
        validators=[MaxValueValidator(9999999)], blank=True, null=True, unique=False)
    # total_price=models.PositiveBigIntegerField(
    #     validators=[MaxValueValidator(9999999)], blank=True, null=True, unique=False)
    # discount=models.PositiveBigIntegerField(
    #     validators=[MaxValueValidator(9999999)], blank=True, null=True, unique=False)    
    review = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # file_field= models.FileField(upload_to="review_file/", blank=True, null=True)

    def __str__(self):
        return self.package.package_name





