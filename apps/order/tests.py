from django.test import TestCase
from apps.order.repository import *
from unittest import mock
from datetime import datetime


class RepositoryTest(TestCase):

    @mock.patch('apps.order.models.datetime')
    def test_create_new_order(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2023, 6, 25, 0, 0, 0)
        order = order_create()
        self.assertEquals(order.order_id, "20230625-00001")

    @mock.patch('apps.order.models.datetime')
    def test_create_order_with_exist_data_in_table(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2023, 6, 25, 0, 0, 0)
        order = order_create()
        self.assertEquals(order.order_id, "20230625-00001")

        order = order_create()
        self.assertEquals(order.order_id, "20230625-00002")


class ModelTest(TestCase):
    @mock.patch('apps.order.models.datetime')
    def test_create_new_order(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2023, 6, 25, 0, 0, 0)
        order = Orders.objects.create()
        self.assertEquals(order.order_id, "20230625-00001")

    @mock.patch('apps.order.models.datetime')
    def test_create_order_with_exist_data_in_table(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2023, 6, 25, 0, 0, 0)
        order = Orders.objects.create()
        self.assertEquals(order.order_id, "20230625-00001")

        order = Orders.objects.create()
        self.assertEquals(order.order_id, "20230625-00002")

    @mock.patch('apps.order.models.datetime')
    def test_create_order_with_wrong_order_id(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2023, 6, 25, 0, 0, 0)
        order = Orders.objects.create()
        self.assertEquals(order.order_id, "20230625-00001")

        order = Orders.objects.create(order_id="20230625-00001")
        self.assertEquals(order.order_id, "20230625-00002")
