from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from hr.models import JobPost, CandidateApplication
# Create your views here.

@login_required
def candidate_dashboard(request):
    jobs = JobPost.objects.all()
    print(jobs)
    return render(request,'candidate/dashboard.html',{'jobs':jobs})

@login_required
def myJobListviews(request):
    return render(request,'candidate/myjoblist.html')

@login_required
def applyforjob(request,pk):
    print(pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('name')
        college = request.POST.get('college')
        passing_year = request.POST.get('passing_year')
        yearOfExperience = request.POST.get('yearOfExperience')
        resume = request.FILES.get('resume')
        job = JobPost.objects.get(id=pk)
        CandidateApplication(user=request.user, job=job,passingYear=passing_year,yearOfExperience=yearOfExperience,resume=resume).save()
        return redirect('candidate_dashboard')
    return render(request,'candidate/apply.html')