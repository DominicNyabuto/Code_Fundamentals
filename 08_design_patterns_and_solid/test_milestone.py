import unittest
from exercise import (
    DiscountStrategy,
    NoDiscount,
    PercentageDiscount,
    FlatDiscount,
    KitchenDisplay,
    CustomerAlertObserver,
    OrderSubject
)

class TestMilestone08(unittest.TestCase):
    def test_discount_strategies(self):
        no_disc = NoDiscount()
        self.assertEqual(no_disc.calculate_discount(50.0), 0.0)

        pct_disc = PercentageDiscount(20)
        self.assertEqual(pct_disc.calculate_discount(50.0), 10.0)

        with self.assertRaises(ValueError):
            PercentageDiscount(120)

        flat_disc = FlatDiscount(15.0)
        self.assertEqual(flat_disc.calculate_discount(50.0), 15.0)
        # Cap at subtotal
        self.assertEqual(flat_disc.calculate_discount(10.0), 10.0)

    def test_order_final_total_with_strategy(self):
        order = OrderSubject(101, subtotal=40.0, discount_strategy=PercentageDiscount(25))
        self.assertAlmostEqual(order.get_final_total(), 30.0)

    def test_observer_pattern_dispatch(self):
        kitchen = KitchenDisplay()
        customer = CustomerAlertObserver("Dave")

        order = OrderSubject(505, subtotal=20.0)
        order.attach_observer(kitchen)
        order.attach_observer(customer)

        # Transition to PREPARING
        order.set_status("PREPARING")
        self.assertIn(505, kitchen.active_tickets)
        self.assertEqual(len(customer.notifications), 1)
        self.assertIn("is now PREPARING", customer.notifications[0])

        # Transition to DELIVERED
        order.set_status("DELIVERED")
        self.assertNotIn(505, kitchen.active_tickets)
        self.assertEqual(len(customer.notifications), 2)
        self.assertIn("is now DELIVERED", customer.notifications[1])

if __name__ == "__main__":
    unittest.main()

