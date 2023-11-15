from django.db import models

# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=70)
  roll = models.IntegerField()
  city = models.CharField(max_length=90)

  def __str__(self):
    return f"{self.name}"
