from django.views.generic import ListView, DetailView
from django.http import Http404

from backend.news.models import Post


class PostList(ListView):

    model = Post
    paginate_by = 10
    template_name = 'news/post_list.html'

    def get_queryset(self):
        queryset = super(PostList, self).get_queryset()
        return queryset.filter(published=True)


class PostDetailView(DetailView):

    model = Post
    template_name = 'news/post_detail.html'

    def get_object(self, queryset=None):
        object = super(PostDetailView, self).get_object(queryset)
        if object.published:
            return object
        else:
            raise Http404("Пост не найден!")
