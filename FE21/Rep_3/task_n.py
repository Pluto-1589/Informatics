import unittest


class MyTestSuite(unittest.TestCase):

    # is_palindrome takes a string as parameter x and determines if it is a palindrome. It returns True if yes, otherwise False.

    # If x is not a string, a TypeError is raised.

    # If x is less than 3 characters long, a ValueError is raised.

    def test_is_palindrome(self):

        expected = True
        actual = is_palindrome("maoam")

        self.assertEqual(expected, actual)

    def test_is_not_palindrome(self):
        expected = False
        actual = is_palindrome("I don't know")

        self.assertEqual(expected, actual)

    def test_len(self):

        with self.assertRaises(TypeError):
            is_palindrome("xo")

    def test_type(self):

        with self.assertRaises(ValueError):
            is_palindrome(123)

    def test_empty(self):

        with self.assertRaises(ValueError):
            is_palindrome("")

    def test_case_insensitive(self):

        expected = True
        actual = is_palindrome("Was it a car or a cat I saw?")

        self.assertEqual(expected, actual)

    def test_special_char(self):

        expected = True
        actual = is_palindrome("Was it a car or a cat I saw?")

        self.assertEqual(expected, actual)


# Solutions

class MyTestSuite(unittest.TestCase):
    def test_len_3(self):
        self.assertTrue(is_palindrome("bob"))

    def test_len_less_than_3_raises_ValueError(self):
        with self.assertRaises(ValueError):
            self.assertTrue(is_palindrome("aa"))

    def test_basic(self):
        self.assertTrue(is_palindrome("atoyota"))

    def test_with_nonalpha(self):
        self.assertTrue(is_palindrome("a toyota!"))

    def test_with_mixed_casing(self):
        self.assertTrue(is_palindrome("AToyoTa"))

    def test_false(self):
        self.assertFalse(is_palindrome("Honda"))

    def test_rejects_non_string(self):
        with self.assertRaises(TypeError):
            is_palindrome(True)
