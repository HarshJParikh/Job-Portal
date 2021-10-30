from django.urls import path, include

from .views import dashboard, view_application, view_dashboard_job, interview_for_job, apply_interview

urlpatterns = [
	path('', dashboard, name='dashboard'),
	path('job/<int:job_id>/', view_dashboard_job, name='view_dashboard_job'),
	path('application/<int:application_id>/', view_application, name='view_application'),
	path('application/<int:application_id>/interviewpage/', apply_interview, name="apply_interview"),
	path('application/<int:application_id>/interview_for_job/', interview_for_job, name='interview_for_job'),
]