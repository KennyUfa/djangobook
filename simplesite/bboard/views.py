import random

from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Bb
from .models import Rubric
from django.views.generic.edit import CreateView
from .forms import BbForm


def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', context)


def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


def home(request):
    return render(request, 'bboard/home.html')


def time(request):
    return render(request, 'bboard/timer.html')


from django.shortcuts import render
from random import randint


# Create your views here.

def attack_def(request):
    if request.method == "GET":
        return render(request, 'bboard/dice_roller.html')
    elif request.method == "POST":
        rolls, result = hit_dice_roll(request.POST["amount"], request.POST[
            "dice_type"])
        start_amount = request.POST["amount"]
        start_dice_type = request.POST["dice_type"]

        return render(request, 'bboard/dice_roller.html',
                      {"rolls": rolls, "roll": result, "start": start_amount,
                       'start_dice_type': start_dice_type})


def hit_dice_roll(amount, dice_type):
    rolls = []
    for i in range(int(amount)):
        rolls.append(random.randint(1, int(dice_type)))
    result = sum(rolls)
    return rolls, result
