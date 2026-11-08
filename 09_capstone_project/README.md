# Milestone 09: Capstone — The Complete Berry's Pizzeria Engine

Congratulations on reaching the Capstone! In this final milestone, all OOP concepts you have practiced unite into an end-to-end, object-oriented food ordering and dispatch application.

---

## 🏗️ Architecture Overview

```mermaid
classDiagram
    class MenuItem {
        <<abstract>>
        +name: str
        +get_price()* float
        +get_description()* str
    }
    class Pizza {
        +crust: Crust
        +sauce: Sauce
        +toppings: list~Topping~
        +get_price() float
        +get_description() str
    }
    class Beverage {
        +size_oz: int
        +get_price() float
    }
    class DiscountStrategy {
        <<abstract>>
        +calculate_discount(subtotal)* float
    }
    class PaymentProcessor {
        <<abstract>>
        +process_payment(amount)* dict
    }
    class OrderObserver {
        <<abstract>>
        +update(order_id, status)* void
    }
    class Order {
        -order_id: int
        -status: str
        +items: list~MenuItem~
        +attach_observer(obs)
        +transition_to(status)
        +calculate_total() float
    }

    MenuItem <|-- Pizza
    MenuItem <|-- Beverage
    Order *-- MenuItem
    Order o-- DiscountStrategy
    Order o-- OrderObserver
```

---

## 🚀 Running the Capstone

You can run the interactive ordering CLI demo:
```bash
python3 berrys_pizzeria.py
```

Or run the end-to-end integration test suite:
```bash
python3 test_capstone.py
```

