from math import ceil
import unittest


def get_sum_of_proper_divisors(n: int)->int:
    sum = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            sum += i
    return sum


class TestMethods(unittest.TestCase):
    def test_get_sum_of_proper_divisors(self):
        self.assertEqual(get_sum_of_proper_divisors(12), 16)
        self.assertEqual(get_sum_of_proper_divisors(6), 6)


def is_abundant(n: int)->bool:
    return get_sum_of_proper_divisors(n) > n


def main():
    MAX_LIMIT = 28124
    MIN_ABUNDANT_NUM = 12
    abundant = [is_abundant(i) for i in range(28124)]
    dic = {i: False for i in range(1, MAX_LIMIT)}
    for i in range(MIN_ABUNDANT_NUM, len(abundant)):
        if abundant[i]:
            for j in range(i, len(abundant)):
                if abundant[j]:
                    dic[i + j] = True
    print(sum((i for i, can_be_written in dic.items() if not can_be_written)))


if __name__ == '__main__':
    # unittest.main()
    main()
