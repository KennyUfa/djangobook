from django.shortcuts import render
from django.http import HttpResponse
from random import randint
from dnd.models import DndSpell
from django.views.generic import ListView

def home(request):
    return render(request, 'dnd/home.html')


def character(request):
    return render(request, 'dnd/character.html')


def roll_dice(request):
    if request.method == "GET":
        return render(request, 'dnd/dice_roller.html')
    elif request.method == "POST":
        rolls, result = hit_dice_roll(request.POST["amount"], request.POST[
            "dice_type"])
        start_amount = request.POST["amount"]
        start_dice_type = request.POST["dice_type"]

        return render(request, 'dnd/dice_roller.html',
                      {"rolls": rolls, "roll": result, "start": start_amount,
                       'start_dice_type': start_dice_type})


def hit_dice_roll(amount, dice_type):
    rolls = []
    for i in range(int(amount)):
        rolls.append(randint(1, int(dice_type)))
    result = sum(rolls)
    return rolls, result

class SpellView(ListView):
    model = DndSpell
# def spell_views(request):
#     spells = DndSpell.objects.all()
#     return render(request, 'dnd/dndspell_list.html', {'title': 'Список заклинаний',
#                                               'spells': spells})


def get_spell(request, spell_id):
    spell = DndSpell.objects.get(id=spell_id)
    return render(request, 'dnd/spell.html', {'spell': spell})
