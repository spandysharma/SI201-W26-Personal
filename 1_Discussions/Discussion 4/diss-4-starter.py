import unittest

"""
Discussion 4: Multiple classes + dictionaries/tuples

You are given 3 classes:
- Item: represents a product (name, price, stock)
- Warehouse: stores Items and can fulfill Orders
- Order: stores what a customer wants to buy (dictionary of item_name -> quantity)

Your job is to complete the TODOs so that all tests pass.

TASK 1: Implement Warehouse.add_item(item) with MERGE behavior (same name => add stock)
TASK 2: Implement Order.add_line(item_name, quantity) using a DICTIONARY
TASK 3: Implement Warehouse.fulfill_order(order) and Warehouse.inventory_report()
TASK 4 (Optional): Warehouse.inventory_report()

Notes:
- Students do NOT write tests in this discussion.
- Focus is on classes, association, dicts, and tuples.
"""


class Item:
    """Represents an item to be sold."""

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"Item(name={self.name}, price={self.price}, stock={self.stock})"

    def sell(self, quantity):
        if quantity <= 0 or quantity > self.stock:
            return False

        self.stock -= quantity
        return True


class Order:
    """
    Represents a customer's order.
    Stores order lines as a dictionary that maps item_name -> quantity:
        self.lines[item_name] = quantity
    """

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.lines = {}  # item_name -> quantity (int)

    # ==============================
    # Task 2
    # ==============================
    def add_line(self, item_name, quantity):
        """
        TASK 2:
        Add (or update) an item in the order.

        Rules:
        - If quantity <= 0: do nothing
        - Otherwise:
            * if item_name already exists, add to its quantity
            * else set it
        """
        # TODO
        pass

    def __str__(self):
        return f"Order(customer={self.customer_name}, lines={self.lines})"


class Warehouse:
    """Stores and manages items."""

    def __init__(self, items=None):
        self.items = []
        if items is not None:
            for it in items:
                self.add_item(it)

    def find_item(self, item_name):
        """Return the Item with this name, or None if not found."""
        for it in self.items:
            if it.name == item_name:
                return it
        return None

    # ==============================
    # Task 1
    # ==============================
    def add_item(self, item):
        """
        TASK 1:
        Add an item to the warehouse.

        Intended behavior:
        - If an item with the same name already exists, increase its stock by item.stock.
          (Keep the existing price as-is.)
        - Otherwise, append the new item.
        """
        # TODO
        itemExists = self.find_item(item.name)
        if itemExists:
            itemExists.stock += item.stock
        else:
            self.items.append(item)


    # ==============================
    # Task 3
    # ==============================
    def fulfill_order(self, order):
        """
        TASK 3:
        Attempt to fulfill an Order by selling stock.

        For each (item_name, quantity) in order.lines:
        - If the item doesn't exist, the whole quantity is backordered
        - If item exists but not enough stock:
            * sell as many as possible (stock becomes 0)
            * remaining qty goes to backorder
        - If enough stock:
            * sell all requested

        Return: backorder dictionary item_name -> remaining_qty (only include items with remaining_qty > 0)
        """
        # TODO
        pass

    # ==============================
    # Task 4 (Optional)
    # ==============================
    def inventory_report(self):
        """
        TASK 4: Return a DICTIONARY where:
            key   = item.name
            value = (item.price, item.stock)   <-- a TUPLE

        Example:
            {
              "Water": (1, 100),
              "Cider": (5, 25)
            }
        """
        # TODO
        pass


# -------------------- PROVIDED TESTS --------------------


class TestWarehouseOrderSystem(unittest.TestCase):
    def setUp(self):
        self.beer = Item("Beer", 6, 20)
        self.cider = Item("Cider", 5, 25)
        self.water = Item("Water", 1, 100)
        self.fanta = Item("Fanta", 2, 60)
        self.coke = Item("CocaCola", 3, 40)

    def test_item_sell(self):
        # Valid sale
        self.assertTrue(self.beer.sell(5))
        self.assertEqual(self.beer.stock, 15)

        # Too large
        self.assertFalse(self.beer.sell(100))
        self.assertEqual(self.beer.stock, 15)

        # Non-positive
        self.assertFalse(self.beer.sell(0))
        self.assertFalse(self.beer.sell(-3))
        self.assertEqual(self.beer.stock, 15)

    def test_warehouse_add_item_merge(self):
        w = Warehouse()
        self.assertEqual(len(w.items), 0)

        w.add_item(self.cider)
        self.assertEqual(len(w.items), 1)
        self.assertEqual(w.find_item("Cider").stock, 25)

        # Add same-name item: should MERGE stock, not create a duplicate
        w.add_item(Item("Cider", 999, 10))  # price should not overwrite existing
        self.assertEqual(len(w.items), 1)
        self.assertEqual(w.find_item("Cider").price, 5)
        self.assertEqual(w.find_item("Cider").stock, 35)

        # Add different item: should append
        w.add_item(self.water)
        self.assertEqual(len(w.items), 2)
        self.assertEqual(w.find_item("Water").stock, 100)

    def test_order_add_line_dict(self):
        o = Order("Ada")
        self.assertEqual(o.lines, {})

        o.add_line("Water", 3)
        self.assertEqual(o.lines, {"Water": 3})

        # Update existing line
        o.add_line("Water", 2)
        self.assertEqual(o.lines, {"Water": 5})

        # Ignore non-positive
        o.add_line("Water", 0)
        o.add_line("Beer", -1)
        self.assertEqual(o.lines, {"Water": 5})

    def test_inventory_report_dict_tuple(self):
        w = Warehouse([self.beer, self.cider])
        report = w.inventory_report()

        # Must be dict of name -> (price, stock)
        self.assertIsInstance(report, dict)
        self.assertEqual(report["Beer"], (6, 20))
        self.assertEqual(report["Cider"], (5, 25))

        # tuple-ness check
        self.assertIsInstance(report["Beer"], tuple)
        self.assertEqual(len(report["Beer"]), 2)

    def test_fulfill_order_backorder(self):
        w = Warehouse([self.water, self.coke])  # Water=100, Coke=40
        o = Order("Lin")

        o.add_line("Water", 30)  # enough
        o.add_line("CocaCola", 50)  # not enough (only 40)
        o.add_line("Fanta", 5)  # doesn't exist in warehouse

        back = w.fulfill_order(o)

        # Water should be reduced by 30
        self.assertEqual(w.find_item("Water").stock, 70)

        # Coke should go to 0, and 10 should be backordered
        self.assertEqual(w.find_item("CocaCola").stock, 0)
        self.assertEqual(back.get("CocaCola"), 10)

        # Missing item entirely => full amount backordered
        self.assertEqual(back.get("Fanta"), 5)

        # Items fully filled should not appear in backorder dict
        self.assertNotIn("Water", back)


def main():
    unittest.main(verbosity=2)


if __name__ == "__main__":
    main()
