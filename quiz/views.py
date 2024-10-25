# quiz/views.py

from django.shortcuts import render
from .models import Question, Option

def quiz_view(request):
    questions = Question.objects.all()
    return render(request, 'quiz/quiz.html', {'questions': questions})

def result_view(request):
    score = 0
    total = 0
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('question_'):
                question_id = key.split('_')[1]
                option_id = value
                total += 1
                if Option.objects.filter(id=option_id, question_id=question_id, is_correct=True).exists():
                    score += 1
    return render(request, 'quiz/result.html', {'score': score, 'total': total})
