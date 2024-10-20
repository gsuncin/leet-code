class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
        Symbol       Value
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        """
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        "XIV"
        value = 0
        for i in range(len(s)):
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                value -= values[s[i]]
            else:
                value += values[s[i]]
        return value

sol = Solution()
# sol.romanToInt("III")
# sol.romanToInt("IV")
# sol.romanToInt("IX")
# sol.romanToInt("LVIII")
sol.romanToInt("MCMXCIV")