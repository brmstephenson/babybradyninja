from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice


def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()
    total_votes = 0
    boy_votes = 0
    girl_votes = 0
    for choice in choices:
        if choice.choice_text == 'boy':
            boy_votes = choice.number_of_votes
        elif choice.choice_text == 'girl':
            girl_votes = choice.number_of_votes

        total_votes += choice.number_of_votes
    boy_percent = int(boy_votes / total_votes * 100) - 10
    girl_percent = int(girl_votes / total_votes * 100) - 10

    return render(request, 'polls/results.html', {
        'question': question,
        'boy_votes': boy_votes,
        'girl_votes': girl_votes,
        'boy_percent': boy_percent,
        'girl_percent': girl_percent
    })


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't select a choice!",
        })
    else:
        selected_choice.number_of_votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
