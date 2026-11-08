"""Milestone 05 Reference Solution."""

from abc import ABC, abstractmethod
from typing import Dict, Any

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> Dict[str, Any]:
        pass


class NotificationService(ABC):
    @abstractmethod
    def notify(self, recipient: str, message: str) -> bool:
        pass


class StripeProcessor(PaymentProcessor):
    def __init__(self, api_key: str):
        self.api_key = api_key

    def process_payment(self, amount: float) -> Dict[str, Any]:
        if amount <= 0:
            return {"success": False, "transaction_id": "", "provider": "Stripe", "amount": amount}
        return {
            "success": True,
            "transaction_id": f"stripe_tx_{int(amount * 100)}",
            "provider": "Stripe",
            "amount": amount
        }


class PayPalProcessor(PaymentProcessor):
    def __init__(self, account_email: str):
        self.account_email = account_email

    def process_payment(self, amount: float) -> Dict[str, Any]:
        if amount <= 0:
            return {"success": False, "transaction_id": "", "provider": "PayPal", "amount": amount}
        return {
            "success": True,
            "transaction_id": f"pp_tx_{self.account_email[:3]}",
            "provider": "PayPal",
            "amount": amount
        }


class CashProcessor(PaymentProcessor):
    def __init__(self, cash_tendered: float):
        self.cash_tendered = float(cash_tendered)

    def process_payment(self, amount: float) -> Dict[str, Any]:
        if self.cash_tendered >= amount and amount > 0:
            return {
                "success": True,
                "transaction_id": "cash_on_delivery",
                "provider": "Cash",
                "amount": amount
            }
        return {
            "success": False,
            "transaction_id": "insufficient_cash",
            "provider": "Cash",
            "amount": amount
        }


class SMSNotifier(NotificationService):
    def __init__(self, sender_id: str = "BerrysPizza"):
        self.sender_id = sender_id
        self.sent_messages = []

    def notify(self, recipient: str, message: str) -> bool:
        self.sent_messages.append({"to": recipient, "message": message})
        return True


class CheckoutService:
    def __init__(self, payment_processor: PaymentProcessor, notifier: NotificationService):
        self.payment_processor = payment_processor
        self.notifier = notifier

    def checkout(self, customer_phone: str, amount: float) -> bool:
        result = self.payment_processor.process_payment(amount)
        if result.get("success"):
            self.notifier.notify(
                customer_phone,
                f"Your order of ${amount:.2f} has been paid via {result.get('provider')}!"
            )
            return True
        return False
