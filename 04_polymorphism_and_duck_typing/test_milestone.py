import unittest
from exercise import PizzaItem, BeverageItem, SideItem, DeliveryFeeItem, Cart

class TestMilestone04(unittest.TestCase):
    def test_polymorphic_pricing(self):
        pizza = PizzaItem("Veggie", "Medium", 10.0, 3)
        self.assertEqual(pizza.get_total_price(), 14.50)

        drink = BeverageItem("Lemonade", 3.0, 2)
        self.assertEqual(drink.get_total_price(), 6.00)

        side = SideItem("Cheese Sticks", 6.50, "Marinara")
        self.assertEqual(side.get_total_price(), 6.50)

        fee = DeliveryFeeItem(4.0, 1.50)
        self.assertEqual(fee.get_total_price(), 6.00)

    def test_cart_polymorphic_total(self):
        cart = Cart()
        cart.add_item(PizzaItem("Pepperoni", "Large", 12.0, 1)) # 13.50
        cart.add_item(BeverageItem("Iced Tea", 2.50, 2))       # 5.00
        cart.add_item(SideItem("Garlic Bread", 4.00))          # 4.00
        cart.add_item(DeliveryFeeItem(2.0, 2.00))             # 4.00

        self.assertAlmostEqual(cart.calculate_total(), 26.50)

    def test_cart_receipt_output(self):
        cart = Cart()
        cart.add_item(PizzaItem("Cheese", "Small", 8.0, 0))
        cart.add_item(BeverageItem("Soda", 2.0, 1))

        receipt = cart.generate_receipt()
        expected = (
            "Small Cheese (w/ 0 toppings): $8.00\n"
            "1x Soda: $2.00\n"
            "---\n"
            "TOTAL: $10.00"
        )
        self.assertEqual(receipt, expected)

    def test_duck_typing_enforcement(self):
        cart = Cart()
        
        class NonCompliantItem:
            pass

        with self.assertRaises(TypeError):
            cart.add_item(NonCompliantItem())

if __name__ == "__main__":
    unittest.main()

