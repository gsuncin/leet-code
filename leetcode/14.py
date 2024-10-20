from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # ["flower", "flow", "flight"]
        mcp = ""
        strs.sort()
        menor, maior = strs[0], strs[-1]
        for i in range(min(len(menor), len(maior))):
            if menor[i] != maior[i]:
                return mcp
            mcp += menor[i]
        return mcp

sol = Solution()
sol.longestCommonPrefix(["flower", "flow", "flight"])