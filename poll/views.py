from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Question,Choice
from django.urls import reverse
from django.template import loader

def index(request):
        latest_question_list = Question.objects.order_by('-published_date')
        context = {'latest_question_list':latest_question_list}
        return render(request, 'poll/index.html',context)
def detail(request,question_id):
        try:
                question = Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
                raise Http404("Questions Does Not Exist")     
        return render(request , 'poll/detail.html',{'question':question})   

def results(request,question_id):
        question = get_object_or_404(Question,pk=question_id)
        return render(request,'poll/results.html',{'question':question})
def vote(request,question_id):
        question = get_object_or_404(Question,pk=question_id)
        try:
                selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except [KeyError , Choice.DoesNotExist]:
                return render(request,'poll/detail.html',{
                        'question':question,
                        'error_message':"Select a choice you fucking asshole",
                })       
        else:
                selected_choice.votes +=1
                selected_choice.save() 
                return HttpResponseRedirect(reverse('poll:results', args=(question_id,)))