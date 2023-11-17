class Solution:
    def isVowel(self, c):
        return c in 'aeiouAEIOU'

    def sortVowels(self, s: str) -> str:
        vowels = sorted([c for c in s if self.isVowel(c)])
        result = ""
        j = 0
        for i in range(len(s)):
            if self.isVowel(s[i]):
                result += vowels[j]
                j += 1
            else:
                result += s[i]
        return result