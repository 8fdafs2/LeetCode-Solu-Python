class Solution(object):
    def __init__(self):
        self.maxSubArray = self.maxSubArray_01

    # Your runtime beats 44.60% of pythonsubmissions.
    def maxSubArray_01(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums_max = max(nums)
        if nums_max < 0:
            return nums_max

        sum_max_g = 0
        sum_max = 0
        for num in nums:
            if sum_max + num >= 0:
                sum_max += num
            else:
                sum_max = 0
            sum_max_g = max(sum_max_g, sum_max)

        return sum_max_g

    # Your runtime beats 44.60% of pythonsubmissions.
    def maxSubArray_02(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums_max = max(nums)
        if nums_max < 0:
            return nums_max

        sum_maxs = []
        sum_max = 0
        for num in nums:
            if sum_max + num >= 0:
                sum_max += num
            else:
                sum_max = 0
            sum_maxs.append(sum_max)

        return max(sum_maxs)


def sets_gen(maxSubArray):
    import random
    test_sets = []
    for i in range(10, 500):
        nums = [random.randint(-i, i) for _ in range(i)]
        match = maxSubArray(nums)
        test_sets.append((nums, match))
    return test_sets


def test(maxSubArray, test_sets, msg):
    for nums, match in test_sets:
        try:
            assert (maxSubArray(nums) == match)
        except AssertionError as ex:
            print(nums, match, maxSubArray(nums))
            print(msg, '--> Assertion Error <--')


def test_spd(maxSubArray, test_sets):
    for nums, _ in test_sets:
        maxSubArray(nums)


if __name__ == '__main__':
    sol = Solution()
    # prep
    print('prep...')
    test_sets = sets_gen(sol.maxSubArray)
    # test
    print('test...')
    test(sol.maxSubArray_01, test_sets, '01')
    test(sol.maxSubArray_02, test_sets, '02')
    # test_spd
    print('test_spd...')
    _stmt_ = 'test_spd(sol.maxSubArray_{0:02d}, test_sets)'
    _setup_ = 'from __main__ import test_spd, test_sets, sol'
    _number_ = 100
    from timeit import timeit

    print(timeit(stmt=_stmt_.format(1), setup=_setup_, number=_number_))
    print(timeit(stmt=_stmt_.format(2), setup=_setup_, number=_number_))
