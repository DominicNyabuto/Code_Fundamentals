# Milestone 04: Polymorphism & Duck Typing

## 🎯 The Core Insight from Cloud X Berry
In the video, Cloud X Berry demonstrates the nightmare of the **"Type-Checking Ladder"**:

```python
# 🚫 BAD CODE: The Type-Checking Nightmare
def process_checkout(cart):
    total = 0.0
    for item in cart:
        if isinstance(item, Pizza):
            total += item.compute_pizza_cost()
        elif isinstance(item, Soda):
            total += item.beverage_price()
        elif isinstance(item, GarlicBread):
            total += item.side_dish_fee()
    return total
```

### What is wrong here?
Whenever Berry's Pizzeria introduces a new item (e.g. `ChickenWings`, `IceCream`, `MerchTshirt`), **every single checkout function, receipt generator, and tax calculator has to be modified**!

---

## 🦆 Polymorphism & Python's "Duck Typing"

**Polymorphism** means *"many forms"*. Different classes can implement the **exact same method name** (`get_total_price()`, `get_receipt_line()`).

In Python, we also have **Duck Typing**:
> *"If it walks like a duck and quacks like a duck, it's a duck."*

The checkout cart doesn't care whether an object is a `Pizza`, a `Drink`, a `Dessert`, or a `DeliveryFee`. As long as it responds to `.get_total_price()`, the cart can process it!

```python
#  CLEAN, POLYMORPHIC CODE
def process_checkout(cart):
    return sum(item.get_total_price() for item in cart)
```

No `if isinstance(...)`! New items can be added tomorrow without touching a single line of checkout code.

---

## 🔨 Your Exercise
Open [exercise.py](file:///home/dominicnyabuto/Code/00_Coding_Fundamentals/OOPs/04_polymorphism_and_duck_typing/exercise.py).
1. Implement multiple distinct item types (`PizzaItem`, `BeverageItem`, `SideItem`, and even a `DeliveryFeeItem`).
2. Implement uniform polymorphic methods: `get_total_price()` and `get_receipt_line()`.
3. Implement `Cart` that sums prices and generates itemized receipts polymorphically.

Run:
```bash
python3 test_milestone.py
```

