from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.


class Worker(models.Model):
  full_name = models.CharField(max_length=200)
  image = models.ImageField(upload_to='worker/')
  before  = [
    (1, 'Работала в салоне с 8:00 до 21:00 практически без выходных. '),
    (2, 'Получала только процент от выручки, остальное забирало начальство.'),
    (3, 'Мало дней отпуска и в неудобное для меня время.'),
  ]
  after  = [
    (1, 'Занимаеюсь делом в свободном графике.'),
    (2, "Зарабатывает больше 150 000 рублей в месяц."),
    (3, 'Путешествую когда захочу и куда захочу.'),
  ]

  def __str__(self) -> str:
    return self.full_name
