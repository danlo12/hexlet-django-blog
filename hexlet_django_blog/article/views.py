from django.views import View

class Index(View):

    template_name = "articles.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = 'World'
        return context
# Create your views here.
