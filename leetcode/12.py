class Solution:
    def intToRoman(self, num: int) -> str:
        values = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1,
        }
        am = num
        result = ""
        while am != 0:
            for k, v in values.items():
                if am == 0:
                    break
                if am >= v:
                    x = am // v
                    am = am % v
                    result += (x * k)
        return result

sol = Solution()
sol.intToRoman(3749)