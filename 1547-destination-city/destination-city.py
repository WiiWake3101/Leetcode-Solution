class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        mp={}
        seen={}
        for i in range(len(paths)):
            mp[paths[i][1]]=1
            mp[paths[i][0]]=1
            seen[paths[i][0]]=1
        for i in mp.keys():
            if i not in seen:
                return i  