class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp={}
        ans=[]
        for s in strs:
            sorted_strs=''.join(sorted(s))
            if sorted_strs in mp:
                ans[mp[sorted_strs]].append(s)
            else:
                mp[sorted_strs]=len(ans)
                ans.append([s])
        return ans