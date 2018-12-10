import os
from .forms import CoursesFinishedForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def welcome(request):
    return HttpResponse("<h1>欢迎来到首页！</h1>")

def upload(request):
    if request.method == 'POST':
        form = CoursesFinishedForm(request.POST)
        if form.is_valid():
            courses_finished = form.save()
            courses_finished.save()
            return HttpResponseRedirect(reverse('creditessential.views.welcome'))
        else:
            # that form is not valid
            pass
    elif request.method == 'GET':
        form = CoursesFinishedForm()
        APP_ROOT = os.path.dirname(os.path.abspath(__file__))
        # PROJECT_ROOT = os.path.dirname(APP_ROOT)
        return render(request, os.path.join(APP_ROOT, 'templates', 'data_upload.html'), {'form': form})
    else:
        # other methods
        pass