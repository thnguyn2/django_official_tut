from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from polls.models import Question, Choice
from django.shortcuts import get_object_or_404, render
from django.views import generic

class IndexView(generic.ListView):
#Note these are the classes, not methods
    template = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #Because django has already looked for a folder name /templates/ in each app.
    context_dict = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context_dict)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    #question.id is the property of the object in the database
    #question_id is the field extracted from the url
    #Retrive the question object in the dictionary
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        #request.POST is a dictionary of the submitted data
    except (KeyError, Choice.DoesNotExist):
        #Redisplay the voting form
        return render(request, 'polls/detail.html', {'question': question, 'error_message': 'You did not select a choice'})
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        #Direct to the result of the current question, just needs the URL