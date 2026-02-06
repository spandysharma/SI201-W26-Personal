import unittest

# TASK 1: Complete test_count_a()
# TASK 2: Complete test_add_item(), test_warehouse_max_stock(), and test_warehouse_max_price()

# Counts the number of a's in a string


def count_a(string):
    total = 0
    for i in range(len(string)):
        if string.lower()[i] == 'a':
            total += 1
    return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
    # Constructor.
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    # Print
    def __str__(self):
        return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.


class Warehouse:

    # Constructor
    def __init__(self, items=[]):
        self.items = items[:]

    # Prints all the items in the warehouse, one on each line.
    def print_items(self):
        for item in self.items:
            print(item)
            print("\n")

    # Adds an item to the warehouse
    def add_item(self, item):
        self.items.append(item)

    # Returns the item in the warehouse with the most stock
    def get_max_stock(self):
        max_stock_item = self.items[0]
        for item in self.items:
            if item.stock > max_stock_item.stock:
                max_stock_item = item
        return max_stock_item

    # Returns the item in the warehouse with the highest price
    def get_max_price(self):
        max_price_item = self.items[0]
        for item in self.items:
            if item.price > max_price_item.price:
                max_price_item = item
        return max_price_item


# Tests
class TestAllMethods(unittest.TestCase):

    # SetUp -- we create a bunch of items for you to use in your tests.
    def setUp(self):
        self.item1 = Item("Beer", 6, 20)
        self.item2 = Item("Cider", 5, 25)
        self.item3 = Item("Water", 1, 100)
        self.item4 = Item("Fanta", 2, 60)
        self.item5 = Item("CocaCola", 3, 40)

    # Check to see whether count_a works
    def test_count_a(self):
        # Sentence with an a
        self.assertEqual(count_a("i am a cat."), 3)

        # # With 0 a's
        self.assertEqual(count_a('not one here'), 0)

        # # Capital A's
        self.assertEqual(count_a('A A A'), 3)

        # # A at beginning
        self.assertEqual(count_a('A big dog'), 1)

        # # A at end
        self.assertEqual(count_a('big A'), 1)

        # # Only a's
        self.assertEqual(count_a('aaaaaaaaa'), 9)

        pass

    # Check to see whether you can add an item to the warehouse

    def test_add_item(self):
        w1 = Warehouse()
        self.assertEqual(len(w1.items), 0)
        # Adding one item
        w1.add_item(self.item1)
        self.assertEqual(len(w1.items), 1)
        self.assertEqual(w1.items[0], self.item1)

        # Adding 2 items
        w1.add_item(self.item2)
        w1.add_item(self.item3)
        self.assertEqual(len(w1.items), 3)
        self.assertEqual(w1.items[1], self.item2)

    # Check to see whether warehouse correctly returns the item with the most stock

    def test_warehouse_max_stock(self):
        w2 = Warehouse()

        # Adding one item, seeing if it returns the correct item.
        w2.add_item(self.item5)
        self.assertEqual(w2.get_max_stock(), self.item5)

        # Adding multiple items, seeing if it returns the right one
        w2.add_item(self.item1)
        w2.add_item(self.item2)
        self.assertEqual(w2.get_max_stock(), self.item5)

        w2.add_item(self.item3)
        w2.add_item(self.item4)
        self.assertEqual(w2.get_max_stock(), self.item3)

    # Check to see whether the warehouse correctly return the item with the highest price

    def test_warehouse_max_price(self):
        w3 = Warehouse()

        # Adding one item, seeing if it returns the correct item.
        w3.add_item(self.item5)
        self.assertEqual(w3.get_max_price(), self.item5)

        # Adding multiple items, seeing if it returns the right one
        w3.add_item(self.item1)
        w3.add_item(self.item2)
        self.assertEqual(w3.get_max_price(), self.item1)
        w3.add_item(self.item3)
        w3.add_item(self.item4)
        self.assertEqual(w3.get_max_price(), self.item1)


def main():
    unittest.main(verbosity=2)


if __name__ == "__main__":
    main()
