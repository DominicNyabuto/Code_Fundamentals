"""Milestone 07 Exercise: Class Methods, Static Methods & Factory Constructors.

Implement:
1. Factory constructors on Pizza:
   - Pizza.margherita(size)
   - Pizza.pepperoni_feast(size)
   - Pizza.from_dict(payload)
2. Static validator methods:
   - Pizza.validate_size(size)
   - OrderValidator.is_valid_phone(phone_str)
"""

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
        """Return True if size is 'small', 'medium', or 'large' (case-insensitive)."""
        # TODO: Implement validate_size
        pass

    @classmethod
    def margherita(cls, size: str = "medium") -> "Pizza":
        """Factory method to construct a Margherita pizza.
        Toppings: ['tomato sauce', 'fresh mozzarella', 'basil']
        Price: base price for that size + 2.0
        Validate size first; raise ValueError("Invalid size") if invalid.
        """
        # TODO: Implement margherita factory
        pass

    @classmethod
    def pepperoni_feast(cls, size: str = "large") -> "Pizza":
        """Factory method to construct a Pepperoni Feast pizza.
        Toppings: ['tomato sauce', 'mozzarella', 'double pepperoni']
        Price: base price for that size + 4.5
        Validate size first; raise ValueError("Invalid size") if invalid.
        """
        # TODO: Implement pepperoni_feast factory
        pass

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Pizza":
        """Construct Pizza from a dictionary payload.
        Expected keys: 'name', 'size', 'price', 'toppings'
        Raise KeyError if any of these required keys are missing.
        """
        # TODO: Implement from_dict factory
        pass


class OrderValidator:
    """Namespace for helper validation logic."""

    @staticmethod
    def is_valid_phone(phone: str) -> bool:
        """Validate 10-digit phone number, ignoring dashes, spaces, and parentheses.
        e.g. '555-123-4567' -> True, '(555) 1234567' -> True, '123' -> False
        """
        # TODO: Implement is_valid_phone
        pass
