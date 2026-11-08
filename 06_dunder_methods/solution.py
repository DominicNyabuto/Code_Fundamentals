"""Milestone 06 Reference Solution."""

from typing import List, Any

class Pizza:
    def __init__(self, name: str, size: str, price: float):
        self.name = name
        self.size = size.lower()
        self.price = float(price)

    def __repr__(self) -> str:
        return f"Pizza(name='{self.name}', size='{self.size}', price={self.price})"

    def __str__(self) -> str:
        return f"{self.size.title()} {self.name} (${self.price:.2f})"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Pizza):
            return False
        return (
            self.name == other.name and
            self.size == other.size and
            self.price == other.price
        )


class PizzeriaOrder:
    def __init__(self, customer_name: str, items: List[Pizza] = None):
        self.customer_name = customer_name
        self.items: List[Pizza] = list(items) if items else []

    def add_item(self, pizza: Pizza) -> None:
        self.items.append(pizza)

    def __len__(self) -> int:
        return len(self.items)

    def __getitem__(self, index: int) -> Pizza:
        return self.items[index]

    def __iter__(self):
        return iter(self.items)

    def __add__(self, other: "PizzeriaOrder") -> "PizzeriaOrder":
        if not isinstance(other, PizzeriaOrder):
            raise TypeError("Can only add another PizzeriaOrder")
        merged_customer = f"{self.customer_name} & {other.customer_name}"
        merged_items = self.items + other.items
        return PizzeriaOrder(merged_customer, merged_items)

    def __repr__(self) -> str:
        return f"PizzeriaOrder(customer='{self.customer_name}', items_count={len(self)})"
