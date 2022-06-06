from django.shortcuts import render
from random import randint
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from time import sleep
from dnd.models import DndSpell


# Create your views here.

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
