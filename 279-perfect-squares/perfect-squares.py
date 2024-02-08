class Solution:
    def numSquares(self, n: int) -> int:
        perfectSquares = [i**2 for i in range(1, math.floor(math.sqrt(n) + 1))]
        def isPerfectSquare(num: int) -> bool:
            temp = math.floor(math.sqrt(num))
            return temp ** 2 == num

        # print(perfectSquares)
        
        if isPerfectSquare(n):
            return 1

        candidates = set()
        for item in perfectSquares:
            candidates.add(n - item)
        ans = 1

        while candidates:
            # print(candidates)
            nextCandidates = set()
            for candidate in candidates:
                if isPerfectSquare(candidate):
                    return ans + 1
                for item2 in perfectSquares:
                    if item2 > candidate:
                        break
                    if item2 not in nextCandidates:
                        nextCandidates.add(candidate - item2)
            candidates = nextCandidates
            ans += 1
        
        return ans