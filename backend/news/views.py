from django.http import Http404
from django.views.generic import ListView, DetailView

from backend.news.models import Post


class PostList(ListView):
    """Вывод списока новостей"""
    model = Post
    paginate_by = 10
    template_name = 'news/post_list.html'

    def get_queryset(self):
        if self.kwargs.get("slug"):
            posts = Post.objects.filter(category__slug=self.kwargs.get("slug"))
        else:
            posts = Post.objects.all()
        if posts.exists():
            return posts
        else:
            raise Http404


class PostDetailView(DetailView):
    """Вывод новости"""
    model = Post
    template_name = 'news/post_detail.html'

    def get_object(self, queryset=None):
        obj = super(PostDetailView, self).get_object(queryset)
        if obj.published:
            return obj
        else:
            raise Http404("Пост не найден!")

# class AddComment(View):
#     def get(self, request, *args, **kwargs):
#         print(f'args = {self.args}\nkwargs={self.kwargs}\n')
#         # x=PostList.get_queryset(self)
#         # print(f'x={x}\n')
#         pass
