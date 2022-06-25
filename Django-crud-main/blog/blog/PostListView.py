from .models import Post
from django.views import View
from django.views.generic.list import ListView
class PostListView(View):
    model=Post
    