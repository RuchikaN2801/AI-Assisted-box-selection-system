from django.test import TestCase

from products.models import Product
from boxes.models import Box
from orders.models import Order, OrderItem
from services.box_selector import BoxSelector


class BoxSelectorTest(TestCase):

    def setUp(self):

        self.product = Product.objects.create(
            name="Laptop",
            length=30,
            width=20,
            height=5,
            weight=2
        )

    def test_cheapest_box_selected(self):

        Box.objects.create(
            name="Large Box",
            length=60,
            width=60,
            height=60,
            max_weight=20,
            cost=50
        )

        Box.objects.create(
            name="Small Box",
            length=35,
            width=25,
            height=10,
            max_weight=5,
            cost=20
        )

        order = Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=self.product,
            quantity=1
        )

        box = BoxSelector.recommend(order)

        self.assertEqual(box.name, "Small Box")

    def test_no_box_found(self):

        Box.objects.create(
            name="Tiny Box",
            length=10,
            width=10,
            height=10,
            max_weight=1,
            cost=10
        )

        order = Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=self.product,
            quantity=1
        )

        box = BoxSelector.recommend(order)

        self.assertIsNone(box)
        