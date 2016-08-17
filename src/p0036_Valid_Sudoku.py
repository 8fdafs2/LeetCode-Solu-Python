class Solution(object):

    def __init__(self):
        self.isValidSudoku = self.isValidSudoku_01

    # Your runtime beats 55.62% of pythonsubmissions.
    def isValidSudoku_01(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            row = [ele for ele in row if ele != '.']
            if len(set(row)) != len(row):
                return False

        for col in zip(*board):
            col = [ele for ele in col if ele != '.']
            if len(set(col)) != len(col):
                return False

        for i_row_set in [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
            for i_col_set in [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
                blk = [ele for ele in [board[i_row][i_col] for i_col in i_col_set for i_row in i_row_set] if ele != '.']
                if '.' not in blk and len(set(blk)) != len(blk):
                    return False

        return True

    # Your runtime beats 13.70% of pythonsubmissions.
    def isValidSudoku_02(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            row = {}
            col = {}
            blk = {}
            for j in range(9):

                ele_row = board[i][j]
                if ele_row != '.':
                    if ele_row in row:
                        return False
                    row[ele_row] = None

                ele_col = board[j][i]
                if ele_col != '.':
                    if ele_col in col:
                        return False
                    col[ele_col] = None

                ele_blk = board[i // 3 * 3 + j // 3][i % 3 * 3 + j % 3]
                if ele_blk != '.':
                    if ele_blk in blk:
                        return False
                    blk[ele_blk] = None

        return True


if __name__ == '__main__':
    sol = Solution()
    bd = [".87654321",
          "2........",
          "3........",
          "4........",
          "5........",
          "6........",
          "7........",
          "8........",
          "9........"]
    print(sol.isValidSudoku(bd))
    bd = ["..4...63.",
          ".........",
          "5......9.",
          "...56....",
          "4.3.....1",
          "...7.....",
          "...5.....",
          ".........",
          "........."]
    print(sol.isValidSudoku(bd))
