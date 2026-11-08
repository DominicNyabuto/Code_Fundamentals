"""Milestone 08 Exercise: Strategy & Observer Design Patterns in Berry's Pizza.

Implement:
1. Strategy Pattern for Discounts:
   - DiscountStrategy (ABC)
   - NoDiscount
   - PercentageDiscount
   - FlatDiscount
2. Observer Pattern for Order Status Updates:
   - OrderObserver (ABC)
   - KitchenDisplay
   - CustomerAlertObserver
   - OrderSubject (Subject/Observable)
"""

from abc import ABC, abstractmethod
from typing import List

# =====================================================================
# 1. STRATEGY PATTERN: Discounts
# =====================================================================

class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_discount(self, subtotal: float) -> float:
        """Calculate discount amount to subtract from subtotal.
        Discount should never exceed subtotal, and cannot be negative.
        """
        pass


class NoDiscount(DiscountStrategy):
    def calculate_discount(self, subtotal: float) -> float:
        return 0.0


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: float):
        """percent should be between 0 and 100.
        If not, raise ValueError("Percentage must be between 0 and 100").
        """
        # TODO: Implement __init__
        pass

    def calculate_discount(self, subtotal: float) -> float:
        """Return (subtotal * percent) / 100."""
        # TODO: Implement calculate_discount
        pass


class FlatDiscount(DiscountStrategy):
    def __init__(self, amount: float):
        if amount < 0:
            raise ValueError("Discount amount cannot be negative")
        self.amount = float(amount)

    def calculate_discount(self, subtotal: float) -> float:
        """Return min(self.amount, subtotal)."""
        # TODO: Implement calculate_discount
        pass


# =====================================================================
# 2. OBSERVER PATTERN: Status Alerts
# =====================================================================

class OrderObserver(ABC):
    @abstractmethod
    def update(self, order_id: int, new_status: str) -> None:
        """Called whenever the observed order changes status."""
        pass


class KitchenDisplay(OrderObserver):
    def __init__(self):
        self.active_tickets = []

    def update(self, order_id: int, new_status: str) -> None:
        """If new_status is 'PREPARING', add order_id to self.active_tickets.
        If new_status is 'READY' or 'DELIVERED', remove order_id from active_tickets (if present).
        """
        # TODO: Implement update
        pass


class CustomerAlertObserver(OrderObserver):
    def __init__(self, customer_name: str):
        self.customer_name = customer_name
        self.notifications = []

    def update(self, order_id: int, new_status: str) -> None:
        """Append f"Hello {self.customer_name}, Order #{order_id} is now {new_status}!"
        to self.notifications.
        """
        # TODO: Implement update
        pass


class OrderSubject:
    """The Subject being observed (Order)."""

    def __init__(self, order_id: int, subtotal: float, discount_strategy: DiscountStrategy = None):
        self.order_id = order_id
        self.subtotal = float(subtotal)
        self.discount_strategy = discount_strategy or NoDiscount()
        self.status = "DRAFT"
        self._observers: List[OrderObserver] = []

    def attach_observer(self, observer: OrderObserver) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach_observer(self, observer: OrderObserver) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self.order_id, self.status)

    def set_status(self, new_status: str) -> None:
        """Update self.status to new_status and notify all attached observers."""
        # TODO: Implement set_status
        pass

    def get_final_total(self) -> float:
        """Calculate final total: subtotal - discount_strategy.calculate_discount(subtotal)."""
        # TODO: Implement get_final_total
        pass

