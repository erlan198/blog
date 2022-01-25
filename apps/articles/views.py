from django.http import Http404
from django.shortcuts import render
from django.views import generic
from .models import Article


class ArticleListView(generic.TemplateView):
    template_name = "article_list.html"
    def get_context_data(self, **kwargs):
        context= dict()
        context["article_list"]= Article.objects.all()
        return context

class ArticleDetailView(generic.TemplateView):
    template_name = "article_detail.html"
    def get_context_data(self, **kwargs):
        context=dict()
        article_pk = kwargs["pk"]
        try:
            context["article_id"]=Article.objects.get(id=article_pk)
        except Article.DoesNotExist:
            raise Http404
        return  context
