from django.http import HttpResponse

from apps.order.repository import order_create


def create_order(request):
    order_create.apply_async()
    return HttpResponse("test")
