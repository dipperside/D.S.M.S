import itertools

from django.db.models import Q
from django.utils.text import slugify


def unique_slug_generator(instance, model, field):
    max_length = model._meta.get_field('slug').max_length
    slug = orig = slugify(field)[:max_length]

    for x in itertools.count(1):
        if instance.id:
            if model.objects.filter(Q(slug=instance.slug), Q(author=instance.author), Q(id=instance.id),).exists():
                break
        if not model.objects.filter(slug=instance.slug).exists():
            break

        slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)

    return slug