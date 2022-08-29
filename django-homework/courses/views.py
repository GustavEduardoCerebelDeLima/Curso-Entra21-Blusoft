from django.shortcuts import render


def index(request):
    return render(request, 'courses/index.html')


def html_course(request):
    return render(request, 'courses/html_course.html')


def css_course(request):
    return render(request, 'courses/css_course.html')


def javascript_course(request):
    return render(request, 'courses/javascript_course.html')


def python_course(request):
    return render(request, 'courses/python_course.html')
