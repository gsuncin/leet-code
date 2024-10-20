from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != amount + 1 else -1


sol = Solution()
# result = sol.coinChange([1, 2, 5], 11)
# result = sol.coinChange([2], 3)
# result = sol.coinChange([1], 0)
result = sol.coinChange([186, 419, 83, 408], 6249)
