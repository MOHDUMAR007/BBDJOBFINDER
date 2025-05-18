from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Resume, ResumeReference, Company
from .forms import ResumeForm, CompanyProfileForm, HelpRequestForm
from django.views.decorators.http import require_POST
from django.http import HttpResponseForbidden


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

def company_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and hasattr(user, 'company_profile'):
            login(request, user)
            return redirect('company_dashboard')
        else:
            messages.error(request, "Invalid credentials or not a company account.")
    return render(request, 'company_login.html')

def company_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        location = request.POST['location']
        industry = request.POST['industry']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            user = User.objects.create_user(username=username, password=password)
            company = Company.objects.create(user=user, name=name, location=location, industry=industry)
            login(request, user)
            return redirect('company_dashboard')
    return render(request, 'company_register.html')

@login_required
def company_dashboard(request):
    if not hasattr(request.user, 'company_profile'):
        return HttpResponseForbidden("You do not have access to the company dashboard.")
    company = request.user.company_profile
    references = ResumeReference.objects.filter(company=company)
    return render(request, 'company_dashboard.html', {
        'company': company,
        'references': references,
    })

def company_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('company_login')

def upload_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('browse')  # Redirect to the browse page after successful upload
    else:
        form = ResumeForm()
    return render(request, 'upload_resume.html', {'form': form})

def home(request):
    return render(request, 'index.html')

def resume_status(request):
    references = ResumeReference.objects.all()  # Or filter by user if needed
    return render(request, 'resume_status.html', {'references': references})

def form_page(request):
    return render(request, 'form_page.html')

def delete_resume(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)
    if request.method == "POST":
        resume.delete()
    return redirect('browse')

def submit_resume(request):
    if request.method == "POST":
        # handle form data here
        pass
    return render(request, 'form_page.html')

@login_required
def manage_company_profile(request):
    # Check if the user has a company_profile (Company object)
    company = getattr(request.user, 'company_profile', None)
    if not company:
        messages.error(request, "You do not have a company profile. Please register as a company.")
        return redirect('home')  # or another appropriate page

    if request.method == 'POST':
        form = CompanyProfileForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_dashboard')
    else:
        form = CompanyProfileForm(instance=company)
    return render(request, 'company_profile.html', {'form': form})

@require_POST
@login_required
def update_reference_status(request, ref_id):
    reference = get_object_or_404(ResumeReference, id=ref_id, company=request.user.company_profile)
    new_status = request.POST.get('status')
    if new_status in ['Accepted', 'Rejected']:
        reference.status = new_status
        reference.save()
    return redirect('company_dashboard')

def help_view(request):
    if request.method == 'POST':
        form = HelpRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'help.html', {'form': HelpRequestForm(), 'success': True})
    else:
        form = HelpRequestForm()
    return render(request, 'help.html', {'form': form})
