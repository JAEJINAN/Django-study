from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    # template_name = 'blog/index.html'
    ordering = '-pk'


class PostDetail(DetailView):
    model = Post
    # template_name = 'blog/single_post_page.html'
    

# FBV Style Code
# def index(request):
#     posts = Post.objects.all().order_by('-pk')
#     return render(request,
#                   'blog/index.html',
#                   {'posts': posts})


# def single_post_page(request, pk: int):
#     post = Post.objects.get(pk=pk)
#     return render(request, 'blog/single_post_page.html',
#                   {
#                    'post': post,
#                    })
