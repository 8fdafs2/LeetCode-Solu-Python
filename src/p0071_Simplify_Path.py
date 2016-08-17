class Solution(object):
    def __init__(self):
        self.simplifyPath = self.simplifyPath_01

    def simplifyPath_01(self, path):
        """
        :type path: str
        :rtype: str
        """
        import re

        pat_01 = re.compile(r'/\.(/|$)', re.I)
        pat_02 = re.compile(r'/{2,}', re.I)
        pat_03 = re.compile(r'/[^/]*[a-zA-Z0-9\-]+[^/]*/\.{2}(/|$)', re.I)
        pat_04 = re.compile(r'^/\.{2}(/|$)', re.I)

        while pat_01.search(path):
            path = pat_01.sub(r'/', path)

        path = pat_02.sub(r'/', path)

        while pat_03.search(path):
            path = pat_03.sub(r'/', path)

        while pat_04.search(path):
            path = pat_04.sub(r'/', path)

        if len(path) > 1 and path.endswith('/'):
            return path[:-1]

        return path

    def simplifyPath_02(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = [ele for ele in path.split('/') if ele not in ('', ' ', '.')]
        for idx in range(len(path)):
            if path[idx] == '..':
                path[idx] = None
                i = idx - 1
                while i >= 0 and path[i] is None:
                    i -= 1
                if i >= 0:
                    path[i] = None
        path = [ele for ele in path if ele]
        if not path:
            return '/'
        return '/' + '/'.join(path)


def set_gen(simplifyPath):
    paths = ["/..", "/..hidden", "/...", "/.", "/./", "/home/", "/a/./b/../../c/",
             "/../", "/home//foo/", "/Hhp/..///f/R///FM/DPPv///..//",
             "/home/foo/.ssh/../.ssh2/authorized_keys/",
             "/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///",
             "/b/DfZ/AT/ya///./../../",
             "///eHx/..",
             ]
    test_set = []
    for path in paths:
        match = simplifyPath(path)
        test_set.append((path, match))
    return test_set


def test(simplifyPath, test_set):
    for path, match in test_set:
        try:
            assert (simplifyPath(path) == match)
        except AssertionError as ex:
            print(simplifyPath(path), match)
            print('--> Assertion Error <--')


def test_spd(simplifyPath, test_set):
    for path, _ in test_set:
        simplifyPath(path)


if __name__ == '__main__':
    sol = Solution()
    # prep
    print('prep...')
    test_set = set_gen(sol.simplifyPath)
    # test
    print('test...')
    test(sol.simplifyPath_01, test_set)
    test(sol.simplifyPath_02, test_set)
    # test_spd
    print('test_spd...')
    _stmt_ = 'test_spd(sol.simplifyPath_{0:02d}, test_set)'
    _setup_ = 'from __main__ import test_spd, test_set, sol'
    _number_ = 10000
    from timeit import timeit
    print(timeit(stmt=_stmt_.format(1), setup=_setup_, number=_number_))
    print(timeit(stmt=_stmt_.format(2), setup=_setup_, number=_number_))
