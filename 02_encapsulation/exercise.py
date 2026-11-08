"""Milestone 02 Exercise: Encapsulation & Data Protection in Berry's Pizza.

Implement:
1. `CashRegister`: Encapsulates cash balance with strict transaction controls.
2. `TrackedOrder`: Encapsulates status transitions so orders follow proper workflow.
"""

from typing import List

class InsufficientFundsError(Exception):
    """Raised when withdrawal exceeds available balance."""
    pass

class InvalidStateTransitionError(Exception):
    """Raised when an order status transition violates workflow rules."""
    pass


class CashRegister:
    """Encapsulates the pizzeria till. Nobody touches the drawer directly."""

    def __init__(self, initial_float: float = 100.0):
        """Initialize with private balance attribute `__balance`.
        If initial_float is negative, raise ValueError.
        """
        # TODO: Implement __init__
        pass

    @property
    def balance(self) -> float:
        """Getter for current balance. Read-only attribute!"""
        # TODO: Implement balance getter
        pass

    def deposit(self, amount: float) -> None:
        """Add positive cash amount to register.
        Raise ValueError("Deposit amount must be positive") if amount <= 0.
        """
        # TODO: Implement deposit
        pass

    def withdraw(self, amount: float) -> float:
        """Withdraw cash from register.
        Raise ValueError("Withdrawal amount must be positive") if amount <= 0.
        Raise InsufficientFundsError("Insufficient funds in register") if amount > self.balance.
        Return the withdrawn amount.
        """
        # TODO: Implement withdraw
        pass


class TrackedOrder:
    """An order that strictly enforces lifecycle states.
    
    Valid workflow progression:
    'DRAFT' -> 'CONFIRMED' -> 'PREPARING' -> 'OUT_FOR_DELIVERY' -> 'DELIVERED'
    'CANCELLED' can be reached only from 'DRAFT' or 'CONFIRMED'.
    """

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
        """Read-only property returning current status."""
        # TODO: Implement status getter
        pass

    def transition_to(self, new_status: str) -> None:
        """Change the order's status.
        new_status should be normalized to uppercase.
        If new_status is not a valid progression from current status,
        raise InvalidStateTransitionError(f"Cannot transition from {current} to {new_status}").
        """
        # TODO: Implement transition_to
        pass

