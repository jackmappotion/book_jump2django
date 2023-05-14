# from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotAllowed
from django.utils import timezone
from django.core.paginator import Paginator

from .models import Question
from .forms import QuestionForm, AnswerForm

def index(request):
    page = request.GET.get('page','1')
    question_list = Question.objects.order_by("-create_date")
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    context = {'question_list':page_obj}
    return render(request=request, template_name='pybo/question_list.html', context=context)

def detail(request, question_id):
    question = get_object_or_404(klass=Question, pk=question_id)
    # question = Question.objects.get(id=question_id)
    context = {'question':question}
    return render(request=request, template_name='pybo/question_detail.html', context=context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question':question, 'form':form}
    return render(request=request,template_name='pybo/question_detail.html',context=context)

def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form':form}
    return render(request=request, template_name='pybo/question_form.html', context=context)