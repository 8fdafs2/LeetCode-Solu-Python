class Solution(object):
    def __init__(self):
        self.longestCommonPrefix = self.longestCommonPrefix_01

    # Vertical Scanning
    # Your runtime beats 53.43% of pythonsubmissions.
    def longestCommonPrefix_01(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        num_str = len(strs)
        len_min = min([len(prefix) for prefix in strs])
        if len_min == num_str == 1:
            return strs[0]
        prefix = strs[0][:len_min]

        for i in range(len_min):
            chr = prefix[i]
            for str in strs[1:]:
                if str[i] != chr:
                    return str[:i]

        return prefix

    # Horizontal Scanning
    # Your runtime beats 36.93% of pythonsubmissions.
    def longestCommonPrefix_02(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        num_str = len(strs)
        len_min = min([len(str) for str in strs])
        if len_min == num_str == 1:
            return strs[0]
        prefix = strs[0][:len_min]

        for str in strs[1:]:
            while not str.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ''

        return prefix

    # Divide 'n' Conquer
    # Your runtime beats 22.22% of pythonsubmissions.
    def longestCommonPrefix_03(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        num_str = len(strs)
        len_min = min([len(str) for str in strs])
        if len_min == num_str == 1:
            return strs[0]

        def cp(str_l, str_r):
            len_min = min(len(str_l), len(str_r))
            for i in range(len_min):
                if str_l[i] != str_r[i]:
                    return str_l[:i]
            return str_l[:len_min]

        def lcp(strs, l, r):
            if l == r:
                return strs[l]
            else:
                mid = (l + r) // 2
                str_l = lcp(strs, l, mid)
                str_r = lcp(strs, mid + 1, r)
                return cp(str_l, str_r)

        return lcp(strs, 0, len(strs) - 1)

    # Binary Search
    # Your runtime beats 36.93% of pythonsubmissions.
    def longestCommonPrefix_04(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        num_str = len(strs)
        high = min([len(str) for str in strs])
        if high == num_str == 1:
            return strs[0]

        def iscp(strs, length):
            prefix = strs[0][:length]
            for str in strs[1:]:
                if not str.startswith(prefix):
                    return False
            return True

        low = 1

        while (low <= high):
            mid = (low + high) // 2
            if iscp(strs, mid):
                low = mid + 1
            else:
                high = mid - 1

        return strs[0][:(low + high) // 2]


def sets_gen(longestCommonPrefix=None):
    import string
    import random

    test_sets = []

    for i in range(20):  # length of prefix
        strs = []
        prefix = ''.join(random.choice(string.letters + string.digits) for _ in range(i))
        for j in range(40 - i):  # length of rest
            for _ in range(20):  # number of strs
                str = prefix + ''.join(random.choice(string.letters + string.digits) for _ in range(j))
                strs.append(str)
            match = longestCommonPrefix(strs)
            test_sets.append((strs, match))

    return test_sets


def test(longestCommonPrefix=None, test_sets=None, msg=None):
    for strs, match in test_sets:
        try:
            assert (longestCommonPrefix(strs) == match)
        except AssertionError as ex:
            print(strs, match, longestCommonPrefix(strs))
            print(msg, '--> Assertion Error <--')


def test_spd(longestCommonPrefix=None, test_sets=None):
    for strs, _ in test_sets:
        longestCommonPrefix(strs)


if __name__ == '__main__':
    sol = Solution()
    # prep
    print('prep...')
    test_sets = sets_gen(sol.longestCommonPrefix)
    # test
    print('test...')
    test(sol.longestCommonPrefix_01, test_sets, '01')
    test(sol.longestCommonPrefix_02, test_sets, '02')
    test(sol.longestCommonPrefix_03, test_sets, '03')
    test(sol.longestCommonPrefix_04, test_sets, '04')
    # test_spd
    print('test_spd...')
    _stmt_ = 'test_spd(sol.longestCommonPrefix_{0:02d}, test_sets)'
    _setup_ = 'from __main__ import test_spd, sol, test_sets'
    _number_ = 50
    import timeit

    print(timeit.timeit(stmt=_stmt_.format(01), setup=_setup_, number=_number_))
    print(timeit.timeit(stmt=_stmt_.format(02), setup=_setup_, number=_number_))
    print(timeit.timeit(stmt=_stmt_.format(03), setup=_setup_, number=_number_))
    print(timeit.timeit(stmt=_stmt_.format(04), setup=_setup_, number=_number_))
