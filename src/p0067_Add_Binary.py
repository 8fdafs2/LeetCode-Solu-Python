class Solution(object):
    def __init__(self):
        self.addBinary = self.addBinary_01

    # Your runtime beats 72.27% of pythonsubmissions.
    def addBinary_01(self, a, b):
        '''
        :type a: str
        :type b: str
        :rtype: str
        '''
        # return '{0:b}'.format(int(a, 2) + int(b, 2))
        return bin(int(a, 2) + int(b, 2))[2:]

    # Your runtime beats 72.27% of pythonsubmissions.
    def addBinary_02(self, a, b):
        '''
        :type a: str
        :type b: str
        :rtype: str
        '''
        map_ch2nu = {
            '0': 0, '1': 1, '2': 2, '3': 3,
            '4': 4, '5': 5, '6': 6, '7': 7,
            '8': 8, '9': 9,
        }
        a = [map_ch2nu[bit] for bit in a]
        b = [map_ch2nu[bit] for bit in b]
        a.reverse()
        b.reverse()
        len_a = len(a)
        len_b = len(b)
        if len_a < len_b:
            a, b = b, a
            len_a, len_b = len_b, len_a
        carry = 0
        for bit in range(len_b):
            _bit_ = a[bit] + b[bit] + carry
            if _bit_ == 3:
                a[bit] = '1'
                carry = 1
            elif _bit_ == 2:
                a[bit] = '0'
                carry = 1
            elif _bit_ == 1:
                a[bit] = '1'
                carry = 0
            else:
                a[bit] = '0'
                carry = 0
        for bit in range(bit + 1, len_a):
            _bit_ = a[bit] + carry
            if _bit_ == 2:
                a[bit] = '0'
                carry = 1
            elif _bit_ == 1:
                a[bit] = '1'
                carry = 0
            else:
                a[bit] = '0'
                carry = 0
        a.reverse()
        if carry:
            return '1' + ''.join(a)
        return ''.join(a)

    # Your runtime beats 60.04% of pythonsubmissions.
    def addBinary_03(self, a, b):
        '''
        :type a: str
        :type b: str
        :rtype: str
        '''
        map_ch2nu = {
            '0': 0, '1': 1, '2': 2, '3': 3,
            '4': 4, '5': 5, '6': 6, '7': 7,
            '8': 8, '9': 9,
        }
        map_flag = {
            3: ('1', 1),
            2: ('0', 1),
            1: ('1', 0),
            0: ('0', 0),
        }
        a = [map_ch2nu[bit] for bit in a]
        b = [map_ch2nu[bit] for bit in b]
        a.reverse()
        b.reverse()
        len_a = len(a)
        len_b = len(b)
        if len_a < len_b:
            a, b = b, a
            len_a, len_b = len_b, len_a
        carry = 0
        for bit in range(len_b):
            a[bit], carry = map_flag[a[bit] + b[bit] + carry]
        for bit in range(bit + 1, len_a):
            a[bit], carry = map_flag[a[bit] + carry]
        a.reverse()
        if carry:
            return '1' + ''.join(a)
        return ''.join(a)

    # Your runtime beats 1.53% of pythonsubmissions.
    def addBinary_04(self, a, b):
        '''
        :type a: str
        :type b: str
        :rtype: str
        '''
        map_ch2nu = {
            '0': 0, '1': 1, '2': 2, '3': 3,
            '4': 4, '5': 5, '6': 6, '7': 7,
            '8': 8, '9': 9,
        }
        a = [map_ch2nu[bit] for bit in a]
        b = [map_ch2nu[bit] for bit in b]
        a.reverse()
        b.reverse()
        len_a = len(a)
        len_b = len(b)
        if len_a < len_b:
            a, b = b, a
            len_a, len_b = len_b, len_a
        carry = 0
        for bit in range(len_b):
            _bit_ = a[bit] + b[bit] + carry
            a[bit], carry = _bit_ & 0b0001, _bit_ >> 1
        for bit in range(bit + 1, len_a):
            _bit_ = a[bit] + carry
            a[bit], carry = _bit_ & 0b0001, _bit_ >> 1
        a.reverse()
        if carry:
            return '1' + ''.join(map(str, a))
        return ''.join(map(str, a))

    def addBinary_05(self, a, b):
        '''
        :type a: str
        :type b: str
        :rtype: str
        '''
        len_a = len(a)
        len_b = len(b)
        if len_a < len_b:
            a, b = b, a
            len_a, len_b = len_b, len_a
        a, b = list(a), list(b)
        a.reverse()
        b.reverse()
        for i in range(len_b):
            if b[i] == '0':  # a[i] -> x; b[i] -> 0
                continue
            if a[i] == '0':  # a[i] -> 0; b[i] -> 1
                a[i] = '1'
                continue
            a[i] = '0'  # a[i] -> 1; b[i] -> 1
            # carry forward
            if i == len_a - 1:
                a.append('1')
                break
            for j in range(i + 1, len_a):
                if a[j] == '0':
                    a[j] = '1'
                    break
                a[j] = '0'  # carry forward
                if j == len_a - 1:
                    a.append('1')
                    break
        a.reverse()
        return ''.join(a)  # reversed back


    def addBinary_06(self, a, b):
        '''
        :type a: str
        :type b: str
        :rtype: str
        '''
        map_ch2nu = {
            '0': 0, '1': 1, '2': 2, '3': 3,
            '4': 4, '5': 5, '6': 6, '7': 7,
            '8': 8, '9': 9,
        }
        map_flag_bit = {
            3: 1,  2: 0,
            1: 1,  0: 0,
        }
        map_flag_car = {
            3: 1,  2: 1,
            1: 0,  0: 0,
        }
        a = [map_ch2nu[bit] for bit in a]
        b = [map_ch2nu[bit] for bit in b]
        a.reverse()
        b.reverse()
        len_a = len(a)
        len_b = len(b)
        if len_a < len_b:
            a, b = b, a
            len_a, len_b = len_b, len_a
        for bit in range(len_b):
            a[bit] += b[bit]
        for bit in range(len_a - 1):
            _a_bit_ = a[bit]
            a[bit] = map_flag_bit[_a_bit_]
            a[bit + 1] += map_flag_car[_a_bit_]
        if a[-1] == 3:
            a[-1] = 1
            a.append(1)
        elif a[-1] == 2:
            a[-1] = 0
            a.append(1)
        a.reverse()
        return ''.join(map(str, a))


def sets_gen(addBinary):
    import random
    test_sets = []
    for i in range(1000):
        a = bin(random.randint(0, 1000))[2:]
        b = bin(random.randint(0, 1000))[2:]
        match = addBinary(a, b)
        test_sets.append((a, b, match))
    return test_sets


def test(addBinary, test_sets, msg):
    for a, b, match in test_sets:
        try:
            assert (addBinary(a, b) == match)
        except AssertionError as ex:
            print(a, b, match, addBinary(a, b))
            print(msg, '--> Assertion Error <--')


def test_spd(addBinary, test_sets):
    for a, b, _ in test_sets:
        addBinary(a, b)


if __name__ == '__main__':
    sol = Solution()
    # prep
    print('prep...')
    test_sets = sets_gen(sol.addBinary)
    # test
    print('test...')
    test(sol.addBinary_01, test_sets, '01')
    test(sol.addBinary_02, test_sets, '02')
    test(sol.addBinary_03, test_sets, '03')
    test(sol.addBinary_04, test_sets, '04')
    test(sol.addBinary_05, test_sets, '05')
    test(sol.addBinary_06, test_sets, '06')
    # test_spd
    print('test_spd...')
    import timeit

    _stmt_ = 'test_spd(sol.addBinary_{0:02d}, test_sets)'
    _setup_ = 'from __main__ import sol, test_sets, test_spd'
    _number_ = 100

    print(timeit.timeit(stmt=_stmt_.format(01), setup=_setup_, number=_number_))
    print(timeit.timeit(stmt=_stmt_.format(02), setup=_setup_, number=_number_))
    print(timeit.timeit(stmt=_stmt_.format(03), setup=_setup_, number=_number_))
    print(timeit.timeit(stmt=_stmt_.format(04), setup=_setup_, number=_number_))
    print(timeit.timeit(stmt=_stmt_.format(05), setup=_setup_, number=_number_))
    print(timeit.timeit(stmt=_stmt_.format(06), setup=_setup_, number=_number_))
