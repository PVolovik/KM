from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now(), final_date__gt=timezone.now()).order_by('-pub_date')

class ArchiveView(generic.ListView):
    template_name = 'polls/archive.html'
    context_object_name = 'a_question_list'

    def get_queryset(self):
        q1 = Question.objects.filter(final_date__lt=timezone.now())
        q2 = Question.objects.filter(completed = True)
        return q1.union(q2)

class ChoiceListView(generic.ListView):
    model = Choice
    paginate_by = 2


class ChoiceDetailView(generic.DetailView):
    model = Choice
    template_name = 'polls/choice_detail.html'


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        for q in Question.objects.filter(pub_date__lte=timezone.now()):
            q.completed = q.was_completed()
            q.save()
        return Question.objects.filter(pub_date__lte=timezone.now())

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        result = [['Участник', 'Количество голосов']]
        for pers in self.object.choice_set.all():
            result.append([' '.join([pers.first_name, pers.last_name]), pers.votes])
        context['graf'] = result
        return context


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Вы не выбрали вариант.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        result = [['Участник', 'Количество голосов']]
        for pers in question.choice_set.all():
            result.append([' '.join([pers.first_name,pers.last_name]), pers.votes ])
        return render(request, 'polls/result.html', {
            'question': question,
            'graf': result,
        })
