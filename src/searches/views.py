from django.shortcuts import render

from blog.models import BlogPost
from .models import SearchQuery


def search_view(request):
    template_name = 'searches/view.html'
    query = request.GET.get('q', None)
    user = None

    if request.user.is_authenticated:
        user = request.user

    context = {'query': query}

    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        context['blog_list'] = BlogPost.objects.search(query=query)

    return render(request, template_name, context)
