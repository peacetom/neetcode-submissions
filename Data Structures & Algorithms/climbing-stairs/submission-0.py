class Solution:
    def climbStairs(self, n: int) -> int:
        return self._climbStairs(n, {})


    def _climbStairs(self, n, memo):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n in memo:
            return memo[n]

        memo[n] = self._climbStairs(n-1, memo) + self._climbStairs(n-2, memo)

        return memo[n]

        