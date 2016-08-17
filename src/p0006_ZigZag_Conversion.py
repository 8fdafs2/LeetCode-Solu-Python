# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string text, int nRows);
#
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
#
# P Y A I H R N # 0::+2+0
# A P L S I I G # 0::+0+2
#
# P   A   H   N # 0::+4+0
# A P L S I I G # 0::+2+2
# Y   I   R     # 0::+0+4
#
# P     I     N # 0::+6+0
# A   L S   I G # 1::+4+2
# Y A   H R     # 2::+2+4
# P     I       # 4::+0+6
#
# P      H      # 0::+8+0
# A    S I      # 1::+6+2
# Y  I   R      # 2::+4+4
# P L    I G    # 3::+2+6
# A      N      # 4::+0+8


class Solution(object):
    def __init__(self):
        self.convert = self.convert_01

    # Your runtime beats 80.68% of pythonsubmissions.
    def convert_01(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        ret = ''
        len_s = len(s)
        step_01, step_02 = (numRows - 1) << 1, 0
        for row in range(numRows):
            if row >= len_s:
                break
            i = row
            while i < len_s:
                if step_01:
                    ret += s[i]
                    i += step_01
                    if i >= len_s:
                        break
                if step_02:
                    ret += s[i]
                    i += step_02
            step_01 -= 2
            step_02 += 2
        return ret

    # Your runtime beats 41.14% of pythonsubmissions.
    def convert_02(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        len_s = len(s)
        numRows_minus_1 = numRows - 1
        step = numRows_minus_1 << 1
        step_01 = step - 2
        step_02 = 2
        ret = ''
        for row in range(1, numRows_minus_1):
            if row >= len_s:
                break
            i = row
            while i < len_s:
                ret += s[i]
                i += step_01
                if i >= len_s:
                    break
                ret += s[i]
                i += step_02
            step_01 -= 2
            step_02 += 2
        if numRows_minus_1 < len_s:
            return s[::step] + ret + s[numRows_minus_1::step]
        return s[::step] + ret

    def convert_03(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        len_s = len(s)
        numRows_minus_1 = numRows - 1
        step = numRows_minus_1 << 1
        ret = ''
        for i in range(1, numRows_minus_1):
            for j in range(i, len_s, step):
                ret += s[j]
                k = j + step - (i << 1)
                if k < len_s:
                    ret += s[k]
        if numRows_minus_1 < len_s:
            return s[::step] + ret + s[numRows_minus_1::step]
        return s[::step] + ret


def sets_gen(convert):
    import random
    import string
    test_sets = []
    for i in range(10, 100):
        s = ''.join([random.choice(string.ascii_uppercase) for _ in range(i)])
        numRows = random.randint(1, i)
        match = convert(s, numRows)
        test_sets.append((s, numRows, match))
    return test_sets


def test(convert, test_sets, msg):
    for s, numRows, match in test_sets:
        try:
            assert (convert(s, numRows) == match)
        except AssertionError as ex:
            print(s, numRows, match, convert(s, numRows))
            print(msg, '--> Assertion Error <--')


def test_spd(convert, test_sets):
    for s, numRows, _ in test_sets:
        convert(s, numRows)


if __name__ == '__main__':
    sol = Solution()
    # prep
    print('prep...')
    test_sets = sets_gen(sol.convert)
    # test
    print('test...')
    test(sol.convert_01, test_sets, '01')
    test(sol.convert_02, test_sets, '02')
    test(sol.convert_03, test_sets, '03')
    # test_spd
    print('test_spd...')
    _stmt_ = 'test_spd(sol.convert_{0:02d}, test_sets)'
    _setup_ = 'from __main__ import sol, test_sets, test_spd'
    _number_ = 1000
    import timeit

    print(timeit.timeit(stmt=_stmt_.format(01), setup=_setup_, number=_number_))
    print(timeit.timeit(stmt=_stmt_.format(02), setup=_setup_, number=_number_))
    print(timeit.timeit(stmt=_stmt_.format(03), setup=_setup_, number=_number_))
