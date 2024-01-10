from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
class IndexView(View):

    template_name = "articles.html"

    def get(self, request, **kwargs):
        context = {'article_id':'', 'tags':''}
        context['article_id'] = kwargs['article_id']
        context['tags'] = kwargs['tags']
        return render(request, self.template_name, context)

def home_redirect(request):
    url = reverse('article',kwargs={'tags':"python",'article_id':'42'})
    return redirect(url)
# Create your views here.

