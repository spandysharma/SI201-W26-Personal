import unittest

"""
WRITTEN SOLUTION - Discussion 5: Testing and Debugging

You are given 3 classes:
- Item: represents a product (name, price, stock)
- Warehouse: stores Items and can fulfill Orders
- Order: stores what a customer wants to buy (dictionary of item_name -> quantity)


TASK 1: 
TASK 2: 
TASK 3: 
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

    def add_line(self, item_name, quantity):
        if quantity <= 0:
            return

        # Add new or update existing
        if item_name in self.lines:
            self.lines[item_name] += quantity
        else:
            self.lines[item_name] = quantity

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

    def add_item(self, item):
        """
        If an item with the same name already exists, increase its stock.
        Keep the existing price.
        Otherwise, append the item.
        """
        existing = self.find_item(item.name)
        if existing is not None:
            existing.stock += item.stock
        else:
            self.items.append(item)

    def inventory_report(self):
        """
        Return dict: name -> (price, stock)
        """
        report = {}
        for it in self.items:
            report[it.name] = (it.price, it.stock)
        return report

    def fulfill_order(self, order):
        """
        Attempt to fulfill an order. Return dict of backordered items:
            item_name -> remaining_qty
        """
        backorder = {}

        for item_name, qty in order.lines.items():
            item = self.find_item(item_name)

            # Item not found => all backordered
            if item is None:
                backorder[item_name] = qty
                continue

            # Enough stock => sell all
            if item.stock >= qty:
                item.sell(qty)
                continue

            # Not enough stock => sell what you can, backorder the rest
            remaining = qty - item.stock
            if item.stock > 0:
                item.sell(item.stock)  # sell everything left
            if remaining > 0:
                backorder[item_name] = remaining

        return backorder


# -------------------- TODO TESTS --------------------


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

        # todo: add test cases to check zero, Non-positive values
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
