from django.views.generic.base import TemplateView

class ArticleIndexView(TemplateView):

    template_name = 'article/articles_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'ARTICLE'
        return context
