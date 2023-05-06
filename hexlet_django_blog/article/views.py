from django.views import View
from django.shortcuts import render, get_object_or_404

from hexlet_django_blog.article.models import Article


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        return render(request, 'article/index_article.html',
                      context={'articles': articles}
                      )


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['article_id'])
        return render(request, 'article/article_card.html',
                      context={'article': article},
                      )
