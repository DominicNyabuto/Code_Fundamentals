"""Milestone 05 Exercise: Abstraction & Interfaces using Python ABCs.

Instructions:
1. Define abstract base class `PaymentProcessor` with abstract method `process_payment(amount: float) -> dict`.
2. Define abstract base class `NotificationService` with abstract method `notify(recipient: str, message: str) -> bool`.
3. Implement concrete classes:
   - StripeProcessor
   - PayPalProcessor
   - CashProcessor
   - SMSNotifier
4. Implement `CheckoutService` that coordinates payment and notification.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any

class PaymentProcessor(ABC):
    """Abstract interface for all payment providers."""

    @abstractmethod
    def process_payment(self, amount: float) -> Dict[str, Any]:
        """Process a payment.
        Must return a dict: {"success": bool, "transaction_id": str, "provider": str, "amount": float}
        """
        pass


class NotificationService(ABC):
    """Abstract interface for order alerts."""

    @abstractmethod
    def notify(self, recipient: str, message: str) -> bool:
        """Send notification. Return True if sent successfully."""
        pass


class StripeProcessor(PaymentProcessor):
    def __init__(self, api_key: str):
        self.api_key = api_key

    def process_payment(self, amount: float) -> Dict[str, Any]:
        """Simulate Stripe payment processing.
        If amount <= 0, return success: False.
        Otherwise, return success: True, transaction_id: f"stripe_tx_{int(amount * 100)}",
        provider: "Stripe", amount: amount.
        """
        # TODO: Implement process_payment
        pass


class PayPalProcessor(PaymentProcessor):
    def __init__(self, account_email: str):
        self.account_email = account_email

    def process_payment(self, amount: float) -> Dict[str, Any]:
        """Simulate PayPal payment processing.
        If amount <= 0, return success: False.
        Otherwise, return success: True, transaction_id: f"pp_tx_{self.account_email[:3]}",
        provider: "PayPal", amount: amount.
        """
        # TODO: Implement process_payment
        pass


class CashProcessor(PaymentProcessor):
    def __init__(self, cash_tendered: float):
        self.cash_tendered = float(cash_tendered)

    def process_payment(self, amount: float) -> Dict[str, Any]:
        """Check if cash_tendered is >= amount.
        If yes: success: True, transaction_id: "cash_on_delivery",
        provider: "Cash", amount: amount.
        If no: success: False, transaction_id: "insufficient_cash",
        provider: "Cash", amount: amount.
        """
        # TODO: Implement process_payment
        pass


class SMSNotifier(NotificationService):
    def __init__(self, sender_id: str = "BerrysPizza"):
        self.sender_id = sender_id
        self.sent_messages = []

    def notify(self, recipient: str, message: str) -> bool:
        """Store (recipient, message) in self.sent_messages and return True."""
        # TODO: Implement notify
        pass


class CheckoutService:
    """Demonstrates high-level business logic depending ONLY on abstractions,
    not on concrete implementations! (Dependency Inversion Principle).
    """
    def __init__(self, payment_processor: PaymentProcessor, notifier: NotificationService):
        self.payment_processor = payment_processor
        self.notifier = notifier

    def checkout(self, customer_phone: str, amount: float) -> bool:
        """1. Charge the amount using self.payment_processor.
        2. If payment succeeds, send confirmation SMS via self.notifier and return True.
        3. If payment fails, return False.
        """
        # TODO: Implement checkout
        pass

