class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        length = -1
        myhash= {}
        
        for i in range(len(s)):
            
            if s[i] not in myhash:
                myhash[s[i]] = i
            else:
                length = max(length , i- myhash.get(s[i]) -1)
                
        return length
        