# Milestone 02: Encapsulation & Data Protection

## 🎯 The Core Insight from Cloud X Berry
In the video, Cloud X Berry uses the **Cash Register / Bank Account** analogy:
> *"When you go into Berry's Pizza shop, can you just walk behind the counter, pull open the cash register drawer, take money out, or shove money in? Absolutely not! You talk to the cashier."*

In programming, **Encapsulation** is the bundling of data and the methods that operate on that data, while **restricting direct access** to some of the object's internal components.

---

## 🔒 Encapsulation in Python

Unlike Java or C++ which have strict `public`, `protected`, and `private` keywords, Python uses conventions:

1. **Public (`self.name`):** Accessible by anyone, anywhere.
2. **Protected by convention (`self._balance`):** Single underscore signals: *"Internal implementation detail; don't touch unless you know what you're doing."*
3. **Private via Name Mangling (`self.__balance`):** Double underscore. Python renames this internally to `_ClassName__balance` to prevent accidental overwriting in subclasses.

### The Pythonic Way: `@property` and `@setter`

Instead of clumsy Java-style `getBalance()` and `setBalance(val)`, Python uses properties:

```python
class CashRegister:
    def __init__(self, initial_cash: float = 0.0):
        if initial_cash < 0:
            raise ValueError("Initial cash cannot be negative")
        self.__balance = float(initial_cash)

    @property
    def balance(self) -> float:
        """Getter: lets callers read register.balance like an attribute."""
        return self.__balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds in register")
        self.__balance -= amount
```

---

## 🔨 Your Exercise
Open [exercise.py](file:///home/dominicnyabuto/Code/00_Coding_Fundamentals/OOPs/02_encapsulation/exercise.py).
You will build:
1. `CashRegister`: Private balance, `@property`, deposit/withdraw validations.
2. `TrackedOrder`: Encapsulated status workflow (`DRAFT` -> `CONFIRMED` -> `PREPARING` -> `OUT_FOR_DELIVERY` -> `DELIVERED`). Disallows illegal backward jumps!

Run:
```bash
python3 test_milestone.py
```
