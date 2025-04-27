from django.db import models

# Create your models here.
class Resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    batch = models.CharField(max_length=100)
    percentage_10 = models.CharField(max_length=100)
    percentage_12 = models.CharField(max_length=100)
    graduation_percentage = models.CharField(max_length=100)
    current_location = models.CharField(max_length=100)
    skills = models.TextField()
    upload_resume = models.FileField(upload_to='resume/')

    def __str__(self):
        return self.name