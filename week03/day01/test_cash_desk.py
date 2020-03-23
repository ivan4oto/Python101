import unittest
from cash_desk import Bill, BillBatch, CashDesk

class TestCashDesk(unittest.TestCase):
    def test_negative_amount_raises_ValueError(self):
        with self.assertRaises(ValueError): billtest = Bill(-1)

    def test_non_int_amount_raises_TypeError(self):
        with self.assertRaises(TypeError): billtest = Bill('edin lev')
    
    def test_equality_check_works(self):
        a = Bill(10)
        b = Bill(5)
        c = Bill(10)

        self.assertTrue((a == c) and (a != b))
    
    def test_string_representation(self):
        a = Bill(10)
        expectedResult = "A 10$ bill"
        result = str(a)

        self.assertEqual(result, expectedResult)
        
    def test_int_representation(self):
        a = Bill(20)
        b = int(a)
        c = 20

        self.assertEqual(b, c)

class TestBillBatch(unittest.TestCase):
    def test_length_function(self):
        values = [10, 20, 50, 100]
        bills = [Bill(value) for value in values]
        batch = BillBatch(bills)
        self.assertEqual(len(batch), 4)
    
    def test_total_returns_correct_result(self):
        values = [10, 20, 50, 100]
        bills = [Bill(value) for value in values]
        batch = BillBatch(bills)
        x = batch.total()

        self.assertEqual(x, 180)

    def test_getitem_indexing(self):
        pass

    
class TestCashDeskClass(unittest.TestCase):
    def test_total_works_with_bills(self):
        desk = CashDesk()
        desk.take_money(Bill(5))
        desk.take_money(Bill(10))
        desk.take_money(Bill(10))
        self.assertEqual(25, desk.total())

    def test_total_works_with_batch_bills(self):
        bills = [Bill(10), Bill(5), Bill(20)]
        batch = BillBatch(bills)
        desk = CashDesk()
        desk.take_money(batch)

        self.assertEqual(35, desk.total())

if __name__ == "__main__":
    unittest.main()