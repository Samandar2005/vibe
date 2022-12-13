from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.


class Worker(models.Model):
  full_name = models.CharField(max_length=200)
  image = models.ImageField(upload_to='worker/')
  description = models.TextField()


  def __str__(self) -> str:
    return self.full_name
