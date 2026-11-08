"""Milestone 02 Reference Solution."""

class InsufficientFundsError(Exception):
    """Raised when withdrawal exceeds available balance."""
    pass

class InvalidStateTransitionError(Exception):
    """Raised when an order status transition violates workflow rules."""
    pass


class CashRegister:
    """Encapsulates the pizzeria till. Nobody touches the drawer directly."""

    def __init__(self, initial_float: float = 100.0):
        if initial_float < 0:
            raise ValueError("Initial cash cannot be negative")
        self.__balance = float(initial_float)

    @property
    def balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise InsufficientFundsError("Insufficient funds in register")
        self.__balance -= amount
        return amount


class TrackedOrder:
    """An order that strictly enforces lifecycle states."""

    ALLOWED_STATES = ["DRAFT", "CONFIRMED", "PREPARING", "OUT_FOR_DELIVERY", "DELIVERED", "CANCELLED"]

    VALID_TRANSITIONS = {
        "DRAFT": ["CONFIRMED", "CANCELLED"],
        "CONFIRMED": ["PREPARING", "CANCELLED"],
        "PREPARING": ["OUT_FOR_DELIVERY"],
        "OUT_FOR_DELIVERY": ["DELIVERED"],
        "DELIVERED": [],
        "CANCELLED": []
    }

    def __init__(self, order_id: int):
        self._order_id = order_id
        self.__status = "DRAFT"

    @property
    def order_id(self) -> int:
        return self._order_id

    @property
    def status(self) -> str:
        return self.__status

    def transition_to(self, new_status: str) -> None:
        new_status = new_status.upper()
        allowed_next = self.VALID_TRANSITIONS.get(self.__status, [])
        if new_status not in allowed_next:
            raise InvalidStateTransitionError(
                f"Cannot transition from {self.__status} to {new_status}"
            )
        self.__status = new_status
