from django.db import models

# Create your models here.
class details(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.TextField()
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.user_name

