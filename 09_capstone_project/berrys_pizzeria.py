#!/usr/bin/env python3
"""Berry's Pizzeria - Full Object-Oriented Capstone Application.

Demonstrating:
- Classes & Objects
- Encapsulation & Properties
- Inheritance & Composition
- Polymorphism & Duck Typing
- Abstraction & Interfaces (ABCs)
- Dunder Methods (__repr__, __str__, __len__, __iter__)
- Classmethods & Factory Patterns
- Design Patterns (Strategy & Observer)
- SOLID Principles
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional

# =====================================================================
# 1. DOMAIN MODELS (Composition & Inheritance)
# =====================================================================

class Crust:
    def __init__(self, name: str, extra_cost: float = 0.0):
        self.name = name
        self.extra_cost = float(extra_cost)


class Sauce:
    def __init__(self, name: str, is_spicy: bool = False):
        self.name = name
        self.is_spicy = is_spicy


class Topping:
    def __init__(self, name: str, price: float = 1.50):
        self.name = name
        self.price = float(price)


class MenuItem(ABC):
    """Abstract interface / base class for all catalog items (Polymorphism)."""
    def __init__(self, name: str, base_price: float):
        self.name = name
        self.base_price = float(base_price)

    @abstractmethod
    def get_price(self) -> float:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass


class Pizza(MenuItem):
    """Pizza IS-A MenuItem, and HAS-A Crust, Sauce, and Toppings (Composition)."""

    BASE_PRICES = {"small": 8.0, "medium": 10.0, "large": 12.0}

    def __init__(self, name: str, size: str, crust: Crust, sauce: Sauce, base_price: float = None):
        size = size.lower()
        if size not in self.BASE_PRICES:
            raise ValueError(f"Invalid pizza size: {size}")
        computed_base = base_price if base_price is not None else self.BASE_PRICES[size]
        super().__init__(name, computed_base)
        self.size = size
        self.crust = crust
        self.sauce = sauce
        self.toppings: List[Topping] = []

    def add_topping(self, topping: Topping) -> None:
        if not isinstance(topping, Topping):
            raise TypeError("Must be a Topping instance")
        self.toppings.append(topping)

    def get_price(self) -> float:
        toppings_cost = sum(t.price for t in self.toppings)
        return self.base_price + self.crust.extra_cost + toppings_cost

    def get_description(self) -> str:
        topping_names = ", ".join(t.name for t in self.toppings) if self.toppings else "Plain Cheese"
        return f"{self.size.title()} {self.name} [{self.crust.name}, {self.sauce.name}] topped with: {topping_names}"

    # Factory Constructors (@classmethod)
    @classmethod
    def margherita(cls, size: str = "medium") -> "Pizza":
        p = cls("Margherita", size, Crust("Hand Tossed"), Sauce("San Marzano Tomato"))
        p.add_topping(Topping("Fresh Mozzarella", 2.0))
        p.add_topping(Topping("Fresh Basil", 1.0))
        return p

    @classmethod
    def pepperoni(cls, size: str = "large") -> "Pizza":
        p = cls("Pepperoni Classic", size, Crust("Thin Crust"), Sauce("Classic Red"))
        p.add_topping(Topping("Pepperoni", 2.50))
        return p

    def __str__(self) -> str:
        return f"{self.get_description()} - ${self.get_price():.2f}"

    def __repr__(self) -> str:
        return f"Pizza(name='{self.name}', size='{self.size}', price={self.get_price():.2f})"


class Beverage(MenuItem):
    def __init__(self, name: str, base_price: float, size_oz: int):
        super().__init__(name, base_price)
        self.size_oz = size_oz

    def get_price(self) -> float:
        return self.base_price

    def get_description(self) -> str:
        return f"{self.name} ({self.size_oz} oz)"

    def __str__(self) -> str:
        return f"{self.get_description()} - ${self.get_price():.2f}"


# =====================================================================
# 2. STRATEGY PATTERN: Discounts
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


# =====================================================================
# 3. OBSERVER PATTERN: Status Broadcast
# =====================================================================

class OrderObserver(ABC):
    @abstractmethod
    def update(self, order_id: int, new_status: str) -> None:
        pass


class KitchenDisplay(OrderObserver):
    def __init__(self):
        self.active_orders = []

    def update(self, order_id: int, new_status: str) -> None:
        if new_status == "PREPARING":
            self.active_orders.append(order_id)
            print(f"👨‍🍳 [KITCHEN DISPLAY] Order #{order_id} added to the baking queue!")
        elif new_status in ("READY", "DELIVERED"):
            if order_id in self.active_orders:
                self.active_orders.remove(order_id)
            print(f"👨‍🍳 [KITCHEN DISPLAY] Order #{order_id} completed and cleared.")


class CustomerSMSNotifier(OrderObserver):
    def __init__(self, customer_phone: str):
        self.customer_phone = customer_phone

    def update(self, order_id: int, new_status: str) -> None:
        print(f"📱 [SMS to {self.customer_phone}] Berry's Pizza: Order #{order_id} is now {new_status}!")


# =====================================================================
# 4. ENCAPSULATED ORDER & PAYMENT ABSTRACTION
# =====================================================================

class PaymentProcessor(ABC):
    @abstractmethod
    def process(self, amount: float) -> bool:
        pass


class MockCardProcessor(PaymentProcessor):
    def process(self, amount: float) -> bool:
        print(f"💳 [CARD PROCESSOR] Successfully authorized ${amount:.2f}")
        return True


class Order:
    """Encapsulates items, status workflow, and observers."""

    VALID_TRANSITIONS = {
        "DRAFT": ["CONFIRMED", "CANCELLED"],
        "CONFIRMED": ["PREPARING", "CANCELLED"],
        "PREPARING": ["READY"],
        "READY": ["DELIVERED"],
        "DELIVERED": [],
        "CANCELLED": []
    }

    def __init__(self, order_id: int, customer_name: str, discount: Optional[DiscountStrategy] = None):
        self._order_id = order_id
        self.customer_name = customer_name
        self.__status = "DRAFT"
        self.discount_strategy = discount or NoDiscount()
        self._items: List[MenuItem] = []
        self._observers: List[OrderObserver] = []

    @property
    def order_id(self) -> int:
        return self._order_id

    @property
    def status(self) -> str:
        return self.__status

    def add_item(self, item: MenuItem) -> None:
        if not isinstance(item, MenuItem):
            raise TypeError("Item must be a MenuItem")
        self._items.append(item)

    def attach_observer(self, obs: OrderObserver) -> None:
        self._observers.append(obs)

    def transition_to(self, new_status: str) -> None:
        new_status = new_status.upper()
        if new_status not in self.VALID_TRANSITIONS.get(self.__status, []):
            raise ValueError(f"Illegal transition from {self.__status} to {new_status}")
        self.__status = new_status
        for obs in self._observers:
            obs.update(self._order_id, self.__status)

    def get_subtotal(self) -> float:
        return sum(item.get_price() for item in self._items)

    def get_final_total(self) -> float:
        subtotal = self.get_subtotal()
        disc = self.discount_strategy.calculate_discount(subtotal)
        return max(0.0, subtotal - disc)

    # Dunder methods
    def __len__(self) -> int:
        return len(self._items)

    def __getitem__(self, index: int) -> MenuItem:
        return self._items[index]

    def __iter__(self):
        return iter(self._items)


# =====================================================================
# DEMO EXECUTION
# =====================================================================

def run_demo():
    print("=" * 65)
    print("🍕 WELCOME TO BERRY'S PIZZERIA OOP CAPSTONE DEMO")
    print("=" * 65)

    # 1. Create Order with a 15% VIP discount strategy
    order = Order(order_id=402, customer_name="Alice Johnson", discount=PercentageDiscount(15))

    # 2. Attach Observers (Kitchen display and Customer SMS)
    kitchen = KitchenDisplay()
    customer_sms = CustomerSMSNotifier("+1-555-0199")
    order.attach_observer(kitchen)
    order.attach_observer(customer_sms)

    # 3. Add items polymorphically
    # Using Factory method
    margherita = Pizza.margherita(size="medium")
    pepperoni = Pizza.pepperoni(size="large")
    # Adding a custom drink
    cola = Beverage("Craft Mexican Coke", base_price=3.50, size_oz=12)

    order.add_item(margherita)
    order.add_item(pepperoni)
    order.add_item(cola)

    # 4. Display Order Summary via Dunder Methods
    print(f"\nOrder for {order.customer_name} ({len(order)} items):")
    for item in order:
        print(f"  • {item}")

    subtotal = order.get_subtotal()
    final_total = order.get_final_total()
    print(f"\nSubtotal: ${subtotal:.2f}")
    print(f"After VIP Discount (15%): ${final_total:.2f}")

    # 5. Process Payment
    card_processor = MockCardProcessor()
    payment_ok = card_processor.process(final_total)

    if payment_ok:
        print("\n--- Moving Order through Status Workflow ---")
        order.transition_to("CONFIRMED")
        order.transition_to("PREPARING")
        order.transition_to("READY")
        order.transition_to("DELIVERED")

    print("\n🎉 Capstone demonstration completed successfully!")

if __name__ == "__main__":
    run_demo()
