from django.views import View
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse


def index(request):
    # return render(request,'article/index_article.html')
    return redirect(reverse('article', kwargs={'tags': 'python', 'article_id': 42}), 302)


class HexletArticleIndex(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse(f'Статья номер {kwargs["article_id"]}. Тег {kwargs["tags"]}')
