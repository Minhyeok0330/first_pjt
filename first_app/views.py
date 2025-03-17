import random
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def hello(request):
    my_name = 'dayom'

    context = {
        'my_name': my_name,
    }

    return render(request, 'hello.html', context)

def lunch(request):
    menu = ['마라탕', '떡볶이', '제육덮밥']

    pick = random.choice(menu)

    context = {
        'pick':pick,
    }

    return render(request, 'lunch.html', context)

def lotto(request):
    lotto_num = range(1, 46)

    number = random.sample(lotto_num, 6)

    context = {
        'number':number,
    }
    return render(request, 'lotto.html', context)