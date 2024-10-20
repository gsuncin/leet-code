class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        mapping = {}

        if len(set(words)) != len(set(pattern)):
            return False

        for i, x in enumerate(pattern):
            mapping[x] = words[i]

        mounted_word = ""
        for i, x in enumerate(pattern):
            if i == (len(words) - 1):
                mounted_word += f"{mapping[x]}"
                continue
            mounted_word += f"{mapping[x]} "
        if mounted_word == s:
            return True
        return False

sol = Solution()
result = sol.wordPattern("abba", "dog cat cat dog")
result = sol.wordPattern("abba", "dog dog dog dog")
# "abba"
# "dog cat cat dog"
