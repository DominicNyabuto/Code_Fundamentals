# Milestone 07: Class Methods, Static Methods & Factory Patterns

## 🎯 The Dilemma: Messy Constructor Calls
When customers order standard pizzas at Berry's (like a *Margherita* or *Pepperoni Feast*), callers shouldn't need to specify every single ingredient manually every single time:

```python
# 🚫 Clunky and error-prone
pizza = Pizza("Margherita", "large", 12.0, ["san_marzano_tomato", "fresh_mozzarella", "basil"])
```

What if the customer orders from a web API payload (JSON dictionary)?
Do you write dictionary parsing in the web controller? No! The class itself should know how to instantiate itself from dictionaries or standard presets.

---

## 🛠️ The 3 Method Types in Python

```python
class Pizza:
    BASE_PRICES = {"small": 8.0, "medium": 10.0, "large": 12.0}

    def __init__(self, name: str, size: str, price: float, toppings: list):
        self.name = name
        self.size = size
        self.price = price
        self.toppings = toppings

    # 1. Instance Method: operates on self (an existing pizza instance)
    def bake(self):
        print(f"Baking {self.name} at 450°F")

    # 2. Class Method (@classmethod): receives 'cls' (the class itself).
    # Used for ALTERNATIVE CONSTRUCTORS / FACTORIES.
    @classmethod
    def margherita(cls, size: str = "medium") -> "Pizza":
        price = cls.BASE_PRICES[size.lower()] + 2.0
        return cls(name="Margherita", size=size, price=price, toppings=["tomato", "mozzarella", "basil"])

    @classmethod
    def from_dict(cls, data: dict) -> "Pizza":
        return cls(
            name=data["name"],
            size=data["size"],
            price=float(data["price"]),
            toppings=list(data.get("toppings", []))
        )

    # 3. Static Method (@staticmethod): does not touch self or cls.
    # Self-contained utility function that logically belongs in this class namespace.
    @staticmethod
    def is_valid_size(size: str) -> bool:
        return size.lower() in ("small", "medium", "large")
```

---

## 🔨 Your Exercise
Open [exercise.py](file:///home/dominicnyabuto/Code/00_Coding_Fundamentals/OOPs/07_class_static_methods/exercise.py).
Implement preset factory methods (`margherita`, `pepperoni_feast`, `from_dict`) and static validation utilities.

Run:
```bash
python3 test_milestone.py
```

