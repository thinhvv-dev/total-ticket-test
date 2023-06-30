from celery.result import AsyncResult
from django.http import HttpResponse

from apps.order.repository import order_create


def create_order(request):
    res = order_create.delay()

    response = res.wait(timeout=5, interval=0.5)
    print("response.get()")
    print(res)
    return HttpResponse(res)
