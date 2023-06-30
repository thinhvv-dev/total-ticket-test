from django.forms.models import model_to_dict

from apps.order.models import Orders
from config.celery import app


@app.task(bind=True, ignore_result=False)
def order_create(request):
    order = Orders()
    order.save()
    return model_to_dict(order)
