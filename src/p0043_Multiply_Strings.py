class Solution(object):
    def __init__(self):
        self.multiply = self.multiply_01

    # Your runtime beats 71.46% of pythonsubmissions.
    def multiply_01(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1) * int(num2))

    # Your runtime beats 70.86% of pythonsubmissions.
    def multiply_02(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        char2num_dict = {
            '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
            '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        }
        def num_get(numstr):
            _num_ = 0
            factor = 1
            for digit in reversed(numstr):
                _num_ += char2num_dict[digit] * factor
                factor *= 10
            return _num_
        return str(num_get(num1) * num_get(num2))

    # Your runtime beats 62.67% of pythonsubmissions.
    def multiply_03(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        char2num_dict = {
            '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
            '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        }
        num = 0
        factor1 = 1
        for digit_num1 in reversed(num1):
            digit_num1 = char2num_dict[digit_num1] * factor1
            factor1 *= 10
            factor2 = 1
            for digit_num2 in reversed(num2):
                digit_num2 = char2num_dict[digit_num2] * factor2
                factor2 *= 10
                num += digit_num1 * digit_num2
        return str(num)

    # Your runtime beats 63.87% of pythonsubmissions.
    def multiply_04(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        char2num_dict = {
            '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
            '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        }
        num1 = [char2num_dict[digit] for digit in num1][::-1]
        num2 = [char2num_dict[digit] for digit in num2][::-1]
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i + j] += num1[i] * num2[j]
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10
        return ''.join(map(str, res[::-1])).lstrip('0')


def sets_gen(multiply):
    import random
    test_sets = []
    for i in range(0, 100):
        for j in range(0, 100):
            num1 = str(random.randint(i, i + 10000))
            num2 = str(random.randint(j, j + 10000))
            match = multiply(num1, num2)
            test_sets.append((num1, num2, match))
    return test_sets


def test(multiply, test_sets, msg):
    for num1, num2, match in test_sets:
        try:
            assert (multiply(num1, num2) == match)
        except AssertionError as ex:
            print(num1, num2, match)
            print(msg, '--> AssertionError <--')


def test_spd(multiply, test_sets):
    for num1, num2, _ in test_sets:
        multiply(num1, num2)


if __name__ == '__main__':
    sol = Solution()
    # prep
    print('prep...')
    test_sets = sets_gen(sol.multiply)
    # test
    print('test...')
    test(sol.multiply_01, test_sets, '01')
    test(sol.multiply_02, test_sets, '02')
    test(sol.multiply_03, test_sets, '03')
    test(sol.multiply_04, test_sets, '04')
    # test_spd
    print('test_spd...')
    _stmt_ = 'test_spd(sol.multiply_{0:02d}, test_sets)'
    _setup_ = 'from __main__ import test_spd, sol, test_sets'
    _number_ = 100
    import timeit

    print(timeit.timeit(stmt=_stmt_.format(01), setup=_setup_, number=_number_))
    print(timeit.timeit(stmt=_stmt_.format(02), setup=_setup_, number=_number_))
    print(timeit.timeit(stmt=_stmt_.format(03), setup=_setup_, number=_number_))
    print(timeit.timeit(stmt=_stmt_.format(04), setup=_setup_, number=_number_))
