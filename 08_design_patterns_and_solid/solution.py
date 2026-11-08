"""Milestone 08 Reference Solution."""

from abc import ABC, abstractmethod
from typing import List

# =====================================================================
# 1. STRATEGY PATTERN: Discounts
# =====================================================================

class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_discount(self, subtotal: float) -> float:
        pass


class NoDiscount(DiscountStrategy):
    def calculate_discount(self, subtotal: float) -> float:
        return 0.0


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: float):
        if not (0 <= percent <= 100):
            raise ValueError("Percentage must be between 0 and 100")
        self.percent = float(percent)

    def calculate_discount(self, subtotal: float) -> float:
        return (subtotal * self.percent) / 100.0


class FlatDiscount(DiscountStrategy):
    def __init__(self, amount: float):
        if amount < 0:
            raise ValueError("Discount amount cannot be negative")
        self.amount = float(amount)

    def calculate_discount(self, subtotal: float) -> float:
        return min(self.amount, subtotal)


# =====================================================================
# 2. OBSERVER PATTERN: Status Alerts
# =====================================================================

class OrderObserver(ABC):
    @abstractmethod
    def update(self, order_id: int, new_status: str) -> None:
        pass


class KitchenDisplay(OrderObserver):
    def __init__(self):
        self.active_tickets: List[int] = []

    def update(self, order_id: int, new_status: str) -> None:
        if new_status == "PREPARING":
            if order_id not in self.active_tickets:
                self.active_tickets.append(order_id)
        elif new_status in ("READY", "DELIVERED"):
            if order_id in self.active_tickets:
                self.active_tickets.remove(order_id)


class CustomerAlertObserver(OrderObserver):
    def __init__(self, customer_name: str):
        self.customer_name = customer_name
        self.notifications: List[str] = []

    def update(self, order_id: int, new_status: str) -> None:
        self.notifications.append(
            f"Hello {self.customer_name}, Order #{order_id} is now {new_status}!"
        )


class OrderSubject:
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
        self.status = new_status
        self.notify_observers()

    def get_final_total(self) -> float:
        discount = self.discount_strategy.calculate_discount(self.subtotal)
        return max(0.0, self.subtotal - discount)

