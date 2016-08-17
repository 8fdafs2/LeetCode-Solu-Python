class Solution(object):
    # [
    #            [1],               n = 1
    #           [1,1],              n = 2
    #          [1,2,1],             n = 3
    #         [1,3,3,1],            n = 4
    #        [1,4,6,4,1],           n = 5
    #      [1,5,10,10,5,1],         n = 6
    #     [1,6,15,20,15,6,1]        n = 7
    #   [1,7,21,35,35,21,7,1]       n = 8
    # ]

    def __init__(self):
        self.generate = self.generate_01

    # Your runtime beats 36.42% of pythonsubmissions.
    def generate_01(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = [
            [1, ],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
            [1, 5, 10, 10, 5, 1],
            [1, 6, 15, 20, 15, 6, 1],
        ]
        if numRows < 7:
            return ret[:numRows]
        for row in range(7, numRows):
            ret_curr = [1, row] + [ret[row - 1][j] + ret[row - 1][j + 1] for j in range(1, row >> 1)]
            if row % 2 == 0:
                ret.append(ret_curr + ret_curr[-2::-1])
            else:
                ret.append(ret_curr + ret_curr[::-1])
        return ret

    def generate_02(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = []
        for row in range(numRows):
            ret_sub = []
            for col in range(row + 1):
                if col == 0 or col == row:
                    ret_sub.append(1)
                else:
                    ret_sub.append(ret[row - 1][col - 1] + ret[row - 1][col])
            ret.append(ret_sub)
        return ret


def sets_gen(generate):
    test_sets = []
    for numRows in range(100):
        match = generate(numRows)
        test_sets.append((numRows, match))
    return test_sets


def test(generate, test_sets, msg):
    for numRows, match in test_sets:
        try:
            assert (generate(numRows) == match)
        except AssertionError as ex:
            print(numRows, match, generate(numRows))
            print(msg, '--> Assertion Error <--')


def test_spd(generate, test_sets):
    for numRows, match in test_sets:
        generate(numRows)


if __name__ == '__main__':
    sol = Solution()
    # prep
    print('prep...')
    test_sets = sets_gen(sol.generate)
    # test
    print('test...')
    test(sol.generate_01, test_sets, '01')
    test(sol.generate_02, test_sets, '02')
    # test_spd
    print('test_spd...')
    _stmt_ = 'test_spd(sol.generate_{0:02d}, test_sets)'
    _setup_ = 'from __main__ import test_spd, sol, test_sets'
    _number_ = 100
    import timeit

    print(timeit.timeit(stmt=_stmt_.format(01), setup=_setup_, number=_number_))
    print(timeit.timeit(stmt=_stmt_.format(02), setup=_setup_, number=_number_))
