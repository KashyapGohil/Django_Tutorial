# from django.http import request, response
# from django.http.response import Http404, HttpResponse, HttpResponseRedirect
# from django.shortcuts import render, resolve_url,get_object_or_404
# from django.http import HttpRequest
# from django.template import loader 
# from . models import Question,Choice
# from django.urls import reverse
# # Create your views here.

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {'latest_question_list':latest_question_list}
#     # return HttpResponse(template.render(context,request))
#     return render(request,'polls/index.html',context)

# def detail(request,question_id):
    
#     question = get_object_or_404(Question, pk=question_id)
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     return render(request,'polls/detail.html',{'question':question})

#     # return HttpResponse("You're looking at question %s" % question_id)

# def results(request,question_id):
#     #response = "You're looking at the results of question %s."
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request,'polls/results.html',{'question':question})

# def vote(request,question_id):
#     # return HttpResponse("You're voting on question %s." % question_id)
#     question = get_object_or_404(Question,pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except(KeyError,Choice.DoesNotExist):
#         return render(request,'polls/deatil.html',{
#             'question':question,
#             'error_message':"You didn't select a choice",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()

#         return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))



from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'polls/deatil.html',{
            'question':question,
            'error_message':"You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
