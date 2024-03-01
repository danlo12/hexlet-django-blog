from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from hexlet_django_blog.article.models import Article
from django.shortcuts import render, get_object_or_404
from django.forms import ModelForm
class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })

class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article,
        })

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ["name","body"]

class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/articles')
        return render(request, 'articles/create.html', {'form': form})
# Create your views here.

