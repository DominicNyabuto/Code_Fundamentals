"""The Procedural Spaghetti Anti-Pattern in Berry's Pizza shop.

Run this script to see how messy, scattered, and vulnerable
procedural programming gets as an application grows.
"""

# Global pricing dictionaries and loose state
SIZE_PRICES = {"small": 8.0, "medium": 10.0, "large": 12.0}
TOPPING_PRICE = 1.50

# Loose pizza dictionaries
order_1 = {
    "customer": "Alice",
    "size": "large",
    "crust": "thin",
    "toppings": ["mushrooms", "olives"]
}

order_2 = {
    "customer": "Bob",
    "size": "small",
    "crust": "stuffed",
    "toppings": ["pepperoni"]
}

def calculate_price(order):
    base = SIZE_PRICES.get(order["size"], 10.0)
    return base + len(order["toppings"]) * TOPPING_PRICE

def print_receipt(order):
    print(f"Receipt for: {order['customer']}")
    print(f"Item: {order['size']} pizza ({order['crust']} crust)")
    print(f"Toppings: {', '.join(order['toppings'])}")
    print(f"Total: ${calculate_price(order):.2f}\n")

if __name__ == "__main__":
    print_receipt(order_1)
    
    # Bug scenario: Anyone can mutate data illegally!
    print("Tampering with Bob's order...")
    order_2["toppings"] = "not_a_list"  # Ruined!
    try:
        print_receipt(order_2)
    except Exception as e:
        print(f"Boom! Unhandled runtime crash due to lack of encapsulation: {e}")
