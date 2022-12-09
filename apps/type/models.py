from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Type(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField()
  images = models.ImageField(upload_to='blog/')
  date_created = models.DateTimeField(auto_now_add=True, blank=True)
  is_active = models.BooleanField(default=True)

  def __str__(self) -> str:
    return self.title
