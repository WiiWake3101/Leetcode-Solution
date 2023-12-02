class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charsMap = {}
        result = 0
        for char in chars:
            if char not in charsMap:
                charsMap[char] = 1
            else:
                charsMap[char] += 1
        
        for word in words:
            charsMapCopy = charsMap.copy()
            end = True
            for char in word:
                if char in charsMapCopy and charsMapCopy[char] > 0:
                    charsMapCopy[char] -= 1
                else:
                    end = False
                    break
            if end:
                result += len(word)

        return result