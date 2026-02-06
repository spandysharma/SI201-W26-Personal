# Name:
# Student ID:
# Email:
# Who or what you worked with on this homework (including generative AI like ChatGPT):
# If you worked with generative AI also add a statement for how you used it.
# e.g.:
# Asked ChatGPT hints for debugging and suggesting the general structure of the code
# Did your use of GenAI on this assignment align with your goals and guidelines in 
#    your Gen AI contract? If not, why?

import random
import io
from contextlib import redirect_stdout


class CouponDispenser:
    """
    CouponDispenser manages a box of coupon cards and assigns one coupon
    to each unique name entered by the user during a session.

    Required attributes (initialized in __init__):
      - coupon_cards: list[str]              # all possible coupon texts
      - customer_roster: list[str]             # names in order of assignment
      - issued_indices: list[int]           # indices into coupon_cards aligned to customer_roster

    """

    def __init__(self, coupon_cards):
        """
        Initialize a new CouponDispenser object.

        Args:
            coupon_cards (list[str]): list of possible coupons users can receive.
        """
        # TODO: Implement per instructions
        pass

    def __str__(self):
        """
        Return a single string with all coupons in coupon_cards joined by pipes ('|').
        If coupon_cards is empty, return an empty string "".

        Returns:
            str
        """
        # TODO: Implement per instructions
        pass

    def issue_coupon(self, name):
        """
        Assign name with a random coupon. If name is already assigned a coupon, return it.
        If the list coupon_cards is empty, return:
        "The box is empty."

        Important: Do not use dictionaries in this method.

        Args:
            name (str): customer name (trimmed, non-empty)

        Returns:
            str: message as described above
        """
        # TODO: Implement per instructions
        pass

    def distribute_session(self):
        """
        Run the "coupon dispenser" session.

        The program will loop asking you to enter a customer name (or names), show, or exit.  
        - If you type exit (exact spelling) the program will print "Goodbye!" and stop.  
        - If you enter one or more customer names (separated by commas).
           * A coupon will be picked at random from a list of coupons for each name 
           if that name doesn't already have an assigned coupon. 
        - If you type show (exact spelling) it will display a string with each customer's name and coupon.

        See the instructions for more details.

        Reminder: Use lists only (no dictionaries).
        """
        # TODO: Implement per instructions 
        pass

    def tally_distribution(self):
        """
        Extra credit:
        Print coupon distribution counts (NO sorting) using ONLY lists.

          - If issued_indices is empty:
              * print("Empty")
              * return
          - Otherwise:
              * For each coupon in coupon_cards (in original order), print:
                    "<coupon> distribution count: <count>."

        Returns:
            None
        """
        # TODO: Implement per instructions
        pass


def main():
    """
    Driver function:
      - Define the coupon_cards list (example coupons below)
      - Create a CouponDispenser
      - Start the interaction via distribute_session()
      - After exit, call tally_distribution() to print the distribution in the terminal
    """
    coupon_cards = [
        "10% off",
        "Free small coffee",
        "Buy 1 get 1 half off",
        "Free extra espresso shot",
    ]

    # Uncomment the lines below as you implement each function.
    # box = CouponDispenser(coupon_cards)
    # box.distribute_session()
    # box.tally_distribution()
    pass


# -----------------------
# Tests (about 3–4 per function)
# -----------------------

def _capture_session_output(box, inputs):
    """
    Helper to simulate interactive input/print for distribute_session().
    - `inputs` is a list of strings that will be returned by input() in order.
    - This function returns the captured stdout as a string.
    """
    stream = io.StringIO()
    it = iter(inputs)

    def fake_input(prompt=""):
        # Echo prompts so they appear in captured output
        print(prompt, end="")
        try:
            return next(it)
        except StopIteration:
            return "exit"

    original_input = __builtins__.input
    try:
        __builtins__.input = fake_input
        with redirect_stdout(stream):
            box.distribute_session()
    finally:
        __builtins__.input = original_input
    return stream.getvalue()


def test():
    """
    Comprehensive test suite that checks each function with 3–4 cases.
    These tests use simple asserts and captured output. They assume
    correct implementations of the methods per the spec.
    """
    total, passed = 0, 0

    def check(condition, msg):
        nonlocal total, passed
        total += 1
        if condition:
            passed += 1
            print(f"[PASS] {msg}")
        else:
            print(f"[FAIL] {msg}")

    # ---------- Tests for __init__ ----------
    notes_base = ["A", "B", "C"]
    box = CouponDispenser(notes_base)
    try:
        check(hasattr(box, "coupon_cards") and hasattr(box, "customer_roster") and hasattr(box, "issued_indices"),
              "__init__: attributes exist")
        check(box.coupon_cards == notes_base, "__init__: coupon_cards assigned")
        check(isinstance(box.customer_roster, list) and box.customer_roster == [], "__init__: customer_roster empty list")
        check(isinstance(box.issued_indices, list) and box.issued_indices == [], "__init__: issued_indices empty list")
        check(len(box.customer_roster) == len(box.issued_indices), "__init__: invariant lengths align")
    except Exception as e:
        check(False, f"__init__: unexpected exception {e}")

    # ---------- Tests for __str__ ----------
    try:
        box_empty = CouponDispenser([])
        check(str(box_empty) == "", "__str__: empty list returns empty string")
        box_single = CouponDispenser(["Only"])
        check(str(box_single) == "Only", "__str__: single element returns itself")
        box_multi = CouponDispenser(["X", "Y", "Z"])
        check(str(box_multi) == "X|Y|Z", "__str__: multi elements joined by pipes")
        _ = str(box_multi)
        check(box_multi.coupon_cards == ["X", "Y", "Z"], "__str__: does not modify coupon_cards")
    except Exception as e:
        check(False, f"__str__: unexpected exception {e}")

    # ---------- Tests for issue_coupon ----------
    try:
        # Test empty coupon_cards
        box_empty = CouponDispenser([])
        msg_empty = box_empty.issue_coupon("Test")
        check(msg_empty == "The box is empty.", "issue_coupon: empty coupon_cards returns correct message")
        
        # Test new name assignment
        random.seed(42)
        box2 = CouponDispenser(["N1", "N2"])
        msg1 = box2.issue_coupon("Ava")
        check("N" in msg1 and len(box2.customer_roster) == 1 and len(box2.issued_indices) == 1,
              "issue_coupon: assigns to new name and updates lists")
        
        # Test duplicate name (re-report)
        before_len = (len(box2.customer_roster), len(box2.issued_indices))
        msg2 = box2.issue_coupon("Ava")
        after_len = (len(box2.customer_roster), len(box2.issued_indices))
        check(msg2.startswith("That name already has a coupon:"),
              "issue_coupon: duplicate name message")
        check(before_len == after_len, "issue_coupon: duplicate does not change state")
        check("N1" in msg2 or "N2" in msg2, "issue_coupon: duplicate returns existing coupon")
        
        # Test name order preserved and alignment
        _ = box2.issue_coupon("Ben")
        check(box2.customer_roster == ["Ava", "Ben"], "issue_coupon: name order preserved")
        check(len(box2.customer_roster) == len(box2.issued_indices), 
              "issue_coupon: customer_roster and issued_indices stay aligned after append")
        check(box2.customer_roster[0] == "Ava" and box2.customer_roster[1] == "Ben",
              "issue_coupon: appends new names to customer_roster correctly")
        check(len(box2.issued_indices) == 2 and all(isinstance(i, int) for i in box2.issued_indices),
              "issue_coupon: appends chosen index to issued_indices correctly")
        
        # Test that different people can get the same coupon (repeats allowed)
        random.seed(999)
        box_repeat = CouponDispenser(["Coupon1"])
        msg_a = box_repeat.issue_coupon("Alice")
        msg_b = box_repeat.issue_coupon("Bob")
        check(box_repeat.issued_indices == [0, 0], "issue_coupon: allows same coupon for different people")
        check(msg_a == msg_b == "Coupon1", "issue_coupon: same coupon text returned for different people")
        check(len(box_repeat.customer_roster) == len(box_repeat.issued_indices),
              "issue_coupon: customer_roster and issued_indices aligned when repeats allowed")
        
        # Test empty box message (when all coupons are used up - but this shouldn't happen now)
        # Actually, with new behavior, we can always assign coupons, so this test is removed
    except Exception as e:
        check(False, f"issue_coupon: unexpected exception {e}")

    # ---------- Tests for distribute_session ----------
    try:
        random.seed(123)
        notes3 = ["Coupon A", "Coupon B", "Coupon C"]
        box3 = CouponDispenser(notes3)
        out1 = _capture_session_output(box3, ["Ava, Ben", "show", "exit"])
        check(box3.customer_roster == ["Ava", "Ben"], "distribute_session: comma-separated assigns two names")
        check(("Ava:" in out1) and ("Ben:" in out1), "distribute_session: 'show' shows both names")
        check("Goodbye!" in out1, "distribute_session: prints goodbye on exit")
        check("Round 1 - Enter a name (or a comma-separated list), or type 'show' or 'exit': " in out1,
              "distribute_session: initial prompt is correct")
        check("Round 2 - Enter a name (or a comma-separated list), or type 'show' or 'exit': " in out1,
              "distribute_session: round number increments correctly")
        check("Round 3 - Enter a name (or a comma-separated list), or type 'show' or 'exit': " in out1,
              "distribute_session: round number continues to increment")

        # Test duplicate name handling
        box4 = CouponDispenser(["N1", "N2", "N3"])
        out2 = _capture_session_output(box4, ["Ava", "Ava", "exit"])
        check("That name already has a coupon:" in out2, "distribute_session: duplicate name message printed")

        # Test empty coupon_cards
        box_empty_session = CouponDispenser([])
        out_empty = _capture_session_output(box_empty_session, ["Test", "exit"])
        check("The box is empty." in out_empty,
              "distribute_session: prints empty-box message when coupon_cards is empty")

        # Test comma-separated with empty/whitespace pieces
        box5 = CouponDispenser(["G1", "G2"])
        out3 = _capture_session_output(box5, ["A, , B,  , C", "exit"])
        check(box5.customer_roster == ["A", "B", "C"], "distribute_session: ignores empty pieces in comma-separated input")
    except Exception as e:
        check(False, f"distribute_session: unexpected exception {e}")

    # ---------- Tests for tally_distribution ----------
    try:
        # Test empty case
        box6 = CouponDispenser(["h1", "h2"])
        buf = io.StringIO()
        with redirect_stdout(buf):
            box6.tally_distribution()
        printed = buf.getvalue()
        check("Empty" in printed, "tally_distribution: empty case prints 'Empty'")

        # Test printing format and original order (no sorting)
        box7 = CouponDispenser(["A1", "A2", "A3"])
        box7.customer_roster = ["X", "Y", "Z"]
        box7.issued_indices = [2, 1, 2]  # A3: 2 times, A2: 1 time, A1: 0 times
        buf7 = io.StringIO()
        with redirect_stdout(buf7):
            box7.tally_distribution()
        printed7 = buf7.getvalue()
        check("A1 distribution count: 0." in printed7, "tally_distribution: prints A1 with count 0")
        check("A2 distribution count: 1." in printed7, "tally_distribution: prints A2 with count 1")
        check("A3 distribution count: 2." in printed7, "tally_distribution: prints A3 with count 2")
        # Check order: should be in original order (A1, A2, A3), not sorted
        idx_a1 = printed7.find("A1")
        idx_a2 = printed7.find("A2")
        idx_a3 = printed7.find("A3")
        check(idx_a1 < idx_a2 < idx_a3, "tally_distribution: prints in original order (no sorting)")

        # Test with single coupon
        box8 = CouponDispenser(["MiXeD"])
        box8.customer_roster = ["p", "q"]
        box8.issued_indices = [0, 0]
        buf8 = io.StringIO()
        with redirect_stdout(buf8):
            box8.tally_distribution()
        printed8 = buf8.getvalue()
        check("coupon: MiXeD is distributed 2 times." in printed8,
              "tally_distribution: prints correct format with mixed case")

        # Test multiple coupons with same count (should stay in original order)
        box9 = CouponDispenser(["Banana", "Apple", "Cherry"])
        box9.customer_roster = ["a", "b", "c"]
        box9.issued_indices = [0, 1, 2]  # Each coupon used once
        buf9 = io.StringIO()
        with redirect_stdout(buf9):
            box9.tally_distribution()
        printed9 = buf9.getvalue()
        idx_banana = printed9.find("Banana")
        idx_apple = printed9.find("Apple")
        idx_cherry = printed9.find("Cherry")
        check(idx_banana < idx_apple < idx_cherry,
              "tally_distribution: maintains original order even with same counts")
    except Exception as e:
        check(False, f"tally_distribution: unexpected exception {e}")

    # ---------- Tests for main() ----------
    try:
        # Test that main() properly defines coupon_cards list
        import inspect
        main_source = inspect.getsource(main)
        check("coupon_cards" in main_source and "=" in main_source.split("coupon_cards")[1][:50],
              "main: coupon_cards list is properly defined")
        
        # Test that main() constructs CouponDispenser
        check("CouponDispenser" in main_source and "(" in main_source.split("CouponDispenser")[1][:20],
              "main: CouponDispenser is properly constructed")
        
        # Test that main() calls distribute_session
        check("distribute_session" in main_source and "()" in main_source.split("distribute_session")[1][:10],
              "main: distribute_session is called correctly")
        
        # Test that main() calls tally_distribution (extra credit)
        check("tally_distribution" in main_source and "()" in main_source.split("tally_distribution")[1][:10],
              "main: tally_distribution is called correctly (extra credit)")
        
        # Test actual execution of main() with captured output
        buf_main = io.StringIO()
        it_main = iter(["exit"])  # Just exit immediately
        
        def fake_input_main(prompt=""):
            print(prompt, end="", file=buf_main)
            try:
                return next(it_main)
            except StopIteration:
                return "exit"
        
        original_input_main = __builtins__.input
        try:
            __builtins__.input = fake_input_main
            with redirect_stdout(buf_main):
                main()
        finally:
            __builtins__.input = original_input_main
        
        main_output = buf_main.getvalue()
        check("Round 1" in main_output, "main: distribute_session is executed")
        check("Goodbye!" in main_output, "main: session runs and exits correctly")
    except Exception as e:
        check(False, f"main: unexpected exception {e}")

    # ---------- Tests for tally_distribution in main() (Extra Credit) ----------
    try:
        # Test that tally_distribution output would be displayed in main()
        # This is tested by checking that main() calls tally_distribution
        # and that the function prints (which we already test above)
        box_tally_main = CouponDispenser(["Test1", "Test2"])
        box_tally_main.customer_roster = ["A"]
        box_tally_main.issued_indices = [0]
        buf_tally_main = io.StringIO()
        with redirect_stdout(buf_tally_main):
            box_tally_main.tally_distribution()
        tally_output = buf_tally_main.getvalue()
        check("is distributed" in tally_output, 
              "tally_distribution: output format correct for main() display")
    except Exception as e:
        check(False, f"tally_distribution in main: unexpected exception {e}")

    print(f"\nTests passed: {passed}/{total}")


if __name__ == "__main__":
    main()
    # test()

