from django.contrib import admin

# Register your models here.
from .models import Resume, Company, ResumeReference, HelpRequest
admin.site.register(Resume)
admin.site.register(Company)
admin.site.register(ResumeReference)
admin.site.register(HelpRequest)