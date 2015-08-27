from lik.models import Category


def get_menu_items(request):
    categories = Category.objects.order_by('name').order_by('order').all()
    return dict(menu_items=categories)
