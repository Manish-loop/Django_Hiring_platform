from django.urls import path
from hr import views


urlpatterns = [
    path('hrdash/', views.hrHome),
    path('post-job',views.post_job,name='post_job')
]
