class Solution(object):

    # 123456
    # 123456 % 10 = 6
    # 123456 // 10 = 12345
    # 12345 % 10 = 5
    # 12345 // 10 = 1234
    # 1234 % 10 = 5
    # 1234 // 10 = 123
    # 123 % 10 = 3
    # 123 // 10 = 12
    # 12 % 10 = 2
    # 12 // 10 = 1
    # 1 % 10 = 1
    # 1 // 10 = 0

    def __init__(self):
        self.reverse = self.reverse_01

    # Your runtime beats 40.58% of pythonsubmissions.
    def reverse_01(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        if x < 0:
            x = -x
            negative = True

        digits = []
        while x > 0:
            digits.append(x % 10)
            x //= 10

        x_reversed = 0
        for digit in digits:
            x_reversed = x_reversed * 10 + digit

        if negative:
            x_reversed = -x_reversed

        if -2147483648 <= x_reversed <= 2147483647:
            return x_reversed

        return 0


def sets_gen(reverse):
    x_32bitoverflow = [-9463847412, -8463847412, -7463847412,
                       6463847412, 7463847412, 8463847412,
                       1000000003]
    import random
    x_list = x_32bitoverflow + [random.randint(-10000000, 10000000) for _ in range(1000)]
    test_sets = []
    for x in x_list:
        match = reverse(x)
        test_sets.append((x, match))
    return test_sets


def test(reverse, test_sets, msg):
    for x, match in test_sets:
        try:
            assert(reverse(x) == match)
        except AssertionError as ex:
            print(x, match, reverse(x))
            print(msg, '--> Assertion Error <--')


def test_spd(reverse, test_sets):
    for x, _ in test_sets:
        reverse(x)


if __name__ == '__main__':
    # prep
    print('prep...')
    sol = Solution()
    test_sets = sets_gen(sol.reverse)
    # test
    print('test...')
    test(sol.reverse_01, test_sets, '01')
    # test_spd
    print('test_spd...')
    _stmt_ = 'test_spd(sol.reverse_{:02d}, test_sets)'
    _setup_ = 'from __main__ import sol, test_spd, test_sets'
    _number_ = 1000
    import timeit
    print(timeit.timeit(stmt=_stmt_.format(1), setup=_setup_, number=_number_))