from django.shortcuts import render
from django.http import HttpResponse
from .models import Interview
from django.contrib.auth.models import User
from .forms import InterviewForm

def InterviewPanel(request):
    if request.method == "GET":
        form = InterviewForm()
        return render(
            request, 
            "interview-panel.html",
            {
                "participants" : User.objects.all() , 
                "interviews" : Interview.objects.all(),
                "form": form
            }
        )

    elif request.method == "POST":
        interview_participants = []
        for participant in request.POST.getlist('participants'):
            interview_participants.append(participant)
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        print(interview_participants)
        print(start_time)
        print(end_time)
        interview = Interview.objects.create(start_time=start_time , end_time=end_time)
        for participant in interview_participants:
            p = User.objects.get(username=participant)
            print(p)
            interview.participants.add(p)
        return render(
            request, 
            "interview-panel.html",
            {
                "participants" : User.objects.all() , 
                "interviews" : Interview.objects.all()
            }
        )
