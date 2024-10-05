from django.test import TestCase

from .models import Order


class OrderTest(TestCase):
    def test_order_discount(self):
        order = Order.objects.create(quantity=10, price_per_item=5.00)

        # testing if we acually do 10% discount
        # avoid being sloppy and apply 90% discout by mistake
        self.assertEqual(order.calculate_total(), 45)

