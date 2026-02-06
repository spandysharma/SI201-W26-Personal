import unittest

"""
Discussion 5: Midterm Practice - Bank Accounts

TASK 1: Implement Ticket.final_price()
TASK 2: Implement StudentTicket.final_price() (override; apply discount)
TASK 3: Implement TicketBooth.sell(ticket, quantity) (store sales using dict + tuples)
TASK 4: TA TODO: Write the <INSERT TESTNAME HERE> test case in TestStudentWritten class

"""


class Ticket:
    """Base class representing a ticket for an event."""

    def __init__(self, event_title, price, timing):
        self.event_title = event_title
        self.event_time = timing # tuple (start_time, end_time)
        self.price = price
        self.ticket_type = "Regular"

    # def final_price(self):
    #     """
    #     TASK 1:
    #     Return the price a customer pays for this ticket.

    #     Rules:
    #     - price <= 0 => treat as free ticket => return 0
    #     - otherwise return price
    #     """
    #     # TODO
    #     pass

    # def ticket_type(self):
    #     """Return a short label for receipts."""
    #     return "Regular"


class StudentTicket(Ticket):
    """Student ticket with a percentage discount."""

    def __init__(self, event_title, price, timing, school_name, discount_percent):
        super().__init__(event_title, price, timing)
        self.school_name = school_name
        self.discount_percent = discount_percent  # e.g., 20 means 20% off

    def final_price(self):
        """
        TASK 1:
        Return the discounted final price.

        Rules:
        - If price <= 0 => return 0
        - Clamp discount_percent into [0, 100]
        - discounted_price = price * (1 - discount/100)
        - Return an int (truncate toward 0). Example: base=25, discount=10 => 22
        """
        # TA:TODO - DOES THE ABOVE CLAMP DISCOUNT_PERCENT MAKE SENSE?
        # TODO
        pass

    def ticket_type(self):
        return "Student"


class TicketBooth:
    """
    Stores ticket sales.

    sales is a dictionary:
        key   = event_title (str)
        value = list of tuples: (ticket_type, final_price)

    Example:
        {
          "Comedy Night": [("Regular", 20), ("Student", 15)],
          "Robotics Expo": [("Student", 12)]
        }
    """

    def __init__(self):
        self.sales = {}  # event_title -> list[ (ticket_type, final_price) ]

    def sell(self, ticket, quantity):
        """
        TASK 3:
        Record the sale of `quantity` tickets of the given Ticket object.

        Rules:
        - If quantity = 0: do nothing (no changes)
        - Otherwise, add `quantity` tuples to self.sales dictionary
        - Use ticket.event_title as the key and tuples of (<ticket type>, <final price>) as values.
        """
        # TODO
        pass

    def event_summary(self, event_title):
        """
        Provided helper (no TODO): Return a tuple (count_sold, revenue) for this event.
        If event_title not in sales => (0, 0)
        """
        if event_title not in self.sales:
            return (0, 0)

        count = len(self.sales[event_title])
        revenue = 0
        for _t_type, price in self.sales[event_title]:
            revenue += price
        return (count, revenue)


# -------------------- UNIT TESTS --------------------


class TestTicketSystem(unittest.TestCase):
    def test_ticket_final_price_nonpositive(self):
        t1 = Ticket("Comedy Night", 20)
        t2 = Ticket("Comedy Night", 0)
        t3 = Ticket("Comedy Night", -5)

        self.assertEqual(t1.final_price(), 20)
        self.assertEqual(t2.final_price(), 0)
        self.assertEqual(t3.final_price(), 0)

    def test_student_ticket_discount_and_clamp(self):
        s1 = StudentTicket("Robotics Expo", 50, "UMich", 20)  # 20% off => 40
        s2 = StudentTicket("Robotics Expo", 50, "UMich", 0)  # 0% off => 50
        s3 = StudentTicket("Robotics Expo", 50, "UMich", 120)  # clamp to 100% => 0
        s4 = StudentTicket("Robotics Expo", 50, "UMich", -10)  # clamp to 0% => 50

        self.assertEqual(s1.final_price(), 40)
        self.assertEqual(s2.final_price(), 50)
        self.assertEqual(s3.final_price(), 0)
        self.assertEqual(s4.final_price(), 50)

    def test_sell_records_dict_and_tuples(self):
        booth = TicketBooth()
        regular = Ticket("Comedy Night", 25)
        student = StudentTicket(
            "Comedy Night", 25, "UMich", 10
        )  # 10% off => 22 (truncate)

        booth.sell(regular, 2)
        booth.sell(student, 3)

        # Must be dict keyed by event name
        self.assertIsInstance(booth.sales, dict)
        self.assertIn("Comedy Night", booth.sales)

        records = booth.sales["Comedy Night"]
        self.assertEqual(len(records), 5)

        # Each record must be a tuple of (type, price)
        self.assertIsInstance(records[0], tuple)
        self.assertEqual(len(records[0]), 2)

        # Check counts via helper
        count, revenue = booth.event_summary("Comedy Night")
        self.assertEqual(count, 5)
        # revenue: 2*25 + 3*22 = 50 + 66 = 116
        self.assertEqual(revenue, 116)

    def test_sell_ignores_nonpositive_quantity(self):
        booth = TicketBooth()
        t = Ticket("Jazz Show", 30)

        booth.sell(t, 0)
        booth.sell(t, -2)
        self.assertEqual(booth.event_summary("Jazz Show"), (0, 0))
        self.assertEqual(booth.sales, {})

    def test_multiple_events_stay_separate(self):
        booth = TicketBooth()
        booth.sell(Ticket("A", 10), 1)
        booth.sell(Ticket("B", 10), 2)

        self.assertEqual(booth.event_summary("A"), (1, 10))
        self.assertEqual(booth.event_summary("B"), (2, 20))


# -------------------- STUDENT-WRITTEN TEST (WRITE 1) --------------------
# TA TODO: SPEC OUT 1-2 SPECIFIC TEST CASES AND ADD A DOCTRING TO GUIDE STUDENTS THROUGH THIS
# Ideas (pick one):
# - Selling a ticket with price <= 0 records price 0 (still records if quantity > 0)
# - StudentTicket with price <= 0 always costs 0 even with discount
# - event_summary on an event that was never sold returns (0, 0)
#
class TestStudentWritten(unittest.TestCase):
    # TODO: write 1 test case here
    pass


def main():
    unittest.main(verbosity=2)


if __name__ == "__main__":
    main()
