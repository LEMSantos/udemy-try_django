from django.shortcuts import render

# Create your views here.
from .models import BlogPost


def blog_post_detail_page(request):
    blog_post = BlogPost.objects.first()

    template_name = 'blog_post_detail.html'
    context = {'blog_post': blog_post}

    return render(request, template_name, context)
