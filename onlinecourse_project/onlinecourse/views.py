from django.shortcuts import render
from .models import Course

def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)

    return render(
        request,
        'onlinecourse/course_details_bootstrap.html',
        {'course': course}
    )


def submit(request, course_id):
    return render(
        request,
        'onlinecourse/exam_result.html',
        {
            'grade': 100,
            'passed': True
        }
    )


def show_exam_result(request, course_id):
    return render(
        request,
        'onlinecourse/exam_result.html',
        {
            'grade': 100,
            'passed': True
        }
    )
