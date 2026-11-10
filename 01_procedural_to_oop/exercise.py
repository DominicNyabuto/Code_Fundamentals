"""Milestone 01 Exercise: Transform Procedural Pizza Code into Classes & Objects.

Instructions:
1. Complete the `Pizza` class with its attributes, `add_topping`, and `calculate_price` methods.
2. Complete the `CustomerOrder` class that aggregates multiple pizzas for a customer.
3. Validate by running `python3 test_milestone.py`.
"""

from typing import List
        # Imports List from Python’s typing module. It is used to write type hints such as
        # List[str], meaning “a list containing strings.” Type hints document intent and 
        # can help tools such as IDEs and type checkers; Python itself does not automatically 
        # enforce them.

class Pizza:
    """
    Class for a customizable Pizza.
        - `class Pizza` - Defines a new class called Pizza. 
        - You can create pizza objects from it, 
            - e.g Pizza("large", "thin") makes a large pizza with thin crust.

    Attributes:
        - size - The size of the pizza. Must be one of "small", "medium", or "large”.
        - crust - The type of crust (e.g., "thin", "stuffed").
        - toppings - A list of toppings on the pizza.
    
    Class variables:
        - SIZE_PRICES - A dictionary mapping each size to its base price.
        - TOPPING_PRICE - The price of a single topping.
    """

    SIZE_PRICES = {
        "small": 8.0,
        "medium": 10.0,
        "large": 12.0
    }
    TOPPING_PRICE = 1.50

    def __init__(self, size: str, crust: str):
        """
        Initialize pizza with a size and crust type.
            - Size should be converted to lower-case.
            - Validate that size is one of: "small", "medium", "large".
            - If invalid, raise ValueError("Invalid pizza size").
            - Crust should be lower-case string.
            - Initialize an empty list of toppings.
        """
        # TODO: Implement __init__
        size = size.lower()
        if size not in self.SIZE_PRICES:
            raise ValueError(f"Invalid pizza size. Must be 'small', 'medium', or 'large'")

        self.size = size
        self.crust = crust.lower()
        self.toppings: List[str] = []



        pass

    def add_topping(self, topping: str) -> None: # -> None - The method does an action and returns nothing.
        """Add a lower-case topping string to self.toppings."""
        # TODO: Implement add_topping
        self.toppings.append(topping.lower())

        pass

    def calculate_price(self) -> float:
        """Calculate total price: base size price + (number of toppings * TOPPING_PRICE)."""
        # TODO: Implement calculate_price
        base_size_price = self.SIZE_PRICES[self.size]
        toppings_price = len(self.toppings) * self.TOPPING_PRICE
        return  base_size_price + toppings_price

        pass

    def get_description(self) -> str:
        """Return formatted description string.
        Format:
        '{size} pizza with {crust} crust topped with: {comma separated toppings or 'Cheese Only'}'
        Example: 'large pizza with thin crust topped with: mushrooms, olives'
        Example (no toppings): 'small pizza with stuffed crust topped with: Cheese Only'
        """
        # TODO: Implement get_description
        toppings_list = ", ".join(self.toppings) if self.toppings else "No Toppings"
        return f"{self.size} pizza with {self.crust} crust topped with: {toppings_list}"
        pass


class CustomerOrder:
    """Represents a customer's total order containing one or more pizzas."""

    def __init__(self, customer_name: str):
        """Initialize with customer name and an empty list of pizzas."""
        # TODO: Implement __init__
        self.customer_name = customer_name
        self.pizzas: List[Pizza] = []
        
        pass

    def add_pizza(self, pizza: Pizza) -> None:
        """Add a Pizza instance to this order.
        If the passed object is not an instance of Pizza, raise TypeError("Item must be a Pizza").
        """
        # TODO: Implement add_pizza
        if not isinstance(pizza, Pizza):
            raise TypeError("Item must be a Pizza")
        
        self.pizzas.append(pizza)
        pass

    def calculate_total(self) -> float:
        """Sum up the prices of all pizzas in the order."""
        # TODO: Implement calculate_total
        return sum(pizza.calculate_price() for pizza in self.pizzas)
        pass

