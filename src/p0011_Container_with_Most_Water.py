class Solution(object):

    def __init__(self):
        self.maxArea = self.maxArea_01

    # Your runtime beats 58.61% of pythonsubmissions.
    def maxArea_01(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        ret = 0
        while l < r:
            height_l = height[l]
            height_r = height[r]
            ret = max(ret, (r - l) * min(height_l, height_r))
            if height_l <= height_r:
                l += 1
            else:
                r -= 1
        return ret

    # Your runtime beats 58.61% of pythonsubmissions.
    def maxArea_02(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        ret = []
        while l < r:
            height_l = height[l]
            height_r = height[r]
            ret.append((r - l) * min(height_l, height_r))
            if height_l <= height_r:
                l += 1
            else:
                r -= 1
        return max(ret)


def sets_gen(maxArea):
    import random
    test_sets = []
    for i in range(10, 100):
        height = [random.randint(0, i) for _ in range(i)]
        match = maxArea(height)
        test_sets.append((height, match))
    return test_sets

def test(maxArea, test_sets, msg):
    for height, match in test_sets:
        try:
            assert (maxArea(height) == match)
        except AssertionError as ex:
            print(height, match, maxArea(height))
            print(msg, '--> Assertion Error <--')

def test_spd(maxArea, test_sets):
    for height, _ in test_sets:
        maxArea(height)

if __name__ == '__main__':
    sol = Solution()
    # prep
    print('prep...')
    test_sets = sets_gen(sol.maxArea)
    # test
    print('test...')
    test(sol.maxArea_01, test_sets, '01')
    test(sol.maxArea_02, test_sets, '02')
    # test_spd
    print('test_spd...')
    _stmt_ = 'test_spd(sol.maxArea_{0:02d}, test_sets)'
    _setup_ = 'from __main__ import sol, test_sets, test_spd'
    _number_ = 100
    import timeit
    print(timeit.timeit(stmt=_stmt_.format(01), setup=_setup_, number=_number_))
    print(timeit.timeit(stmt=_stmt_.format(02), setup=_setup_, number=_number_))