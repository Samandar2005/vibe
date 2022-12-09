from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Customer(models.Model):
  images = models.ImageField(upload_to='customer/')
  date_created = models.DateTimeField(auto_now_add=True, blank=True)
  is_active = models.BooleanField(default=True)

  def __str__(self) -> str:
    return  f"image {self.images} date {self.date_created} is active {self.is_active}"
