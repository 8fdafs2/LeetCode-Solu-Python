# coding=utf-8
class Solution(object):

    def __init__(self):
        self.grayCode = self.grayCode_01

    # Each bit is inverted if the next higher bit of the input value is set to one.
    # Performed in parallel by a bit-shift and exclusive-or operation
    # Your runtime beats 49.04% of pythonsubmissions.
    def grayCode_01(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # The operator >> is shift right.
        # The operator ^ is exclusive or.
        # return [num ^ (num >> 1) for num in range(2 ** n)]
        return [num ^ (num >> 1) for num in range(1 << n)]

    # Each bit is inverted if the next higher bit of the input value is set to one.
    # Alternative way to simulate bit-shift and exclusive-or operation
    # by assuming they are unavailable
    # Your runtime beats 7.05% of pythonsubmissions.
    def grayCode_02(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]

        _code_ = []

        _seq_ = range(n - 1, 0, -1)

        _bin_fmt_ = '{{0:0{}b}}'.format(n)

        for _bin_ in [list(_bin_fmt_.format(num)) for num in range(2 ** n)]:
            for _bit_ in _seq_:
                if _bin_[_bit_ - 1] == '1':
                    if _bin_[_bit_] == '1':
                        _bin_[_bit_] = '0'
                    else:
                        _bin_[_bit_] = '1'
            _code_.append(int(''.join(_bin_), 2))

        return _code_

    # The binary-reflected Gray code list for n bits
    # can be generated recursively from the list for n − 1 bits
    # by reflecting the list (i.e. listing the entries in reverse order),
    # concatenating the original list with the reversed list,
    # prefixing the entries in the original list with a binary 0,
    # and then prefixing the entries in the reflected list with a binary 1.
    # ---------------------------------------------------
    # Recursive Function
    # RuntimeError: maximum recursion depth exceeded
    def grayCode_03(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]

        _code_ = self.grayCode_01(n - 1)
        _msb_ = 1 << (n - 1)
        return _code_ + [_msb_ + c for c in reversed(_code_)]

    # Recursive Function replaced by For-Loop
    def grayCode_04(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]

        _code_ = [0, 1]

        for _n_ in range(2, n + 1):
            _msb_ = 1 << _n_ - 1
            _code_ += [_msb_ + c for c in reversed(_code_)]

        return _code_


def set_gen(grayCode):
    test_set = []
    for n in range(18):
        match = grayCode(n)
        test_set.append((n, match))
    return test_set


def test(grayCode, test_set):
    for n, match in test_set:
        try:
            assert(grayCode(n) == match)
        except AssertionError as ex:
            print(n, match, grayCode(n))


def test_spd(grayCode, test_set):
    for n, match in test_set:
        grayCode(n)


if __name__ == '__main__':
    sol = Solution()
    # prep
    print('prep...')
    test_set = set_gen(sol.grayCode)
    # test
    print('test...')
    test(sol.grayCode_01, test_set)
    test(sol.grayCode_02, test_set)
    test(sol.grayCode_03, test_set)
    test(sol.grayCode_04, test_set)
    # test_spd
    print('test_spd...')
    _stmt_ = 'test_spd(sol.grayCode_{0:02d}, test_set)'
    _setup_ = 'from __main__ import test_spd, test_set, sol'
    _number_ = 100
    from timeit import timeit
    print(timeit(stmt=_stmt_.format(1), setup=_setup_, number=_number_))
    # print(timeit(stmt=_stmt_.format(2), setup=_setup_, number=_number_))
    print(timeit(stmt=_stmt_.format(3), setup=_setup_, number=_number_))
    print(timeit(stmt=_stmt_.format(4), setup=_setup_, number=_number_))