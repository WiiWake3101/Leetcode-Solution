graph = [
    [4,6],
    [6,8],
    [7,9],
    [4,8],
    [0,3,9],
    [],
    [0,1,7],
    [2,6],
    [1,3],
    [2,4],
]

MOD = 10**9+7

DP = [0, 10]
state = [1] * 10
nxt_state = [0] * 10

class Solution:
    def knightDialer(self, n: int) -> int:
        global state, nxt_state
        for _ in range(len(DP), n+1):
            nxt_state[:] = [0] * 10
            for cur, ct in enumerate(state):
                for nxt in graph[cur]:
                    nxt_state[nxt] += ct
            for i in range(10):
                nxt_state[i] %= MOD

            DP.append( sum(nxt_state) % MOD )
            state,nxt_state = nxt_state,state
        return DP[n]