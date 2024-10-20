input = "abcabcbb"


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substrings = {}
        initial = 0
        result = 0
        for i, x in enumerate(s):
            if x in substrings:
                initial = max(initial, substrings[x] + 1)
            result = max(result, (i - initial + 1))
            substrings[x] = i
        return result


sol = Solution()
sol.lengthOfLongestSubstring(input)
