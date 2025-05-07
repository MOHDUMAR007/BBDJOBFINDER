from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'email', 'phone', 'address', 'course', 'batch', 'percentage_10', 'percentage_12', 'graduation_percentage', 'current_location', 'skills', 'upload_resume']