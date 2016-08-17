class Solution(object):
    def __init__(self):
        self.canJump = self.canJump_01

    # Memory Limit Exceeded
    def canJump_01(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)

        i_lst = set([0, ])

        while i_lst:
            if max(i_lst) >= length - 1:
                return True

            i_new_lst = []
            for i in i_lst:
                i_new_lst += [i + step for step in range(1, nums[i] + 1)]

            i_lst = set([i_new for i_new in set(i_new_lst) if i_new not in i_lst])

        return False

    def canJump_02(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i_furthest = 0
        for i, jump_len in enumerate(nums):
            if i > i_furthest:
                return False
            i_furthest = max(i_furthest, i + jump_len)
        return i_furthest >= len(nums) - 1


def test(canJump=None, test_sets=None):
    for arr, match in test_sets:
        try:
            assert (canJump(arr) == match)
        except AssertionError as ex:
            print(arr, match, canJump(arr))
            print(ex)


def test_spd(canJump=None, test_sets=None):
    for arr, match in test_sets:
        canJump(arr)


def sets_get(canJump=None):
    import random
    test_sets = []

    for i in range(10, 100):
        arr = [random.randint(0, int(i ** 0.75)) for _ in range(i)]
        match = canJump(arr)

        test_sets.append((arr, match))

    return test_sets


if __name__ == '__main__':
    # prep
    print('prep...')
    sol = Solution()
    test_sets = sets_get(sol.canJump)

    # test
    print('test...')
    test(sol.canJump_01, test_sets)
    test(sol.canJump_02, test_sets)

    # test_spd
    print('test_spd...')
    _stmt_ = 'test_spd(sol.canJump_{:02d}, test_sets)'
    _setup_ = 'from __main__ import sol, test_spd, test_sets'
    _number_ = 1000

    import timeit

    print(timeit.timeit(stmt=_stmt_.format(1), setup=_setup_, number=_number_))
    print(timeit.timeit(stmt=_stmt_.format(2), setup=_setup_, number=_number_))
