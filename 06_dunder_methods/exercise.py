"""Milestone 06 Exercise: Pythonic Dunder Methods in Berry's Pizza.

Implement:
1. Pizza: __repr__, __str__, __eq__
2. PizzeriaOrder: __len__, __getitem__, __iter__, __add__, __repr__
"""

from typing import List, Any

class Pizza:
    def __init__(self, name: str, size: str, price: float):
        self.name = name
        self.size = size.lower()
        self.price = float(price)

    def __repr__(self) -> str:
        """Return: Pizza(name='{self.name}', size='{self.size}', price={self.price})"""
        # TODO: Implement __repr__
        pass

    def __str__(self) -> str:
        """Return user-friendly: '{self.size.title()} {self.name} (${self.price:.2f})'"""
        # TODO: Implement __str__
        pass

    def __eq__(self, other: Any) -> bool:
        """Return True if other is a Pizza and has matching name, size, and price."""
        # TODO: Implement __eq__
        pass


class PizzeriaOrder:
    def __init__(self, customer_name: str, items: List[Pizza] = None):
        self.customer_name = customer_name
        self.items: List[Pizza] = list(items) if items else []

    def add_item(self, pizza: Pizza) -> None:
        self.items.append(pizza)

    def __len__(self) -> int:
        """Returns the number of pizzas in this order."""
        # TODO: Implement __len__
        pass

    def __getitem__(self, index: int) -> Pizza:
        """Allows indexing into items, e.g. order[0]."""
        # TODO: Implement __getitem__
        pass

    def __iter__(self):
        """Allows iterating through pizzas, e.g. for pizza in order:"""
        # TODO: Implement __iter__
        pass

    def __add__(self, other: "PizzeriaOrder") -> "PizzeriaOrder":
        """Merge this order and another order.
        Customer name becomes '{self.customer_name} & {other.customer_name}'.
        Items is the combined list of both orders' items.
        If other is not a PizzeriaOrder, raise TypeError.
        """
        # TODO: Implement __add__
        pass

    def __repr__(self) -> str:
        return f"PizzeriaOrder(customer='{self.customer_name}', items_count={len(self)})"

