from django.shortcuts import render

from hr.models import JobPost

# Create your views here.

def hrHome_views(request):
    return render(request, 'hr/hrdashboard.html')

# def hrHome(request):
#     # Fetch job posts to display on the dashboard
#     jobposts = JobPost.objects.all()  # Replace with your actual query
#     context = {
#         'jobposts': jobposts,
#     }
#     return render(request, 'hr/hrdashboard.html', context)

def post_job_views(request):
    return render(request, 'hr/postjob.html')

def candidate_view(request,pk):
    print(pk)
    return render(request, 'hr/candidate.html')