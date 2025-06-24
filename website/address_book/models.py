from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=5)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
