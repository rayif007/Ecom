from .models import Category


def my_links(request):
    links = Category.objects.all()
    return dict(links=links)
