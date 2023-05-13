# from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Question


def index(request):
    question_list = Question.objects.order_by("-create_date")
    context = {'question_list':question_list}
    return render(request=request, template_name='pybo/question_list.html', context=context)

def detail(request, question_id):
    question = get_object_or_404(klass=Question, pk=question_id)
    # question = Question.objects.get(id=question_id)
    context = {'question':question}
    return render(request=request, template_name='pybo/question_detail.html', context=context)
