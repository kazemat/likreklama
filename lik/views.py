from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'layout.html', dict(
        active_page='main',
        title_lg='Главная',
        active=None))


def about(request):
    return render(request, 'pages/about.html', dict(
        active_page='about',
        title_lg='О нас',
        active=None))