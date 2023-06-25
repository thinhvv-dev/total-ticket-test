from django.db import models
from datetime import datetime


def create_increment_order_id_schema():
    current_date_str = datetime.now().date().strftime("%Y%m%d")
    prefix_order_id = current_date_str + "-"
    last_order = Orders.objects.filter(order_id__startswith=prefix_order_id).order_by("id").last()

    if not last_order:
        return prefix_order_id + "00001"
    last_order_id = last_order.order_id
    last_order_date, last_order_sequence = last_order_id.split("-")
    last_order_sequence_int = int(last_order_sequence)
    current_order_sequence = last_order_sequence_int + 1
    return prefix_order_id + '{0:0>5}'.format(current_order_sequence)


class Orders(models.Model):
    order_id = models.CharField(max_length=20, unique=True)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.order_id = create_increment_order_id_schema()
        super().save(*args, **kwargs)
