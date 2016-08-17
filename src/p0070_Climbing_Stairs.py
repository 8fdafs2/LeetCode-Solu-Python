class Solution(object):
    def __init__(self):
        self.climbStairs = self.climbStairs_01

    # Fibonacci number:
    # f(0) = 0
    # f(1) = 1
    # f(2) = 2
    # f(n) = f(n-1) + f(n-2) while n >= 3
    # Fibonacci number generation
    def climbStairs_01(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        f = [0, 1, 2] + [0] * (n - 2)
        for i in range(3, n + 1):
            f[i] = f[i - 1] + f[i - 2]
        return f[n]

    # Fibonacci number:
    # f(0) = 0
    # f(1) = 1
    # f(2) = 2
    # f(n) = f(n-1) + f(n-2) while n >= 3
    # Fibonacci number generation
    def climbStairs_02(self, n):
        """
        :type n: int
        :rtype: int
        """
        f_n_minus_2 = 1  # f(1)
        f_n_minus_1 = 2  # f(2)
        if n == 1:
            return f_n_minus_2
        if n == 2:
            return f_n_minus_1
        fn = 0
        for i in range(2, n):
            fn = f_n_minus_1 + f_n_minus_2
            f_n_minus_2 = f_n_minus_1
            f_n_minus_1 = fn
        return fn

    # Time Limit Exceeded
    def climbStairs_03(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.nret_climbStairs = 0

        def recur(n):
            if n == 0:
                self.nret_climbStairs += 1
                return
            if n >= 1:
                recur(n - 1)
            if n >= 2:
                recur(n - 2)

        recur(n)

        return self.nret_climbStairs

        # ret = []
        #
        # def recur(cur, n):
        #     if n == 0:
        #         ret.append(cur)
        #         return
        #     if n >= 1:
        #         recur(cur + '1', n - 1)
        #     if n >= 2:
        #         recur(cur + '2', n - 2)
        #
        # recur('', n)
        #
        # return ret


def test(climbStairs=None, test_sets=None):
    for n, match in test_sets:
        try:
            assert (climbStairs(n) == match)
        except AssertionError as ex:
            print(n, match, climbStairs(n))
            print(ex)


def test_spd(climbStairs=None, test_sets=None):
    for n, match in test_sets:
        climbStairs(n)


def sets_get(climbStairs=None):
    test_sets = []

    for n in range(1, 500):
        match = climbStairs(n)
        test_sets.append((n, match))

    return test_sets


if __name__ == '__main__':
    # prep
    print('prep...')
    sol = Solution()
    test_sets = sets_get(sol.climbStairs)

    # test
    print('test...')
    test(sol.climbStairs_01, test_sets)
    test(sol.climbStairs_02, test_sets)
    # test(sol.climbStairs_03, test_sets)

    # test_spd
    print('test_spd...')
    _stmt_ = 'test_spd(sol.climbStairs_{:02d}, test_sets)'
    _setup_ = 'from __main__ import sol, test_spd, test_sets'
    _number_ = 100

    import timeit

    print(timeit.timeit(stmt=_stmt_.format(1), setup=_setup_, number=_number_))
    print(timeit.timeit(stmt=_stmt_.format(2), setup=_setup_, number=_number_))
    # print(timeit.timeit(stmt=_stmt_.format(3), setup=_setup_, number=_number_))
