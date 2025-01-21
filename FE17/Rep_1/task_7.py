from unittest import TestCase


class testChange(TestCase):
    # 10$, 5$, 2$, 1$

    def test_up_to_100(self):

        self.assertEqual(amount(10, 0, 0, 0), None)

    def test_amount_3(self):

        self.assertEqual(amount(0, 0, 1, 1), 3)
