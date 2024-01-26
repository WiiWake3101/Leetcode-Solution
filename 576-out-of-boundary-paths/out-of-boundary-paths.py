class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @lru_cache(None)
        def recursive_run(i,j,moves):
            if i>=m or j>=n or i<0 or j<0:
                return 1
            elif moves == 0:
                return 0
            out = recursive_run(i+1,j,moves-1)
            out += recursive_run(i-1,j,moves-1)
            out += recursive_run(i,j+1,moves-1)
            out += recursive_run(i,j-1,moves-1)
            return out
        return recursive_run(startRow,startColumn,maxMove) %(10**9+7)
