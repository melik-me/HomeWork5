import unittest

from Year_and_Existance import is_year_leap, does_it_exist
from Who_are_you_dude import who_are_you_dude

class TestYear(unittest.TestCase):

# Testing is_year_leap

    def test_0(self):
        res = is_year_leap(0)
        self.assertTrue(res)

    def test_1(self):
        res = is_year_leap(1)
        self.assertFalse(res)

    def test__1(self):
        self.assertFalse(is_year_leap(-1))

    def test_4(self):
        self.assertTrue(is_year_leap(4))

    def test_100(self):
        self.assertFalse(is_year_leap(100))

    def test_400(self):
        self.assertTrue(is_year_leap(400))

    def test_4000(self):
        self.assertTrue(is_year_leap(4000))

    def test__4(self):
        self.assertTrue(is_year_leap(-4))

    def test__100(self):
        self.assertFalse(is_year_leap(-100))

    def test__400(self):
        self.assertTrue(is_year_leap(-400))

    def test__4000(self):
        self.assertTrue(is_year_leap(-4000))

# Testing does_it_exist

    def test_ab_c(self):
        self.assertTrue(does_it_exist(3, 4, 5))

    def test_ac_b(self):
        self.assertTrue(does_it_exist(3, 5, 4))

    def test_bc_a(self):
        self.assertTrue(does_it_exist(4, 5, 3))

    def test_a_b_c(self):
        self.assertTrue(does_it_exist(3, 3, 3))

    def test_aequalsb_c(self):
        self.assertTrue(does_it_exist(4, 4, 7))

    def test_aequalsc_b(self):
        self.assertTrue(does_it_exist(4, 7, 4))

    def test_bequalsc_a(self):
        self.assertTrue(does_it_exist(7, 4, 4))

    def test_a_is_larger(self):
        self.assertFalse(does_it_exist(8, 4, 4))

    def test_b_is_larger(self):
        self.assertFalse(does_it_exist(4, 9, 4))

    def test_c_is_larger(self):
        self.assertFalse((does_it_exist(3, 3, 7)))

# Testing who_are_you_dude

    def test_equilateral(self):
        self.assertEqual(who_are_you_dude(9, 9, 9), "Equilateral triangle")

    def test_isosceles_ab_c(self):
        self.assertEqual(who_are_you_dude(5, 5, 9), "Isosceles triangle")

    def test_isosceles_ac_b(self):
        self.assertEqual(who_are_you_dude(10, 15, 10), "Isosceles triangle")

    def test_isosceles_bc_a(self):
        self.assertEqual(who_are_you_dude(20, 100, 100), "Isosceles triangle")

    def test_versatile(self):
        self.assertEqual(who_are_you_dude(300, 400, 500), "Versatile triangle")

    def test_not_a_triangle(self):
        self.assertEqual(who_are_you_dude(18, 19, 40), "Not a triangle")

if __name__ == "__main__":
    unittest.main()