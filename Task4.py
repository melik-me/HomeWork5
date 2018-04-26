import unittest

from Task1 import ITEmployee

class Test_ITEmployee(unittest.TestCase):

    def test_name_correct(self):
        p = ITEmployee("John Doe")
        self.assertEqual(p.name(), "John")

    def test_name_1word(self):
        p = ITEmployee("John")
        self.assertEqual(p.name(), "John")

    def test_surname_correct(self):
        p = ITEmployee("John Doe")
        self.assertEqual(p.surname(), "Doe")

    def test_surname_1word(self):
        p = ITEmployee("John")
        self.assertEqual(p.surname(), "Doe")

    def test_how_old_default(self):
        p = ITEmployee("John Doe")
        self.assertEqual(p.how_old(), 117)

    def test_how_old_value(self):
        p = ITEmployee("John Doe", 1936)
        self.assertEqual(p.how_old(2020), 84)

    def test_rank_junior(self):
        p = ITEmployee("Judy Doe", 1936, "old stager", 2, 100500)
        self.assertEqual(p.rank(), "Junior old stager")

    def test_rank_middle(self):
        p = ITEmployee("Judy Doe", 1936, "old stager", 5, 100500)
        self.assertEqual(p.rank(), "Middle old stager")

    def test_rank_senior(self):
        p = ITEmployee("Judy Doe", 1936, "old stager", 90, 100500)
        self.assertEqual(p.rank(), "Senior old stager")

    def test_cash_rain(self):
        p = ITEmployee("Judy Doe", 1936, "old stager", 2, 100500)
        p.cash_rain(899499)
        self.assertEqual(p.salary, 999999)

    def test_add_skills(self):
        p = ITEmployee("Judy Doe", 1936, "old stager", 2, 100500)
        p.add_skills("communication", "head recruiting", "word", "excel", "instagram")
        self.assertEqual(p.skills, ["communication", "head recruiting", "word", "excel", "instagram"])


if __name__ == "__main__":
    unittest.main()