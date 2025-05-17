from django.db import models
from django.contrib.auth.models import User

# Existing Resume model
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

# Updated Company model
class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company_profile', null=True, blank=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)  # <-- Add this line

    def __str__(self):
        return self.name

# New ResumeReference model
class ResumeReference(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='references')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='references')
    referred_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=50,
        choices=[
            ('Pending', 'Pending'),
            ('Accepted', 'Accepted'),
            ('Rejected', 'Rejected'),
        ],
        default='Pending'
    )
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.resume.name} -> {self.company.name}"

# New UserProfile model with photo field
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"

# Signal to create or update UserProfile when User is created or updated
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
