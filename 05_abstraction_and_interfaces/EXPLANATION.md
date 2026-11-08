# Milestone 05: Abstraction & Abstract Base Classes (ABCs)

## 🎯 The Core Insight from Cloud X Berry
What is the difference between **Encapsulation** and **Abstraction**? Many developers confuse the two!

* **Encapsulation** is about **data security & boundary**:
  > *"Hiding the cash in the register drawer and only letting authorized methods touch it."*
* **Abstraction** is about **complexity reduction & contracts**:
  > *"When you press the brake pedal in a car, you don't need to know how the hydraulic lines and calipers work. You just need to know that pushing the pedal slows the car down."*

---

## 💳 The Berry's Pizza Payment System

At checkout, Berry's Pizzeria accepts multiple payment options:
- **Stripe** (processes credit cards with token authorization)
- **PayPal** (redirects to digital wallet with email authentication)
- **Cash on Delivery** (verifies customer has exact change or notes)

Your checkout system should NOT need to know the messy details of Stripe API requests or PayPal webhook handshakes. It only cares that each payment processor obeys a **Contract**.

### Python's `abc` Module
In Python, we declare formal contracts using `ABC` (Abstract Base Class) and `@abstractmethod`:

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        """Any subclass MUST implement this method.
        If it does not, Python will refuse to instantiate it!
        """
        pass
```

If someone tries:
```python
class ApplePayProcessor(PaymentProcessor):
    pass # Forgot to implement process_payment!

p = ApplePayProcessor() #  TypeError: Can't instantiate abstract class ApplePayProcessor without an implementation for abstract method 'process_payment'
```

---

## 🔨 Your Exercise
Open [exercise.py](file:///home/dominicnyabuto/Code/00_Coding_Fundamentals/OOPs/05_abstraction_and_interfaces/exercise.py).
1. Implement abstract `PaymentProcessor` and `NotificationService` base classes.
2. Build concrete `StripeProcessor`, `PayPalProcessor`, and `CashProcessor`.
3. Implement `CheckoutService` that uses abstraction to process orders seamlessly.

Run:
```bash
python3 test_milestone.py
```

