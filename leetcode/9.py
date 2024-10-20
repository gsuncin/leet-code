class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Given an integer x, return true if x is a
        palindrome, and false otherwise.
        Input: x = 121
        Output: true
        Explanation: 121 reads as 121 from left to right and from right to left.
        """
        return str(x) == str(x)[::-1]
        
sol = Solution()
sol.isPalindrome(121)