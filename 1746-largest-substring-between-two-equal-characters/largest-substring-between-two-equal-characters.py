class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        max_distance = -1

        for left in range(len(s)):
            for right in range(left + 1, len(s)):
                if s[left] == s[right]:
                    max_distance = max(max_distance, right - left - 1)

        return max_distance
        