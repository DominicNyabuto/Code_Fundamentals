import unittest
from exercise import CashRegister, TrackedOrder, InsufficientFundsError, InvalidStateTransitionError

class TestMilestone02(unittest.TestCase):
    def test_cash_register_encapsulation(self):
        reg = CashRegister(150.0)
        self.assertEqual(reg.balance, 150.0)

        # Confirm __balance is private (name-mangled)
        self.assertFalse(hasattr(reg, "balance_value"))
        self.assertTrue(hasattr(reg, "_CashRegister__balance"))

        # Cannot set balance directly
        with self.assertRaises(AttributeError):
            reg.balance = 10000.0  # read-only property

    def test_deposit_and_withdrawal(self):
        reg = CashRegister(100.0)
        reg.deposit(50.0)
        self.assertEqual(reg.balance, 150.0)

        with self.assertRaises(ValueError):
            reg.deposit(-10.0)

        with self.assertRaises(ValueError):
            reg.deposit(0)

        with self.assertRaises(ValueError):
            reg.withdraw(-5.0)

        cash = reg.withdraw(50.0)
        self.assertEqual(cash, 50.0)
        self.assertEqual(reg.balance, 100.0)

        with self.assertRaises(InsufficientFundsError):
            reg.withdraw(200.0)

    def test_order_status_valid_flow(self):
        order = TrackedOrder(101)
        self.assertEqual(order.status, "DRAFT")

        order.transition_to("CONFIRMED")
        self.assertEqual(order.status, "CONFIRMED")

        order.transition_to("PREPARING")
        self.assertEqual(order.status, "PREPARING")

        order.transition_to("OUT_FOR_DELIVERY")
        self.assertEqual(order.status, "OUT_FOR_DELIVERY")

        order.transition_to("DELIVERED")
        self.assertEqual(order.status, "DELIVERED")

    def test_order_status_invalid_flow(self):
        order = TrackedOrder(102)
        # Cannot jump from DRAFT straight to DELIVERED
        with self.assertRaises(InvalidStateTransitionError):
            order.transition_to("DELIVERED")

        # After DELIVERED, cannot transition anymore
        order.transition_to("CONFIRMED")
        order.transition_to("PREPARING")
        order.transition_to("OUT_FOR_DELIVERY")
        order.transition_to("DELIVERED")

        with self.assertRaises(InvalidStateTransitionError):
            order.transition_to("CANCELLED")

if __name__ == "__main__":
    unittest.main()

