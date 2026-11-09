# Milestone 01: From Procedural Spaghetti to Clean Classes

## The Core Insight from Cloud X Berry
In the video, Cloud X Berry starts with an online pizza shop. At first, you might write code procedurally using dictionaries and global functions:

```python
# Procedural approach: Data is naked and detached from logic
pizza_order = {
    "size": "large",
    "crust": "thin",
    "toppings": ["cheese", "mushrooms"]
}

def calculate_pizza_price(pizza):
    base_price = 12.0 if pizza["size"] == "large" else 8.0
    return base_price + len(pizza["toppings"]) * 1.5
```

### Why does this fall apart in real software?
1. **No Data Integrity:** Any rogue code can execute `pizza_order["toppings"] = "not a list"` or `pizza_order["size"] = "extra-giant-spaceship"`.
2. **Logic Scattered Everywhere:** When you want to discount a pizza, print a box label, or cook the pizza, you have to pass raw dictionaries around to separate global functions.
3. **Duplication & Brittleness:** If you change a dictionary key from `"toppings"` to `"ingredients"`, every function across your codebase breaks silently.

---

## 💡 The OOP Solution: The Blueprint (Class) and The House (Object)

A **Class** is the recipe / blueprint.
An **Object** (instance) is the actual physical pizza baked from that recipe.

```python
class Pizza:
    def __init__(self, size: str, crust: str):
        # self refers to THIS specific pizza instance being created
        self.size = size.lower()
        self.crust = crust.lower()
        self.toppings = []

    def add_topping(self, topping: str):
        self.toppings.append(topping.lower())

    def calculate_price(self) -> float:
        base = 8.0 if self.size == "small" else 10.0 if self.size == "medium" else 12.0
        return base + (len(self.toppings) * 1.50)
```

---

## 🔨 Your Exercise
Open [exercise.py](file:///home/dominicnyabuto/Code/00_Coding_Fundamentals/OOPs/01_procedural_to_oop/exercise.py) and complete the `Pizza` and `CustomerOrder` classes.
Then run:
```bash
python3 test_milestone.py
```

