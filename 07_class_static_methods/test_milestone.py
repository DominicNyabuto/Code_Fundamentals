import unittest
from exercise import Pizza, OrderValidator

class TestMilestone07(unittest.TestCase):
    def test_static_size_validator(self):
        self.assertTrue(Pizza.validate_size("small"))
        self.assertTrue(Pizza.validate_size("MEDIUM"))
        self.assertTrue(Pizza.validate_size("Large"))
        self.assertFalse(Pizza.validate_size("humongous"))

    def test_margherita_factory(self):
        m = Pizza.margherita(size="small")
        self.assertEqual(m.name, "Margherita")
        self.assertEqual(m.size, "small")
        self.assertEqual(m.price, 8.0 + 2.0)
        self.assertIn("fresh mozzarella", m.toppings)

        with self.assertRaises(ValueError):
            Pizza.margherita(size="extra-large")

    def test_pepperoni_feast_factory(self):
        pep = Pizza.pepperoni_feast(size="large")
        self.assertEqual(pep.name, "Pepperoni Feast")
        self.assertEqual(pep.size, "large")
        self.assertEqual(pep.price, 12.0 + 4.5)
        self.assertIn("double pepperoni", pep.toppings)

    def test_from_dict_factory(self):
        payload = {
            "name": "Custom Hawaiian",
            "size": "medium",
            "price": 14.0,
            "toppings": ["ham", "pineapple"]
        }
        p = Pizza.from_dict(payload)
        self.assertEqual(p.name, "Custom Hawaiian")
        self.assertEqual(p.toppings, ["ham", "pineapple"])

        with self.assertRaises(KeyError):
            Pizza.from_dict({"name": "Incomplete"})

    def test_phone_validator(self):
        self.assertTrue(OrderValidator.is_valid_phone("123-456-7890"))
        self.assertTrue(OrderValidator.is_valid_phone("(123) 456 7890"))
        self.assertTrue(OrderValidator.is_valid_phone("1234567890"))
        self.assertFalse(OrderValidator.is_valid_phone("123-45"))
        self.assertFalse(OrderValidator.is_valid_phone("1234567890123"))

if __name__ == "__main__":
    unittest.main()

