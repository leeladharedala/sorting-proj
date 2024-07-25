import stringreverse
import unittest

from stringreverse import reverse
class TestReverseFunction(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse("Leela"), "aleeL")
    def test_reverse1(self):
        self.assertEqual(reverse(""), "")
    def test_reverse2(self):
        self.assertEqual(reverse(23), 32)
    def test_reverse3(self):
        self.assertEqual(reverse("madam"), "madam")


if __name__ == "__main__":
    unittest.main()