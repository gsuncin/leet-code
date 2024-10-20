"""

Given a string s, return the longest palindromic substring in s.
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        r_word = ""
        for el in range(len(s)):
            for j in range(len(s), -1, -1):
                word_a = s[el:j]
                word_b = s[::-1][el:j]
                if el == j or el > j or j == len(s):
                    break
                elif word_a == word_b:
                    if len(r_word) < len(word_a):
                        r_word = word_a
                elif s[el:j+1] == s[::-1][el:j + 1]:
                    if len(r_word) < len(word_a):
                        r_word = word_a
        return r_word
        # res = ""
        # resLen = 0

        # for i in range(len(s)):
        #     # odd length
        #     l, r = i, i
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         if (r - l + 1) > resLen:
        #             res = s[l : r + 1]
        #             resLen = r - l + 1
        #         l -= 1
        #         r += 1

        #     # even length
        #     l, r = i, i + 1
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         if (r - l + 1) > resLen:
        #             res = s[l : r + 1]
        #             resLen = r - l + 1
        #         l -= 1
        #         r += 1

        # return res
    
    
        # r_word = ""
        # # "abba"
        # for el in range(len(s)):
        #     for j in range(len(s), -1, -1):
        #         word_a = s[el:j]
        #         if len(s) % 2 != 0:
        #             word_b = s[::-1][el:j + 1]
        #         if el == j or el > j:
        #             break
        #         if word_a == word_b:
        #             if len(r_word) < len(word_a):
        #                 r_word = word_a
        # return r_word

    
    

        # repeated_words = {}
        # for i, n in enumerate(s):
        #     for ix, x in enumerate(s):

        #         if i == ix + 1:
        #             continue
        #         if x == n:
        #             if not repeated_words.get(n):
        #                 if i == ix:
        #                     repeated_words[n] = [i]
        #                     continue
        #                 repeated_words[n] = [i, ix]
        #             if i in repeated_words[n]:
        #                 continue
        #             repeated_words[n].append(i)
        # result = s[0]
        # possible_palindromes = []
        # for key, value in repeated_words.items():
        #     if len(value) > 1:
        #         possible_palindromes.append(s[value[0] : value[-1] + 1])
        # if not possible_palindromes:
        #     return result
        # possible_palindromes.sort(key=len)
        # possible_palindromes.reverse()
        # return possible_palindromes[0]


sol = Solution()
result = sol.longestPalindrome("abba")
print(result)
