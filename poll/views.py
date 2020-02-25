from django.shortcuts import render
from .models import Question,Choice
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
