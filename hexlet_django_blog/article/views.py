from django.shortcuts import render


def index(request):
    return render(request, 'index_article.html', context={'name_app': ['Article'],})
