import random
from faker import Faker
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

def profile(request, username):
    context = {
        'username' : username,
    }

    return render(request, 'profile.html', context)

def cube(request, number):
    result = number ** 3

    context = {
        'number' : number,
        'result' : result,
    }

    return render(request, 'cube.html', context)

def articles(request):
    fake = Faker()
    fake_articles = []
    
    for i in range(100):
        fake_articles.append(fake.text())

    context = {
        'fake_articles' : fake_articles,
    }

    return render(request, 'articles.html', context)

def ping(request):
    return render(request, 'ping.html')

def pong(request):

    title = request.GET.get('title')
    content = request.GET.get('content')

    context = {
        'title' : title,
        'content' : content,
    }

    return render(request, 'pong.html', context)