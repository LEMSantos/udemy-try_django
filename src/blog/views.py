from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render

# Create your views here.
from .forms import BlogPostModelForm
from .models import BlogPost


def blog_post_list_view(request):
    queryset = BlogPost.objects.all()

    template_name = 'blog/list.html'
    context = {'blog_post_list': queryset}

    return render(request, template_name, context)


@staff_member_required
def blog_post_create_view(request):
    form = BlogPostModelForm(request.POST or None)

    if form.is_valid():
        blog_post = form.save(commit=False)
        blog_post.user = request.user
        blog_post.save()

        form = BlogPostModelForm()

    template_name = 'blog/form.html'
    context = {'form': form}

    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    queryset = BlogPost.objects.filter(slug=slug)

    if queryset.count() == 0:
        raise Http404

    blog_post = queryset.first()

    template_name = 'blog/detail.html'
    context = {'blog_post': blog_post}

    return render(request, template_name, context)


@staff_member_required
def blog_post_update_view(request, slug):
    queryset = BlogPost.objects.filter(slug=slug)

    if queryset.count() == 0:
        raise Http404

    blog_post = queryset.first()
    form = BlogPostModelForm(request.POST or None, instance=blog_post)

    if form.is_valid():
        form.save()

    template_name = 'form.html'
    context = {
        'title': f'Update {blog_post.title}',
        'form': form,
    }

    return render(request, template_name, context)


@staff_member_required
def blog_post_delete_view(request, slug):
    queryset = BlogPost.objects.filter(slug=slug)

    if queryset.count() == 0:
        raise Http404

    blog_post = queryset.first()

    template_name = 'blog/delete.html'
    context = {'blog_post': blog_post}

    return render(request, template_name, context)
