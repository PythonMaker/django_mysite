from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse

# 视图的工作就是：从参数获取数据，装载一个模板，然后将根据获取的数据对模板进行渲染。
# 如果想看见视图的效果，我们需要将一个 URL 映射到它，这就是我们需要 URLconf 的原因了。
def index(request):
    # question_all = Question.objects.all()
    context = {'question_all': Question.objects.all()}
    return render(request, 'polls\index.html', context)

    # question = Question.objects.get(pk=7)
    # choice_list = ', '.join(
    #     [str(i+1) + '、' + c.choice_text
    #      for i, c in enumerate(question.choice_set.all())])

    # return HttpResponse(question.question_text + choice_list)
    # return HttpResponse("您现在看到的是 Django 的第一个页面！")


def detail(request, question_id):
    # question = Question.objects.get(pk=question_id)
    question = get_object_or_404(Question, pk=question_id)
    # choice_set = [
    #     str(i + 1) + '、' + c.choice_text
    #     for i, c in enumerate(question.choice_set.all())
    # ]
    context = {'question': question}
    return render(request, 'polls\detail.html', context)
    # return HttpResponse('该问题的选项包括： %s.' % request.GET)


def results(request, question_id):
    response = "您正在查看结果。问题编号是 %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': '你没有选择任何选项。'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(
            reverse('polls:results', args=(question.id, )))

    # return HttpResponse("您正在查看的问题编号是 %s." % question_id)
