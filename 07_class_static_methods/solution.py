"""Milestone 07 Reference Solution."""

from typing import List, Dict, Any
import re

class Pizza:
    BASE_PRICES = {"small": 8.0, "medium": 10.0, "large": 12.0}

    def __init__(self, name: str, size: str, price: float, toppings: List[str]):
        self.name = name
        self.size = size.lower()
        self.price = float(price)
        self.toppings = list(toppings)

    @staticmethod
    def validate_size(size: str) -> bool:
        return str(size).lower() in ("small", "medium", "large")

    @classmethod
    def margherita(cls, size: str = "medium") -> "Pizza":
        if not cls.validate_size(size):
            raise ValueError(f"Invalid size: {size}")
        size = size.lower()
        price = cls.BASE_PRICES[size] + 2.0
        return cls("Margherita", size, price, ["tomato sauce", "fresh mozzarella", "basil"])

    @classmethod
    def pepperoni_feast(cls, size: str = "large") -> "Pizza":
        if not cls.validate_size(size):
            raise ValueError(f"Invalid size: {size}")
        size = size.lower()
        price = cls.BASE_PRICES[size] + 4.5
        return cls("Pepperoni Feast", size, price, ["tomato sauce", "mozzarella", "double pepperoni"])

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Pizza":
        for key in ("name", "size", "price", "toppings"):
            if key not in data:
                raise KeyError(f"Missing required key: {key}")
        return cls(
            name=data["name"],
            size=data["size"],
            price=float(data["price"]),
            toppings=list(data["toppings"])
        )


class OrderValidator:
    @staticmethod
    def is_valid_phone(phone: str) -> bool:
        digits_only = re.sub(r"\D", "", phone)
        return len(digits_only) == 10

