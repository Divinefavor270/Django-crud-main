
from .models import Post
from django.views import View
from django.views.generic import UpdateView


class PostUpdateView(View):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy ('blog: all')



    