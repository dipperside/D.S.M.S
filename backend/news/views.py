from django.core.cache import cache
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from backend.news.models import Post
from backend.pages.models import PageHit
from backend.comments.forms import CommentForm


class PostList(ListView):
    """Вывод списока новостей"""
    model = Post
    paginate_by = 10
    template_name = 'news/post_list.html'

    def get_queryset(self):
        if self.kwargs.get("slug"):
            posts = Post.objects.filter(category__slug=self.kwargs.get("slug"))
        else:
            posts = Post.objects.filter(published__exact=True)
        if posts.exists():
            return posts
        else:
            raise Http404


class PostDetailView(FormMixin, DetailView):
    """Вывод новости"""
    model = Post
    template_name = 'news/post_detail.html'
    form_class = CommentForm
    succes_url = '/'

    # def get(self, request, *args, **kwargs):
    #     HIT = self.request.path_info
    #     IP = self.request.META.get('REMOTE_ADDR')
    #     # используем кеш для хранения ПУТИ и ІР
    #     print('set PATH_HIT - ', cache.get_or_set(HIT, 0, 60 * 5), '\t PATH_IP - ', cache.get(IP))
    #     print(f'\n\t\tPATH_HIT={HIT}\n\t\tPATH_IP={IP}\n')
    #     # print(f'\n path={self.request.build_absolute_uri()}, IP={self.request.META.get("REMOTE_ADDR")}\n')
    #     if not cache.get(IP) or not cache.get(HIT):  # якщо ІР або НІТ не встановлені - Null(ed)
    #         cache.get_or_set(IP, self.request.META.get('REMOTE_ADDR'), 60)  # перевірить кеш-таймаут
    #         cache.set(HIT, cache.get(HIT) + 1)
    #     print(f"\n\tIP={cache.get(IP)}\tHIT={cache.get(HIT)}\n")
    #     print('PATH_HIT - ', cache.get(HIT), '\t PATH_IP - ', cache.get(IP))
    #     return super(PostDetailView, self).get(self, request, *args, **kwargs)

    def get_object(self, queryset=None):
        obj = super(PostDetailView, self).get_object(queryset)
        if obj.published:
            return obj
        else:
            raise Http404("Пост не найден!")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        # if not request.user.is_authenticated():
        #     return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            # return self.form_valid(form)
            print('\t\t\tform valid\n')
        else:
            # return self.form_invalid(form)
            print('\t\t\tform INvalid\n')

# class AddComment(View):
#     def get(self, request, *args, **kwargs):
#         print(f'args = {self.args}\nkwargs={self.kwargs}\n')
#         # x=PostList.get_queryset(self)
#         # print(f'x={x}\n')
#         pass
