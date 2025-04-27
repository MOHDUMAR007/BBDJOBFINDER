from django.shortcuts import render
from .models import Resume

# Create your views here.
def browse(request):
    resumes = Resume.objects.all()
    print(resumes)
    context = {
    "resumes": resumes
    }
    return render(request, "browse.html", context)

def resumeDetail(request, resume_id):
    
    resume = get_object_or_404(Resume, id=resume_id)
    context = {
        "resume": resume
    }
    return render(request, "resume_detail.html")
    