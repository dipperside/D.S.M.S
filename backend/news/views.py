from django.views.generic import ListView

from backend.news.models import Post


class PostList(ListView):

    model = Post
    paginate_by = 10
    template_name = 'news/post_list.html'

    def get_queryset(self):
        queryset = super(PostList, self).get_queryset()
        return queryset.filter(published=True)