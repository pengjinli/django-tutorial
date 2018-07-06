from django.shortcuts import render

def index(request):
    #
    return render(request, 'polls/index.html')

def results(request):
    #
    return render(request, 'polls/index.html')

def vote(request):
    #
    return render(request, 'polls/index.html')

def detail(request):
    #
    return render(request, 'polls/index.html')

