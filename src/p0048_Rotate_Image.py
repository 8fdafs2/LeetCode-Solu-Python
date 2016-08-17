class Solution(object):

    def __init__(self):
        self.rotate = self.rotate_01

    # Transpose and Col-Interchange
    # Your runtime beats 15.94% of pythonsubmissions.
    def rotate_01(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # in-place transpose
        for i in range(n):
            for j in range(i + 1, n):
                # matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        # in-place interchange
        for i in range(n):
            matrix[i].reverse()

    # Rotate Ring-by-Ring
    # Your runtime beats 15.94% of pythonsubmissions.
    def rotate_02(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # for r in range(n // 2):
        #     for i in range(r, n - 1 - r):
        #         # left-side, top-side, right-side, bot-side =
        #         # bot-side, left_side, top-side, right-side
        #         matrix[i][r], matrix[r][n - i - 1], matrix[n - i - 1][n - 1 - r], matrix[n - 1 - r][i] = \
        #         matrix[n - 1 - r][i], matrix[i][r], matrix[r][n - i - 1], matrix[n - i - 1][n - 1 - r]
        for r in range(n // 2):
            n_1_r = n - 1 - r
            for i in range(r, n_1_r):
                n_1_i = n - 1 - i
                temp = matrix[i][r]
                matrix[i][r] = matrix[n_1_r][i]
                matrix[n_1_r][i] = matrix[n_1_i][n_1_r]
                matrix[n_1_i][n_1_r] = matrix[r][n_1_i]
                matrix[r][n_1_i] = temp

    # Rotate Block-by-Block
    # Your runtime beats 28.79% of pythonsubmissions.
    def rotate_03(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        c = (n + 1) // 2
        # for x in range(n // 2):
        #     for y in range(c):
        #         # left-side, top-side, right-side, bot-side =
        #         # bot-side, left_side, top-side, right-side
        #         matrix[x][y], matrix[y][n - 1 - x], matrix[n - 1 - x][n - 1 - y], matrix[n - 1 - y][x] = \
        #         matrix[n - 1 - y][x], matrix[x][y], matrix[y][n - 1 - x], matrix[n - 1 - x][n - 1 - y]
        for x in range(n // 2):
            n_1_x = n - 1 - x
            for y in range(c):
                n_1_y = n - 1 - y
                temp = matrix[x][y]
                matrix[x][y] = matrix[n_1_y][x]
                matrix[n_1_y][x] = matrix[n_1_x][n_1_y]
                matrix[n_1_x][n_1_y] = matrix[y][n_1_x]
                matrix[y][n_1_x] = temp


from copy import deepcopy
from pprint import pprint


def set_gen(rotate):
    def mat_gen(n):
        return [list(range(n * i, n * (i + 1))) for i in range(n)]
    test_set = []
    for i in range(2, 100):
        mat = mat_gen(i)
        match = deepcopy(mat)
        rotate(match)
        test_set.append((mat, match))
    return test_set


def test(rotate, test_set):
    for mat, match in test_set:
        rotate(mat)
        try:
            assert(mat == match)
        except AssertionError as ex:
            print(match, mat)
            print(ex)


def test_spd(rotate, test_set):
    for mat, _ in test_set:
        rotate(mat)


if __name__ == '__main__':
    sol = Solution()
    # prep
    print('prep...')
    test_set = set_gen(sol.rotate)
    # test
    print('test...')
    test(sol.rotate_01, deepcopy(test_set))
    test(sol.rotate_02, deepcopy(test_set))
    test(sol.rotate_03, deepcopy(test_set))
    # test_spd
    print('test_spd...')
    _stmt_ = 'test_spd(sol.rotate_{0:02d}, test_set)'
    _setup_ = 'from __main__ import test_spd, test_set, deepcopy, sol; test_set = deepcopy(test_set)'
    _number_ = 100
    from timeit import timeit
    print(timeit(stmt=_stmt_.format(1), setup=_setup_, number=_number_))
    print(timeit(stmt=_stmt_.format(2), setup=_setup_, number=_number_))
    print(timeit(stmt=_stmt_.format(3), setup=_setup_, number=_number_))