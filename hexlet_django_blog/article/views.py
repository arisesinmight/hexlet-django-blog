from django.shortcuts import render

def index(request):
    return render(request, 'article/articles_index.html', context={
        'name': 'ARTICLE',
    })