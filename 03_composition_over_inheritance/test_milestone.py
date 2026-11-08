import unittest
from exercise import Crust, Sauce, Topping, MenuItem, Beverage, Pizza

class TestMilestone03(unittest.TestCase):
    def test_beverage_inheritance(self):
        coke = Beverage("Coca-Cola", 2.50, 16)
        self.assertTrue(isinstance(coke, MenuItem))
        self.assertEqual(coke.name, "Coca-Cola")
        self.assertEqual(coke.get_price(), 2.50)
        self.assertEqual(coke.size_oz, 16)

    def test_pizza_composition_and_pricing(self):
        thin_crust = Crust("Thin Crust", 0.0)
        marinara = Sauce("Classic Marinara", is_spicy=False)
        pizza = Pizza("Custom Pizza", 10.0, thin_crust, marinara)

        self.assertTrue(isinstance(pizza, MenuItem))
        self.assertEqual(pizza.get_price(), 10.0)

        # Add toppings (composed objects)
        cheese = Topping("Mozzarella", 1.50)
        mushrooms = Topping("Portobello Mushrooms", 2.00)
        
        pizza.add_topping(cheese)
        pizza.add_topping(mushrooms)

        # 10.0 base + 0.0 crust + 1.50 + 2.00 = 13.50
        self.assertAlmostEqual(pizza.get_price(), 13.50)

    def test_stuffed_crust_extra_cost(self):
        stuffed_crust = Crust("Cheese Stuffed Crust", 3.00)
        bbq = Sauce("Spicy BBQ", is_spicy=True)
        pizza = Pizza("BBQ Beast", 12.0, stuffed_crust, bbq)

        bacon = Topping("Crispy Bacon", 2.50)
        pizza.add_topping(bacon)

        # 12.00 + 3.00 + 2.50 = 17.50
        self.assertAlmostEqual(pizza.get_price(), 17.50)

    def test_ingredients_summary(self):
        crust = Crust("Gluten-Free", 2.0)
        sauce = Sauce("Pesto")
        pizza = Pizza("Pesto Delight", 11.0, crust, sauce)
        
        self.assertEqual(
            pizza.get_ingredients_summary(),
            "Crust: Gluten-Free, Sauce: Pesto, Toppings: None"
        )
        
        pizza.add_topping(Topping("Olives", 1.0))
        self.assertEqual(
            pizza.get_ingredients_summary(),
            "Crust: Gluten-Free, Sauce: Pesto, Toppings: Olives"
        )

    def test_type_enforcement(self):
        crust = Crust("Pan", 1.0)
        sauce = Sauce("Tomato")
        pizza = Pizza("Test", 10.0, crust, sauce)
        
        with self.assertRaises(TypeError):
            pizza.add_topping("String is not a Topping object")

if __name__ == "__main__":
    unittest.main()
