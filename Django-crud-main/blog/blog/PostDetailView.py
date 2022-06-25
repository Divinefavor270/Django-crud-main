
from .models import Post
from django.views import View
from django.views.generic import DetailView


class PostDetailView(View):
    model = Post


    