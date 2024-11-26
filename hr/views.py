from django.shortcuts import render
from hr.models import JobPost, CandidateApplication, SelectCandidateJob
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def hrHome_views(request):
    
    return render(request, 'hr/hrdashboard.html',{'jobs':jobs})

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
        job_title = request.POst.get('job-title')
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
    print(pk)
    return render(request, 'hr/candidate.html')