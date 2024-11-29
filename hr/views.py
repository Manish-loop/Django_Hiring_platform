from django.shortcuts import render, redirect
from hr.models import Hr, JobPost, CandidateApplication, SelectCandidateJob
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def hrHome_views(request):
    if Hr.objects.filter(user=request.user).exists():
        jobpost = JobPost.objects.filter(user=request.user)
        print(jobpost)
        return render(request, 'hr/hrdashboard.html',{'jobpost':jobpost})
    return redirect('candidate_dashboard')

# def hrHome(request):
#     # Fetch job posts to display on the dashboard
#     jobposts = JobPost.objects.all()  # Replace with your actual query
#     context = {
#         'jobposts': jobposts,
#     }
#     return render(request, 'hr/hrdashboard.html', context)

@login_required
def post_job_views(request):
    msg = None
    if request.method == 'POST':
        job_title = request.POST.get('job-title')
        address = request.POST.get('address')
        company_name = request.POST.get('company-name')
        salary_low = request.POST.get('salary-low')
        salary_high = request.POST.get('salary-high')
        last_date = request.POST.get('last-date')
        print(job_title+" "+address+" "+company_name)
        msg = "Job added successfully"
        job_post = JobPost(user=request.user,title=job_title,address=address,companyName=company_name,salaryHigh=salary_high,salaryLow=salary_low,lastDateToApply=last_date)
        job_post.save()
    return render(request, 'hr/postjob.html',{'msg':msg})

@login_required
def candidate_view(request,pk):
    if JobPost.objects.filter(id=pk).exists():
        job = JobPost.objects.get(id=pk)
        
        applications = CandidateApplication.objects.filter(job=job) 
        selectedapplication = SelectCandidateJob.objects.filter(job=job)
        return render(request, 'hr/candidate.html',{'applications':applications,'selectedapplication':selectedapplication}) 
    return redirect('hr_dash')    
    