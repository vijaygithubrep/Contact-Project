from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    phone = models.IntegerField()

    def __str__(self):
        return self.first_name

class Company(models.Model):
    company_name = models.CharField(max_length=150)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Companies"
