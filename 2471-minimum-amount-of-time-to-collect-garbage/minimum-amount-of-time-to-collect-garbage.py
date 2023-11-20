class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # List to store the prefix sum in travel.
        prefixSum = [0] * (len(travel) + 1)
        prefixSum[1] = travel[0]
        for i in range(1, len(travel)):
            prefixSum[i + 1] = prefixSum[i] + travel[i]

        # Dictionary to store garbage type to the last house index.
        garbageLastPos = {}

        # Dictionary to store the total count of each type of garbage in all houses.
        garbageCount = {}
        for i in range(len(garbage)):
            for c in garbage[i]:
                garbageLastPos[c] = i
                garbageCount[c] = garbageCount.get(c, 0) + 1

        garbageTypes = ['M', 'P', 'G']
        ans = 0
        for c in garbageTypes:
            # Add only if there is at least one unit of this garbage.
            if c in garbageCount:
                ans += prefixSum[garbageLastPos[c]] + garbageCount[c]

        return ans
