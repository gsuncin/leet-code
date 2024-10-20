from copy import deepcopy
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        aux_board = deepcopy(board)
        directions = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]

        for row in range(m):
            for col in range(n):
                live_neighboard = 0
                for d in directions:
                    n_row, n_col = row + d[0], col + d[1]
                    if n_row >= 0 and n_row < m and n_col >= 0 and n_col < n and board[n_row][n_col] == 1:
                        live_neighboard += 1
                # checking conditions
                if board[row][col] == 1:
                    if live_neighboard < 2 or live_neighboard > 3:
                        aux_board[row][col]=0
                else:
                    if live_neighboard == 3:
                        aux_board[row][col] = 1
        # update board
        board[:] = aux_board
                
sol = Solution()
sol.gameOfLife([[0,1,0], [0,0,1],[1,1,1], [0,0,0]])
sol.gameOfLife([[0]])
sol.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])