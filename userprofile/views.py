from django import template
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from job.models import Job, Application
from .models import ConversationMessage, Interview
from notification.utilities import create_notification
from .forms import InterviewForm
from django.db import IntegrityError
from django.template.loader import render_to_string
from django.http import HttpResponse

@login_required
def dashboard(request):
    return render(request, 'userprofile/dashboard.html', {'userprofile': request.user.userprofile})

@login_required
def errorpage(request):
    return render(request, 'userprofile/errorpage.html')

@login_required
def view_application(request, application_id):
    if request.user.userprofile.is_employer:
        application = get_object_or_404(Application, pk=application_id, job__created_by=request.user)
        interview = Interview.objects.get(app_id=application_id)
    else:
        application = get_object_or_404(Application, pk=application_id, created_by=request.user) 
        interview = None 
    
    if request.method == 'POST':
        content = request.POST.get('content')

        if content:
            conversationmessage = ConversationMessage.objects.create(application=application, content=content, created_by=request.user)

            create_notification(request, application.created_by, 'message', extra_id=application.id)

            return redirect('view_application', application_id=application_id)
    
    return render(request, 'userprofile/view_application.html', {'application': application, 'userprofile': request.user.userprofile, 'interview' : interview})

@login_required
def view_dashboard_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id, created_by=request.user)
    return render(request, 'userprofile/view_dashboard_job.html', {'job': job})

@login_required
def interview_for_job(request, application_id):
    app = Application.objects.get(pk=application_id)
    idapp = get_object_or_404(Application, pk=application_id, created_by=request.user)
    if request.method == 'POST':
        form = InterviewForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                application = form.save(commit=False)
                application.app = app
                application.save()
                return redirect('dashboard')
            except IntegrityError:
                rendered = render_to_string('userprofile/errorpage.html')
                return HttpResponse(rendered)
    else:
        form = InterviewForm()
    
    return render(request, 'userprofile/interview_for_job.html', {'form' : form, 'app' : app, 'idapp': idapp})

@login_required	
def apply_interview(request, application_id):
	application = get_object_or_404(Application, pk=application_id, created_by=request.user)
	return	render(request, 'userprofile/interviewpage.html', {'application' : application})