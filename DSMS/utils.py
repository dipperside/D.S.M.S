from django.utils.text import slugify


def unique_slug_generator(instance,  field):
    model = instance.__class__
    max_length = model._meta.get_field('slug').max_length
    slug = orig = slugify(field)[:max_length]

    numb = 1
    while model.objects.filter(slug=slug).exists():
        slug = "{}-{}".format(orig[:max_length - len(str(numb)) - 1], numb)
        numb += 1

    return slug