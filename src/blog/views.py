from django.db.models import query
from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import BlogPost


def blog_post_list_view(request):
    queryset = BlogPost.objects.all()

    template_name = 'blog/list.html'
    context = {'blog_post_list': queryset}

    return render(request, template_name, context)


def blog_post_create_view(request):
    template_name = 'blog/create.html'
    context = {'form': None}

    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    queryset = BlogPost.objects.filter(slug=slug)

    if queryset.count() == 0:
        raise Http404

    blog_post = queryset.first()

    template_name = 'blog/detail.html'
    context = {'blog_post': blog_post}

    return render(request, template_name, context)


def blog_post_update_view(request, slug):
    queryset = BlogPost.objects.filter(slug=slug)

    if queryset.count() == 0:
        raise Http404

    blog_post = queryset.first()

    template_name = 'blog/update.html'
    context = {'blog_post': blog_post, 'form': None}

    return render(request, template_name, context)


def blog_post_delete_view(request):
    queryset = BlogPost.objects.filter(slug=slug)

    if queryset.count() == 0:
        raise Http404

    blog_post = queryset.first()

    template_name = 'blog/delete.html'
    context = {'blog_post': blog_post}

    return render(request, template_name, context)
