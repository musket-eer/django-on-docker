# portfolio/views.py

from django.shortcuts import render


def index(request):
    return render(request, 'portfolio/index.html')


def about(request):
    return render(request, 'portfolio/about.html')


def stats(request):
    return render(request, 'portfolio/stats.html')


def portfolio_page(request):
    return render(request, 'portfolio/portfolio.html')


def blog(request):
    return render(request, 'portfolio/blog.html')


def currents(request):
    return render(request, 'portfolio/currents.html')


def misc(request):
    return render(request, 'portfolio/misc.html')
