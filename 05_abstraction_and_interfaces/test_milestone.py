import unittest
from exercise import (
    PaymentProcessor,
    NotificationService,
    StripeProcessor,
    PayPalProcessor,
    CashProcessor,
    SMSNotifier,
    CheckoutService
)

class TestMilestone05(unittest.TestCase):
    def test_abstract_classes_cannot_be_instantiated(self):
        with self.assertRaises(TypeError):
            PaymentProcessor()
        with self.assertRaises(TypeError):
            NotificationService()

    def test_stripe_processor(self):
        stripe = StripeProcessor("sk_test_12345")
        res = stripe.process_payment(25.50)
        self.assertTrue(res["success"])
        self.assertEqual(res["provider"], "Stripe")
        self.assertEqual(res["amount"], 25.50)

    def test_paypal_processor(self):
        paypal = PayPalProcessor("customer@example.com")
        res = paypal.process_payment(18.00)
        self.assertTrue(res["success"])
        self.assertEqual(res["provider"], "PayPal")

    def test_cash_processor_sufficiency(self):
        cash_ok = CashProcessor(30.00)
        self.assertTrue(cash_ok.process_payment(25.00)["success"])

        cash_short = CashProcessor(15.00)
        self.assertFalse(cash_short.process_payment(25.00)["success"])

    def test_checkout_service_integration(self):
        notifier = SMSNotifier()
        stripe = StripeProcessor("sk_live_key")
        checkout = CheckoutService(payment_processor=stripe, notifier=notifier)

        success = checkout.checkout("+1234567890", 42.00)
        self.assertTrue(success)
        self.assertEqual(len(notifier.sent_messages), 1)
        self.assertIn("Stripe", notifier.sent_messages[0]["message"])

if __name__ == "__main__":
    unittest.main()

