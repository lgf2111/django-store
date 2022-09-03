from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'seller': 'lgf2111',
        'title': 'Macbook Pro',
        'description': 'First ever macbook gotten.',
        'date_posted': 'August 27, 2018'
    },
    {
        'seller': 'Jane Doe',
        'title': 'Samsung TV',
        'description': 'Last ever tv gotten.',
        'date_posted': 'August 28, 2018'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'store/home.html', context)

def about(request):
    return render(request, 'store/about.html')
