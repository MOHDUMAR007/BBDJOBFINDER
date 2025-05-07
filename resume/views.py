from django.shortcuts import render
from .models import Resume
# from .forms import ResumeForm


# Create your views here.
def browse(request):
    resumes = Resume.objects.all()
    print(resumes)
    context = {
    "resumesList": resumes
    }
    return render(request, "browse.html", context)

def resumeDetail(request, resume_id):
    
    resume = get_object_or_404(Resume, id=resume_id)
    print(resume)
    context = {
        "resume": resume
    }
    return render(request, "resume_detail.html")

# def upload_resume(request):
#     if request.method == 'POST':
#         form = ResumeForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('browse')  # Redirect to the browse page after successful upload
#     else:
#         form = ResumeForm()
#     return render(request, 'upload_resume.html', {'form': form})
    