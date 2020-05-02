from django.shortcuts import render
from weblog.models import Post, Comment, Category


def blog_index(request):
    posts = Post.objects.filter(is_published=True).order_by("-date")

    return render(
        request,
        "weblog/index.html",
        context={
            "posts": posts
        }
    )
