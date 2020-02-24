from django.shortcuts import render
from .models import Question,Choice
def index(request):
        latest_question_list = Question.objects.order_by('-published_date')
        context = {'latest_question_list':latest_question_list}
        return render(request, 'poll/index.html',context)
