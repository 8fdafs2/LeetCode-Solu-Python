class Solution(object):
    def __init__(self):
        self.romanToInt = self.romanToInt_01

    # Your runtime beats 90.24% of pythonsubmissions.
    def romanToInt_01(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        length = len(s)
        i = 0

        while i < length and s[i] == 'M':
            num += 1000
            i += 1

        if i+1 < length and s[i: i+2] == 'CM':
            num += 900
            i += 2
        if i < length and s[i] == 'D':
            num += 500
            i += 1
        if i+1 < length and s[i: i+2] == 'CD':
            num += 400
            i += 2
        while i < length and s[i] == 'C':
            num += 100
            i += 1

        if i+1 < length and s[i: i+2] == 'XC':
            num += 90
            i += 2
        if i < length and s[i] == 'L':
            num += 50
            i += 1
        if i+1 < length and s[i: i+2] == 'XL':
            num += 40
            i += 2
        while i < length and s[i] == 'X':
            num += 10
            i += 1

        if i+1 < length and s[i: i+2] == 'IX':
            num += 9
            i += 2
        if i < length and s[i] == 'V':
            num += 5
            i += 1
        if i+1 < length and s[i: i+2] == 'IV':
            num += 4
            i += 2
        while i < length and s[i] == 'I':
            num += 1
            i += 1

        return num


    def romanToInt_02(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman2int_dict = \
            {
                'I': 1,
                'IV': 4,
                'V': 5,
                'IX': 9,
                'X': 10,
                'XL': 40,
                'L': 50,
                'XC': 90,
                'C': 100,
                'CD': 400,
                'D': 500,
                'CM': 900,
                'M': 1000,
            }
        len_s = len(s)
        i = 0
        num = 0
        for roman in ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']:
            while i < len_s and s.startswith(roman, i):
                num += roman2int_dict[roman]
                i += len(roman)
        # roman_len_lst = [('M', 1), ('M', 1), ('M', 1),
        #                  ('CM', 2), ('D', 1), ('CD', 2),
        #                  ('C', 1), ('C', 1), ('C', 1),
        #                  ('XC', 2), ('L', 1), ('XL', 2),
        #                  ('X', 1), ('X', 1), ('X', 1),
        #                  ('IX', 2), ('V', 1), ('IV', 2),
        #                  ('I', 1), ('I', 1), ('I', 1), ]
        # for roman, len_roman in roman_len_lst:
        #     if i < len_s and s.startswith(roman, i):
        #         num += roman2int_dict[roman]
        #         i += len_roman

        return num

def sets_get(romanToInt=None):
    test_sets = []
    romans = [
        'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X',
        'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX',
        'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI', 'XXVII', 'XXVIII', 'XXIX', 'XXX',
        'XXXI', 'XXXII', 'XXXIII', 'XXXIV', 'XXXV', 'XXXVI', 'XXXVII', 'XXXVIII', 'XXXIX', 'XL',
        'XLI', 'XLII', 'XLIII', 'XLIV', 'XLV', 'XLVI', 'XLVII', 'XLVIII', 'XLIX', 'L',
        'LI', 'LII', 'LIII', 'LIV', 'LV', 'LVI', 'LVII', 'LVIII', 'LIX', 'LX',
        'LXI', 'LXII', 'LXIII', 'LXIV', 'LXV', 'LXVI', 'LXVII', 'LXVIII', 'LXIX', 'LXX',
        'LXXI', 'LXXII', 'LXXIII', 'LXXIV', 'LXXV', 'LXXVI', 'LXXVII', 'LXXVIII', 'LXXIX', 'LXXX',
        'LXXXI', 'LXXXII', 'LXXXIII', 'LXXXIV', 'LXXXV', 'LXXXVI', 'LXXXVII', 'LXXXVIII', 'LXXXIX', 'XC',
        'XCI', 'XCII', 'XCIII', 'XCIV', 'XCV', 'XCVI', 'XCVII', 'XCVIII', 'XCIX', 'C',
    ]
    for roman in romans:
        match = romanToInt(roman)
        test_sets.append((roman, match))
    return test_sets


def test(romanToInt=None, test_sets=None):
    for roman, match in test_sets:
        try:
            assert(romanToInt(roman) == match)
        except AssertionError as ex:
            print(roman, match, romanToInt(roman))
            print('--> Assertion Error <--')


def test_spd(romanToInt=None, test_sets=None):
    for roman, _ in test_sets:
        romanToInt(roman)


if __name__ == '__main__':
    # prep
    print('prep...')
    sol = Solution()
    test_sets = sets_get(sol.romanToInt)
    # test
    print('test...')
    test(sol.romanToInt_01, test_sets)
    test(sol.romanToInt_02, test_sets)
    # test_spd
    print('test_spd...')
    _stmt_ = 'test_spd(sol.romanToInt_{:02d}, test_sets)'
    _setup_ = 'from __main__ import sol, test_spd, test_sets'
    _number_ = 1000
    import timeit
    print(timeit.timeit(stmt=_stmt_.format(1), setup=_setup_, number=_number_))
    print(timeit.timeit(stmt=_stmt_.format(2), setup=_setup_, number=_number_))
