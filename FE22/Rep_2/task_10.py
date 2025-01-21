from unittest import TestCase


def count_booleans(booleans):
    return booleans.count(True), booleans.count(False), len(booleans)


class TestSuite(TestCase):

    def test_num_true(self):
        # The number of Trues is incorrect
        expected = (2, 1, 2)[0]
        actual = count_booleans([True, True, False, 3])[0]

        self.assertEqual(expected, actual)

    def test_num_false(self):
        # The number of Falses is incorrect
        expected = (2, 1, 2)[1]
        actual = count_booleans([True, True, False, 3])[1]

        self.assertEqual(expected, actual)

    # fails
    def test_num_elements(self):
        # The total number of elements is incorrect
        expected = (2, 1, 4)[2]
        actual = count_booleans([True, True, False, 3][2])

        self.assertEqual(expected, actual)
