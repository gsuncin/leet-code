"""
Two players pick two tiles from a bag of tiles. Each player can take 6 tiles.
They will pick two tiles at a time and the player with the higher total score wins.
The winner is determinated by the player that has the highest tile score.
The player with the higher total score wins.
The bag of tiles is represented by a list of integers.

"""

import random
from typing import List


class Solution:
    def determinate_winner(self, tiles: List[int]) -> str:
        player1 = 0
        player2 = 0
        for i in range(0, len(tiles), 2):
            if len(tiles) < 2:
                break
            player1 += tiles.pop(random.randint(1, len(tiles)) - 1)
            player2 += tiles.pop(random.randint(1, len(tiles)) - 1)
        return "Player 1" if player1 > player2 else "Player 2"


sol = Solution()
print(sol.determinate_winner([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Player 1
print(sol.determinate_winner([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))  # Player 1
