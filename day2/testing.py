import unittest

# reports are safe by this criteria
# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three. 1,2,3
from .main import check_if_list_increasing, check_if_list_decreasing


def test_list(x: list) -> bool:
    x_len = len(x)
    for i in range(x_len - 1):
        if x[i] == x[i + 1]:
            return False
        out = x[i] - x[i + 1]
        if out < 0:
            out = -out
        if out not in [1, 2, 3]:
            return False
    return True


# 5,4,3,2,1


class Test(unittest.TestCase):
    @unittest.skip("Skipped")
    def test_1(self):
        x = [22, 25, 27, 28, 30, 31, 32, 33]
        self.assertEqual(check_if_list_increasing(x), True)

    @unittest.skip("Skipped")
    def test_2(self):
        x = [5, 4, 3, 2, 1]
        self.assertEqual(check_if_list_decreasing(x), True)

    def test_3(self):
        x = [5, 4, 4]
        out = test_list(x)
        # for i in range(x_len - 1):
        #     if x[i] < x[i + 1]:
        #         out = x[i] - x[i + 1]
        #         if out in [1, 2, 3]:
        #             return True
        #     elif x[i] > x[i + 1]:
        #         out = x[i] - x[i + 1]
        #         if out in [1, 2, 3]:
        #             return True
        #     else:
        #         return False

        self.assertEqual(out, True)
