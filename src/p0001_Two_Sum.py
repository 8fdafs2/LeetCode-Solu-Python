'''
Created on May 8, 2016

@author: ray.wang
'''
import itertools


class Solution(object):
    def __init__(self):
        self.twoSum = self.twoSum_01

    # Approach #01 (Brute Force)
    # 20160508 : Your runtime beats 18.17% of pythonsubmissions.
    def twoSum_01(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rng = list(range(len(nums)))
        for i in rng:
            num2expect = target - nums[i]
            for j in rng[i + 1:]:
                if nums[j] == num2expect:
                    return sorted([i, j])

    # Approach #02 (Two-pass Hash Table)
    # 20160508 : Your runtime beats 74.76% of pythonsubmissions.
    def twoSum_02(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {num: i for i, num in enumerate(nums)}

        for i in range(len(nums)):
            num2expect = target - nums[i]
            if num2expect in nums_dict and nums_dict[num2expect] != i:
                return sorted([i, nums_dict[num2expect]])

            #         i = 0
            #         for num in nums:
            #             num2expect = target - num
            #             if num2expect in nums_dict and nums_dict[num2expect] != i:
            #                 return [i, nums_dict[num2expect]]
            #             i += 1

    # Approach #03 (One-pass Hash Table)
    # 20160508 : Your runtime beats 74.76% of pythonsubmissions.
    def twoSum_03(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}

        for i in range(len(nums)):
            num2expect = target - nums[i]
            if num2expect in nums_dict:
                return sorted([nums_dict[num2expect], i])
            nums_dict[nums[i]] = i

        #         i = 0
        #         for num in nums:
        #             num2expect = target - num
        #             if num2expect in nums_dict:
        #                 return [nums_dict[num2expect], i]
        #             nums_dict[num] = i
        #             i += 1

    # Approach #04 (Binary Search)
    # 20160508 : Your runtime beats 43.14% of pythonsubmissions.
    def twoSum_04(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums, indexs = list(zip(*sorted([(num, i) for i, num in enumerate(nums)])))

        #         indexs, nums = list(zip(*sorted(enumerate(nums), key=lambda x: x[1])))

        #         from operator import itemgetter
        #         indexs, nums = list(zip(*sorted(enumerate(nums), key=itemgetter(1))))

        imax = len(nums)

        for i in range(imax):
            num2expect = target - nums[i]

            lo = i + 1
            hi = imax

            while lo < hi:
                mid = (lo + hi) // 2
                midval = nums[mid]
                if midval < num2expect:
                    lo = mid + 1
                elif midval > num2expect:
                    hi = mid
                else:
                    return sorted([indexs[i], indexs[mid]])

    # Approach #05 (Combination Search)
    # 20160508 : Your runtime beats ?% of pythonsubmissions.
    def twoSum_05(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for ele_01, ele_02 in itertools.combinations(nums, 2):
            if ele_01 + ele_02 == target:
                return [nums.index(ele_01), nums.index(ele_02)]


def test(twoSum=None, test_sets=None):
    for nums, target, match in test_sets:
        assert (twoSum(nums, target) == match)


def test_spd(twoSum=None, test_sets=None):
    for nums, target, _ in test_sets:
        twoSum(nums, target)


def sets_get(twoSum=None):
    import random, itertools
    test_sets = []
    rng = range(10000)
    i = 3
    while i < 101:
        nums = sorted(random.sample(rng, i))
        ele_01, ele_02 = sorted(random.sample(nums, 2))
        target = ele_01 + ele_02
        match = [nums.index(ele_01), nums.index(ele_02)]

        # if len([True for ele_01, ele_02 in itertools.combinations(nums, 2) if ele_01 + ele_02 == target]) > 1:
        #     continue

        is_cont = False
        for _ele_01_, _ele_02_ in itertools.combinations(nums, 2):
            if _ele_01_ + _ele_02_ == target and _ele_01_ != ele_01:
                is_cont = True
                break
        if is_cont:
            continue

        test_sets.append((nums, target, match))
        i += 1

    return test_sets


if __name__ == '__main__':
    # prep
    print('prep...')
    sol = Solution()
    test_sets = sets_get(sol.twoSum)

    # test
    print('test...')
    test(sol.twoSum_01, test_sets)
    test(sol.twoSum_02, test_sets)
    test(sol.twoSum_03, test_sets)
    test(sol.twoSum_04, test_sets)
    test(sol.twoSum_05, test_sets)

    # test_spd
    print('test_spd...')
    _stmt_ = "test_spd(sol.twoSum_{:02d}, test_sets)"
    _setup_ = "from __main__ import sol, test_spd, test_sets"
    _number_ = 1000

    import timeit

    print(timeit.timeit(stmt=_stmt_.format(1), setup=_setup_, number=_number_))
    print(timeit.timeit(stmt=_stmt_.format(2), setup=_setup_, number=_number_))
    print(timeit.timeit(stmt=_stmt_.format(3), setup=_setup_, number=_number_))
    print(timeit.timeit(stmt=_stmt_.format(4), setup=_setup_, number=_number_))
    print(timeit.timeit(stmt=_stmt_.format(5), setup=_setup_, number=_number_))
