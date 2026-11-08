import unittest
from berrys_pizzeria import (
    Crust, Sauce, Topping, Pizza, Beverage,
    PercentageDiscount, KitchenDisplay, CustomerSMSNotifier,
    MockCardProcessor, Order
)

class TestCapstone(unittest.TestCase):
    def test_complete_capstone_flow(self):
        order = Order(order_id=999, customer_name="Sam", discount=PercentageDiscount(10))
        kitchen = KitchenDisplay()
        order.attach_observer(kitchen)

        pizza = Pizza.margherita("medium")
        coke = Beverage("Coke", 2.0, 16)
        order.add_item(pizza)
        order.add_item(coke)

        self.assertEqual(len(order), 2)
        subtotal = pizza.get_price() + coke.get_price()
        self.assertAlmostEqual(order.get_subtotal(), subtotal)
        self.assertAlmostEqual(order.get_final_total(), subtotal * 0.90)

        # Status flow
        order.transition_to("CONFIRMED")
        order.transition_to("PREPARING")
        self.assertIn(999, kitchen.active_orders)

        order.transition_to("READY")
        self.assertNotIn(999, kitchen.active_orders)

        order.transition_to("DELIVERED")
        self.assertEqual(order.status, "DELIVERED")

if __name__ == "__main__":
    unittest.main()
