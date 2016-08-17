class Solution(object):

    def __init__(self):
        self.generateParenthesis = self.generateParenthesis_01

    # Your runtime beats 66.46% of pythonsubmissions.
    def generateParenthesis_01(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return['']

        result = []

        def recur(_cur_, _nleft_, _nright_):

            if _nleft_ == 0 and _nright_ == 1:
                result.append(_cur_ + ')')
                return

            if _nleft_ > 0:
                recur(_cur_ + '(', _nleft_ - 1, _nright_)

            if _nleft_ < _nright_:
                recur(_cur_ + ')', _nleft_, _nright_ - 1)

        recur('(', n - 1, n)

        return result

    # Your runtime beats 66.46% of pythonsubmissions.
    def generateParenthesis_02(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        def recur(_cur_, _nleft_, _nright_):

            if _nleft_ == 0 and _nright_ == 0:
                result.append(_cur_)
                return

            if _nleft_ > 0:
                recur(_cur_ + '(', _nleft_ - 1, _nright_)

            if _nleft_ < _nright_:
                recur(_cur_ + ')', _nleft_, _nright_ - 1)

        recur('', n, n)

        return result


def set_gen(generateParenthesis):
    test_set = []
    for n in range(12):
        match = generateParenthesis(n)
        test_set.append((n, match))
    return test_set


def test(generateParenthesis, test_set):
    for n, match in test_set:
        try:
            assert(generateParenthesis(n) == match)
        except AssertionError as ex:
            print(n, match, generateParenthesis(n))


def test_spd(generateParenthesis, test_set):
    for n, match in test_set:
        generateParenthesis(n)


if __name__ == '__main__':
    sol = Solution()
    # prep
    print('prep...')
    test_set = set_gen(sol.generateParenthesis)
    # test
    print('test...')
    test(sol.generateParenthesis_01, test_set)
    test(sol.generateParenthesis_02, test_set)
    # test_spd
    print('test_spd...')
    _stmt_ = 'test_spd(sol.generateParenthesis_{0:02d}, test_set)'
    _setup_ = 'from __main__ import test_spd, test_set, sol'
    _number_ = 50
    from timeit import timeit
    print(timeit(stmt=_stmt_.format(1), setup=_setup_, number=_number_))
    print(timeit(stmt=_stmt_.format(2), setup=_setup_, number=_number_))