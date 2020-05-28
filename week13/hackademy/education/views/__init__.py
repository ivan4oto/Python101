from education.views import courses, lectures, tasks
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})

