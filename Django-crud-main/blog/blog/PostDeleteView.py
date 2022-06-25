
from .models import Post
from django.views import View
from django.views.generic import DeleteView


class PostDeleteView(View):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy ('blog: all')



    