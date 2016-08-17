class Solution(object):
    def __init__(self):
        self.maxProfit = self.maxProfit_01

    #
    def maxProfit_01(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        price_min = 2147483647
        profit_max = 0
        for price in prices:
            price_min = min(price_min, price)
            profit_max = max(profit_max, price - price_min)
        return profit_max

    # Your runtime beats 87.64% of pythonsubmissions.
    def maxProfit_02(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        price_min = 2147483647
        profits = []
        for price in prices:
            price_min = min(price_min, price)
            profits.append(price - price_min)
        return max(profits)


def sets_gen(maxProfit):
    import random
    test_sets = []
    for i in range(10, 500):
        prices = [random.randint(0, i) for _ in range(i)]
        match = maxProfit(prices)
        test_sets.append((prices, match))
    return test_sets


def test(maxProfit, test_sets, msg):
    for prices, match in test_sets:
        try:
            assert (maxProfit(prices) == match)
        except AssertionError as ex:
            print(prices, match, maxProfit(prices))
            print(msg, '--> Assertion Error <--')


def test_spd(maxProfit, test_sets):
    for prices, _ in test_sets:
        maxProfit(prices)


if __name__ == '__main__':
    sol = Solution()
    # prep
    print('prep...')
    test_sets = sets_gen(sol.maxProfit)
    # test
    print('test...')
    test(sol.maxProfit_01, test_sets, '01')
    test(sol.maxProfit_02, test_sets, '02')
    # test_spd
    print('test_spd...')
    _stmt_ = 'test_spd(sol.maxProfit_{0:02d}, test_sets)'
    _setup_ = 'from __main__ import test_spd, test_sets, sol'
    _number_ = 100
    from timeit import timeit

    print(timeit(stmt=_stmt_.format(1), setup=_setup_, number=_number_))
    print(timeit(stmt=_stmt_.format(2), setup=_setup_, number=_number_))
