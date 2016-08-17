class Solution(object):
    def __init__(self):
        self.plusOne = self.plusOne_01

    # Your runtime beats 72.95% of pythonsubmissions.
    def plusOne_01(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = digits[::-1]

        for i in range(len(digits)):
            digits[i] += 1
            if digits[i] < 10:
                break
            else:
                digits[i] = 0

        if digits[-1] == 0:
            return [1, ] + digits[::-1]

        return digits[::-1]

    # Your runtime beats 72.95% of pythonsubmissions.
    def plusOne_02(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = list(digits)
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] < 10:
                break
            else:
                digits[i] = 0

        if digits[0] == 0:
            return [1, ] + digits

        return digits

    # Your runtime beats 28.47% of pythonsubmissions.
    def plusOne_03(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return map(int, list(str(int(''.join(map(str, digits))) + 1)))


def sets_gen(plusOne):
    import random
    test_sets = []

    for i in range(1, 11):
        digits = [random.randint(0, 9) for _ in range(i)]
        match = plusOne(digits)
        test_sets.append((digits, match))

    return test_sets


def test(plusOne, test_sets, msg):
    for digits, match in test_sets:
        try:
            assert (plusOne(digits) == match)
        except AssertionError as ex:
            print(digits, match, plusOne(digits))
            print(msg, '--> Assertion Error <--')


def test_spd(plusOne, test_sets):
    for digits, _ in test_sets:
        plusOne(digits)


if __name__ == '__main__':
    sol = Solution()
    # prep
    print('prep...')
    test_sets = sets_gen(sol.plusOne)
    # test
    print('test...')
    test(sol.plusOne_01, test_sets, '01')
    test(sol.plusOne_02, test_sets, '02')
    test(sol.plusOne_03, test_sets, '03')
    # test_spd
    print('test_spd...')
    import timeit

    _stmt_ = 'test_spd(sol.plusOne_{0:02d}, test_sets)'
    _setup_ = 'from __main__ import sol, test_sets, test_spd'
    _number_ = 1000

    print(timeit.timeit(stmt=_stmt_.format(01), setup=_setup_, number=_number_))
    print(timeit.timeit(stmt=_stmt_.format(02), setup=_setup_, number=_number_))
    print(timeit.timeit(stmt=_stmt_.format(03), setup=_setup_, number=_number_))
