import unittest
from exercise import Pizza, PizzeriaOrder

class TestMilestone06(unittest.TestCase):
    def test_pizza_repr_str_eq(self):
        p1 = Pizza("Pepperoni", "large", 14.50)
        p2 = Pizza("Pepperoni", "large", 14.50)
        p3 = Pizza("Veggie", "small", 9.00)

        self.assertEqual(repr(p1), "Pizza(name='Pepperoni', size='large', price=14.5)")
        self.assertEqual(str(p1), "Large Pepperoni ($14.50)")
        
        # Dunder __eq__
        self.assertEqual(p1, p2)
        self.assertNotEqual(p1, p3)
        self.assertFalse(p1 == "not a pizza")

    def test_order_dunder_len_getitem_iter(self):
        p1 = Pizza("Margherita", "medium", 11.0)
        p2 = Pizza("Hawaiian", "large", 13.5)
        order = PizzeriaOrder("Alice", [p1, p2])

        # __len__
        self.assertEqual(len(order), 2)

        # __getitem__
        self.assertEqual(order[0], p1)
        self.assertEqual(order[1], p2)

        # __iter__
        names = [p.name for p in order]
        self.assertEqual(names, ["Margherita", "Hawaiian"])

    def test_order_dunder_add_merging(self):
        order1 = PizzeriaOrder("Alice", [Pizza("Cheese", "small", 8.0)])
        order2 = PizzeriaOrder("Bob", [Pizza("BBQ Chicken", "large", 15.0)])

        merged = order1 + order2
        self.assertEqual(merged.customer_name, "Alice & Bob")
        self.assertEqual(len(merged), 2)
        self.assertEqual(merged[0].name, "Cheese")
        self.assertEqual(merged[1].name, "BBQ Chicken")

        with self.assertRaises(TypeError):
            _ = order1 + 100

if __name__ == "__main__":
    unittest.main()

