from django.shortcuts import render, get_object_or_404

from .models import Question

def index(request):
    #
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)

def results(request, question_id):
    #
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()
    context = {
        'question': question,
        'choices_list': choices,
    }
    return render(request, 'polls/results.html', context)

def vote(request):
    #
    return render(request, 'polls/index.html')

def detail(request, question_id):
    #
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()
    context = {
        'question': question,
        'choices_list': choices,
    }
    return render(request, 'polls/detail.html', context)

