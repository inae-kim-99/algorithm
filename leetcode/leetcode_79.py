# https://leetcode.com/problems/word-search/
# leetcode 79 : Word Search
# LEVEL : Medium 

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        row, col = len(board), len(board[0])
        visited = [[False for _ in range(col)] for _ in range(row)]

        def check_word(y, x, index):
            if board[y][x] != word[index]:
                return False
            if index == len(word)-1:
                return True

            for d in directions:
                dy = y + d[0]
                dx = x + d[1]
                if 0 <= dy < row and 0 <= dx < col and not visited[dy][dx]:
                    visited[dy][dx] = True
                    if check_word(dy, dx, index+1):
                        return True
                    visited[dy][dx] = False

            return False

        for i in range(row):
            for j in range(col):
                visited[i][j] = True
                if check_word(i, j, 0):
                    return True
                visited[i][j] = False

        return False
