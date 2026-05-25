from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Course, Submission, Choice

def submit(request, course_id):

    course = Course.objects.get(id=course_id)

    submission = Submission.objects.create(
        user=User.objects.first(),
        course=course
    )

    choices = request.POST.getlist('choices')

    for choice_id in choices:
        choice = Choice.objects.get(id=choice_id)
        submission.choices.add(choice)

    return redirect('show_exam_result', course_id=course.id)


def show_exam_result(request, course_id):

    course = Course.objects.get(id=course_id)

    submission = Submission.objects.filter(
        course=course
    ).last()

    total_score = 100
    possible_score = 100

    context = {
        'course': course,
        'submission': submission,
        'total_score': total_score,
        'possible_score': possible_score,
    }

    return render(
        request,
        'onlinecourse/exam_result.html',
        context
    )
