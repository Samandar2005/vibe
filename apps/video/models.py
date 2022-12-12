from django.db import models


# Create your models here.
class Video(models.Model):
  video = models.FileField(blank=True, null=True, upload_to='video/')
  date_created = models.DateTimeField(auto_now_add=True, blank=True)
  is_active = models.BooleanField(default=True)

  def __str__(self) -> str:
    return f"Video url: {self.video}  Created date: {self.date_created} Active: {self.is_active}"