import unittest

import Anagrammod
from Anagrammod import anagram

class TestAnagramFunction(unittest.TestCase):

    def test_anagram_true(self):
        self.assertEqual(anagram("triangle", "integral"), "Anagram")
        self.assertEqual(anagram("listen", "silent"), "Anagram")
        self.assertEqual(anagram("evil", "vile"), "Anagram")
        self.assertEqual(anagram("cinema", "iceman"), "Anagram")

    def test_anagram_false(self):
        self.assertEqual(anagram("banana", "apple"), "Not an Anagram")
        self.assertEqual(anagram("hello", "world"), "Not an Anagram")
        self.assertEqual(anagram("abc", "def"), "Not an Anagram")
        self.assertEqual(anagram("abcd", "abce"), "Not an Anagram")

    def test_anagram_empty_strings(self):
        self.assertEqual(anagram("", ""), "Anagram")

    def test_anagram_case_sensitive(self):
        self.assertEqual(anagram("Triangle", "integral"), "Not an Anagram")
        self.assertEqual(anagram("Listen", "Silent"), "Not an Anagram")
        self.assertEqual(anagram("Evil", "Vile"), "Not an Anagram")
        self.assertEqual(anagram("Cinema", "Iceman"), "Not an Anagram")

if __name__ == "__main__":
    unittest.main()
