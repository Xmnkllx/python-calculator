import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # ---------- add() (2) ----------
    def test_add_with_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-3, 5), 2)

    # ---------- subtract() (2) ----------
    def test_subtract_positive(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)      # catches b - a bug

    def test_subtract_negative_result(self):
        self.assertEqual(self.calc.subtract(2, 5), -3)

    # ---------- multiply() (2) ----------
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)

    # ---------- divide() (2) ----------
    def test_divide(self):
        self.assertEqual(self.calc.divide(5, 2), 2)

    def test_divide_exact(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    # ---------- modulo() (2) ----------
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)

    def test_modulo_exact(self):
        self.assertEqual(self.calc.modulo(10, 5), 0)

    # ---------- Extra: fault-detecting / sign combinations ----------
    def test_multiply_negative_b(self):                    # catches negative-b bug
        self.assertEqual(self.calc.multiply(3, -4), -12)

    def test_multiply_all_signs(self):
        for a, b, exp in [(3, 4, 12), (3, -4, -12), (-3, 4, -12), (-3, -4, 12)]:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.multiply(a, b), exp)

    def test_divide_all_signs(self):
        for a, b, exp in [(7, 2, 3), (7, -2, -4), (-7, 2, -4), (-7, -2, 3),
                          (6, -3, -2), (-6, 3, -2), (-6, -3, 2), (0, 5, 0)]:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.divide(a, b), exp)

    def test_modulo_all_signs(self):
        for a, b, exp in [(7, 3, 1), (7, -3, -2), (-7, 3, 2), (-7, -3, -1),
                          (6, -3, 0), (-6, 3, 0), (2, 5, 2), (0, 5, 0)]:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.modulo(a, b), exp)

    def test_add_subtract_all_signs(self):
        for a in (-4, 0, 4):
            for b in (-3, 0, 3):
                with self.subTest(a=a, b=b):
                    self.assertEqual(self.calc.add(a, b), a + b)
                    self.assertEqual(self.calc.subtract(a, b), a - b)

    def test_matches_python_operators_exhaustive(self):
        for a in range(-12, 13):
            for b in range(-12, 13):
                with self.subTest(a=a, b=b):
                    self.assertEqual(self.calc.add(a, b), a + b)
                    self.assertEqual(self.calc.subtract(a, b), a - b)
                    self.assertEqual(self.calc.multiply(a, b), a * b)
                    if b != 0:
                        self.assertEqual(self.calc.divide(a, b), a // b)
                        self.assertEqual(self.calc.modulo(a, b), a % b)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)

    def test_modulo_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.modulo(5, 0)


if __name__ == '__main__':
    unittest.main()