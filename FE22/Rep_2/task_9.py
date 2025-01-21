from unittest import TestCase


def min_max_mean(values):
    from statistics import mean
    return min(values), max(values), mean(values)


class TestSuite(TestCase):
    # The minimum value is incorrect
    def test_min_val(self):
        expected = (1, 3, 2)[0]
        actual = min_max_mean([1, 2, 3])[0]
        self.assertEqual(expected, actual)

    # The maximum value is incorrect
    # failing
    def test_max_val(self):
        expected = (3, 1, 2)[1]
        actual = min_max_mean([1, 2, 3])[1]
        self.assertEqual(expected, actual)

    # The mean value is incorrect
    def test_mean_val(self):
        expected = (1, 3, 2)[2]
        actual = min_max_mean([1, 2, 3])[2]
        self.assertEqual(expected, actual)


# Solution

def min_max_mean(values):
    from statistics import mean
    return min(values), max(values), mean(values)


class TestSuite(TestCase):
    def test_min(self):
        actual = min_max_mean([1, 2, 3])
        expected = 1
        self.assertEqual(expected, actual[0])

    def test_max(self):
        actual = min_max_mean([1, 2, 3])
        expected = 3
        self.assertEqual(expected, actual[1])

    def test_mean(self):
        actual = min_max_mean([1, 2, 3])
        expected = 2
        self.assertEqual(expected, actual[2])
