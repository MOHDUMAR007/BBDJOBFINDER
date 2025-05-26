from django import forms
from .models import Resume, Company

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border-2 border-blue-400 bg-blue-50 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-4 py-2 border-2 border-blue-400 bg-blue-50 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition'}),
            'phone': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border-2 border-blue-400 bg-blue-50 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition'}),
            'address': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border-2 border-blue-400 bg-blue-50 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition', 'rows': 3}),
            'course': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border-2 border-blue-400 bg-blue-50 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition'}),
            'batch': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border-2 border-blue-400 bg-blue-50 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition'}),
            'percentage_10': forms.NumberInput(attrs={'class': 'w-full px-4 py-2 border-2 border-blue-400 bg-blue-50 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition', 'step': '0.01'}),
            'percentage_12': forms.NumberInput(attrs={'class': 'w-full px-4 py-2 border-2 border-blue-400 bg-blue-50 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition', 'step': '0.01'}),
            'graduation_percentage': forms.NumberInput(attrs={'class': 'w-full px-4 py-2 border-2 border-blue-400 bg-blue-50 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition', 'step': '0.01'}),
            'current_location': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border-2 border-blue-400 bg-blue-50 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition'}),
            'skills': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border-2 border-blue-400 bg-blue-50 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition', 'rows': 2}),
            'upload_resume': forms.ClearableFileInput(attrs={'class': 'w-full px-4 py-2 border-2 border-blue-400 bg-blue-50 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition'}),
        }

class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'location', 'industry']