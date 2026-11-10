import unittest
from exercise import Pizza, CustomerOrder  #from the exercise.py file it 
                                           #imports Pizza and CustomerOrder classes

class TestMilestone01(unittest.TestCase):
    def test_pizza_initialization_and_validation(self):
        pizza_order_example_1 = Pizza("Large", "Thin")
        self.assertEqual(pizza_order_example_1.size, "large")  #check if Large is lower 'large'
        self.assertEqual(pizza_order_example_1.crust, "thin")  #check if Thin is lower 'thin'
        self.assertEqual(pizza_order_example_1.toppings, [])  #check if toppings is empty

        with self.assertRaises(ValueError):  #check if ValueError is raised when 
            Pizza("Giant", "Thin")  #invalid size "Giant" is passed, should throw eroor, otherwise the test fails

    def test_add_topping_and_price_calculation(self):
        pizza_order_example_2 = Pizza("small", "traditional")
        self.assertEqual(pizza_order_example_2.calculate_price(), 8.0)
        
        pizza_order_example_2.add_topping("Mushrooms")
        pizza_order_example_2.add_topping("Olives")
        self.assertEqual(pizza_order_example_2.toppings, ["mushrooms", "olives"])
        self.assertEqual(pizza_order_example_2.calculate_price(), 8.0 + 3.0)

    def test_description_format(self):
        plain_pizza = Pizza("medium", "stuffed")
        self.assertEqual(
            plain_pizza.get_description(),
            "medium pizza with stuffed crust topped with: No Toppings"
        )
        
        pepperoni_pizza = Pizza("large", "thin")
        pepperoni_pizza.add_topping("pepperoni")
        self.assertEqual(
            pepperoni_pizza.get_description(),
            "large pizza with thin crust topped with: pepperoni"
        )

    def test_customer_order_total(self):
        order = CustomerOrder("Alice")
        self.assertEqual(order.customer_name, "Alice")
        
        p1 = Pizza("small", "thin")  # $8.0
        p2 = Pizza("large", "pan")   # $12.0
        p2.add_topping("extra cheese") # $12.0+$1.50 -> $13.50

        order.add_pizza(p1)
        order.add_pizza(p2)

        self.assertAlmostEqual(order.calculate_total(), 21.50)

    def test_type_safety_on_add_pizza(self):
        order = CustomerOrder("Bob")
        with self.assertRaises(TypeError):
            order.add_pizza({"fake": "pizza"})

if __name__ == "__main__":
    unittest.main()

