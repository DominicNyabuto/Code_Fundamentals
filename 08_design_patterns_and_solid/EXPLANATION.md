# Milestone 08: Design Patterns & SOLID Principles in Python

## 🎯 Elevating to Senior OOP Architecture
Senior engineers do not just write classes; they design systems that are **maintainable**, **extensible**, and **loosely coupled**. Two of the most useful design patterns in an ordering system like Berry's Pizza are:

1. **The Strategy Pattern (Behavioral):**
   Allows switching pricing or discount algorithms dynamically at runtime without modifying the Order class.
2. **The Observer Pattern (Behavioral):**
   Allows notifying interested parties (Kitchen Display, Customer SMS, Delivery Dispatch) whenever an order state changes, without coupling the Order to any specific listener.

---

## 🏛️ The SOLID Principles in Berry's Pizza

| Principle | Meaning in Berry's Pizza |
|---|---|
| **S** - Single Responsibility | `Order` manages order items. It does NOT format receipts, query the database, or send SMS. |
| **O** - Open / Closed | You can add a new `BlackFridayCoupon` without modifying `Order.py`. |
| **L** - Liskov Substitution | Any `DiscountStrategy` can be plugged in without crashing the checkout process. |
| **I** - Interface Segregation | Keep interfaces lean; don't force a `CashRegister` to implement `send_email()`. |
| **D** - Dependency Inversion | High-level `Order` depends on `DiscountStrategy` (abstraction), not concrete `PercentageDiscount`. |

---

## 🔨 Your Exercise
Open [exercise.py](file:///home/dominicnyabuto/Code/00_Coding_Fundamentals/OOPs/08_design_patterns_and_solid/exercise.py).
1. Implement the `DiscountStrategy` hierarchy: `NoDiscount`, `PercentageDiscount`, `FlatDiscount`.
2. Implement the `OrderObserver` interface: `KitchenDisplay`, `CustomerAlertObserver`.
3. Implement `OrderSubject` with observer attachment and event dispatching.

Run:
```bash
python3 test_milestone.py
```
