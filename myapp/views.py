from django.shortcuts import render
from django.http import JsonResponse
from .models import Course, Question

def home(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'home.html', context)

def api_question(request, id):
    raw_questions = Question.objects.filter(course=id)[:20]
    questions = []

    for raw_question in raw_questions:
        question = {
            'question': raw_question.question,
            'answer': raw_question.answer,
            'options': [
                raw_question.option_one,
                raw_question.option_two,
                raw_question.option_three,
                raw_question.option_four
            ]
        }
        questions.append(question)

    return JsonResponse(questions, safe=False)

def take_quiz(request, id):
    context = {'id': id}
    return render(request, 'quiz.html', context)
