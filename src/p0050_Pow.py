import math

class Solution(object):
    def __init__(self):
        self.myPow = self.myPow_01

    def myPow_01(self, x, n):
        # return x**n
        return math.pow(x, n)

    # Your runtime beats 62.45% of pythonsubmissions.
    def myPow_02(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        if n == 1:
            return x
        if n == -1:
            return 1 / x

        def _pow_(x, n):
            n_half = n >> 1
            if n_half == 1:
                pow_half = x
            else:
                pow_half = _pow_(x, n_half)
            if n % 2 == 0:
                return pow_half * pow_half
            return pow_half * pow_half * x

        if n > 0:
            return _pow_(x, n)
        return 1 / _pow_(x, -n)


    # Your runtime beats 36.21% of pythonsubmissions.
    def myPow_03(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        if n == 1:
            return x
        if n == -1:
            return 1 / x

        def _pow_(x, n):
            if n == 1:
                return x
            if n % 2 == 0:
                return _pow_(x * x, n >> 1)
            return _pow_(x * x, n >> 1) * x

        if n > 0:
            return _pow_(x, n)
        return 1 / _pow_(x, -n)


def sets_gen(myPow=None):
    import random
    test_sets = []

    for i in range(1000):
        x = random.uniform(-10.0, 10.0)
        n = random.randint(-100, 100)
        match = myPow(x, n)
        test_sets.append((x, n, match))

    return test_sets

def test(myPow=None, test_sets=None, msg=None):

    def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
        return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

    for x, n, match in test_sets:
        try:
            assert(isclose(myPow(x, n), match))
        except AssertionError as ex:
            print(x, n, match, myPow(x, n))
            print(msg, '--> Assertion Error <--')

def test_spd(myPow=None, test_sets=None):
    for x, n, match in test_sets:
        myPow(x, n)


if __name__ == '__main__':
    sol = Solution()
    # prep
    print('prep...')
    test_sets = sets_gen(sol.myPow)
    # test
    print('test...')
    test(sol.myPow_01, test_sets, '01')
    test(sol.myPow_02, test_sets, '02')
    test(sol.myPow_03, test_sets, '03')
    print('test_spd...')
    _stmt_ = 'test_spd(sol.myPow_{0:02d}, test_sets)'
    _setup_ = 'from __main__ import test_spd, test_sets, sol'
    _number_ = 100
    from timeit import timeit
    print(timeit(stmt=_stmt_.format(1), setup=_setup_, number=_number_))
    print(timeit(stmt=_stmt_.format(2), setup=_setup_, number=_number_))
    print(timeit(stmt=_stmt_.format(3), setup=_setup_, number=_number_))
