from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Allcourses

# Create your views here.

def Courses(request):
    ac= Allcourses.objects.all()
    template=loader.get_template('TechnicalCourses/Courses.html')
    context={
        'ac':ac,
    }
    return HttpResponse(template.render(context, request))

def detail(request, course_id):
    try:
        course= Allcourses.objects.get(pk=course_id)
    except Allcourses.DoesNotExist:
        raise Http404("Course Not Found Error")
    return render(render, 'TechnicalCourses/detail.html',{'course':course})


