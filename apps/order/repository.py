from apps.order.models import Orders

from celery import shared_task


@shared_task
def order_create():
    order = Orders()
    order.save()
    return order
