from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from polls.models import Question
from django.shortcuts import get_object_or_404,render
from django.http import Http404

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #Because django has already looked for a folder name /templates/ in each app.
    context_dict = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context_dict)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)