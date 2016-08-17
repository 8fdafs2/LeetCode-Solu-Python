class Solution(object):
    def __init__(self):
        self.intToRoman = self.intToRoman_01

    # Your runtime beats 69.84% of pythonsubmissions.
    def intToRoman_01(self, num):
        """
        :type num: int
        :rtype: str
        """
        nM = nCM = nD = nCD = nC = nXC = nL = nXL = nX = nIX = nV = nIV = nI = 0

        if num >= 1000:
            nM = num // 1000
            num -= nM * 1000

        if num >= 900:
            nCM = 1
            num -= 900
        elif num >= 500:
            nD = 1
            num -= 500
        elif num >= 400:
            nCD = 1
            num -= 400
        if num >= 100:
            nC = num // 100
            num -= nC * 100

        if num >= 90:
            nXC = 1
            num -= 90
        elif num >= 50:
            nL = 1
            num -= 50
        elif num >= 40:
            nXL = 1
            num -= 40
        if num >= 10:
            nX = num // 10
            num -= nX * 10

        if num >= 9:
            nIX = 1
            num -= 9
        elif num >= 5:
            nV = 1
            num -= 5
        elif num >= 4:
            nIV = 1
            num -= 4
        if num >= 0:
            nI = num

        return nM * 'M' + \
               nCM * 'CM' + nD * 'D' + nCD * 'CD' + nC * 'C' + \
               nXC * 'XC' + nL * 'L' + nXL * 'XL' + nX * 'X' + \
               nIX * 'IX' + nV * 'V' + nIV * 'IV' + nI * 'I'

        # return ''.join([nM * 'M',
        #                 nCM * 'CM', nD * 'D', nCD * 'CD', nC * 'C',
        #                 nXC * 'XC', nL * 'L', nXL * 'XL', nX * 'X',
        #                 nIX * 'IX', nV * 'V', nIV * 'IV', nI * 'I'])

    def intToRoman_02(self, num):
        """
        :type num: int
        :rtype: str
        """
        int2roman_dict = \
            {
                1: 'I',
                4: 'IV',
                5: 'V',
                9: 'IX',
                10: 'X',
                40: 'XL',
                50: 'L',
                90: 'XC',
                100: 'C',
                400: 'CD',
                500: 'D',
                900: 'CM',
                1000: 'M',
            }

        ret = []
        # for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
        #     while num >= n:
        #         ret.append(int2roman_dict[n])
        #         num -= n
        for n in [1000, 1000, 1000, 900, 500, 400, 100, 100, 100, 90, 50, 40, 10, 10, 10, 9, 5, 4, 1, 1, 1]:
            if num >= n:
                ret.append(int2roman_dict[n])
                num -= n

        return ''.join(ret)


def test(intToRoman=None, test_sets=None):
    for num, match in test_sets:
        try:
            assert (intToRoman(num) == match)
        except AssertionError as ex:
            print(num, match, intToRoman(num))
            print('--> Assertion Error <--')


def test_spd(intToRoman=None, test_sets=None):
    for num, _ in test_sets:
        intToRoman(num)


def sets_get(intToRoman=None):
    test_sets = []
    for num in range(1, 4000):
        match = intToRoman(num)
        test_sets.append((num, match))
    return test_sets


if __name__ == '__main__':
    # prep
    print('prep...')
    sol = Solution()
    test_sets = sets_get(sol.intToRoman)
    # test
    print('test...')
    test(sol.intToRoman_01, test_sets)
    test(sol.intToRoman_02, test_sets)
    # test_spd
    print('test_spd...')
    _stmt_ = 'test_spd(sol.intToRoman_{:02d}, test_sets)'
    _setup_ = 'from __main__ import sol, test_spd, test_sets'
    _number_ = 1000
    import timeit
    print(timeit.timeit(stmt=_stmt_.format(1), setup=_setup_, number=_number_))
    print(timeit.timeit(stmt=_stmt_.format(2), setup=_setup_, number=_number_))
