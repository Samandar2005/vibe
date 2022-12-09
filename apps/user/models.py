from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Ovner(models.Model):
  phoone_number = PhoneNumberField(null=False, blank=False, unique=True)
  date_created = models.DateTimeField(auto_now_add=True, blank=True)
  is_active = models.BooleanField(default=True)

  def __str__(self) -> str:
    return f"User phone number: {self.phoone_number} Created date: {self.date_created}"
