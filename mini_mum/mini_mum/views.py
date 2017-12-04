"""Mini_mum app views."""


from django.views.generic import ListView
from blog.models import Blog


class HomeView(ListView):
    """HomeView class."""

    model = Blog
    template_name = 'blog/list.html'
    context_object_name = 'post'
    