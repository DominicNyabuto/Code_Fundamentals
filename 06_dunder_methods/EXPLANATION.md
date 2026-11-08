# Milestone 06: Pythonic "Magic" (Dunder) Methods

## 🎯 Moving from Beginner to Pythonic Pro
In languages like Java or C++, when you want to print an object, you write `order.toString()`. When you want to check if two items are equal, you call `order.equals(other)`.

In Python, classes can integrate seamlessly with the language syntax itself via **Dunder (Double Underscore) Methods**:

| Method | Syntax Trigger | Purpose |
|---|---|---|
| `__repr__(self)` | `repr(obj)` or terminal print | Developer/debug string (e.g., `Pizza(size='L', toppings=['olives'])`) |
| `__str__(self)` | `str(obj)` or `print(obj)` | User-friendly receipt string |
| `__len__(self)` | `len(order)` | Returns total items in order |
| `__getitem__(self, index)` | `order[0]` | Access items using standard square bracket indexing |
| `__iter__(self)` | `for item in order:` | Makes the order an iterable generator/list |
| `__eq__(self, other)` | `order1 == order2` | Value-based equality instead of memory id comparison |
| `__add__(self, other)` | `order1 + order2` | Combines two customer orders into a single merged order! |

---

## 🍕 Real-World Scenario: Merging Group Orders

Imagine a party order at Berry's Pizza: Alice starts an order for 2 pizzas. Bob adds another order of 1 pizza.
Instead of having a clunky `order1.mergeWithOtherOrder(order2)`, Python lets you write:

```python
party_order = alice_order + bob_order
print(f"Total items in party order: {len(party_order)}")
```

---

## 🔨 Your Exercise
Open [exercise.py](file:///home/dominicnyabuto/Code/00_Coding_Fundamentals/OOPs/06_dunder_methods/exercise.py).
Implement the dunder methods on `Pizza` and `PizzeriaOrder`.

Run:
```bash
python3 test_milestone.py
```
