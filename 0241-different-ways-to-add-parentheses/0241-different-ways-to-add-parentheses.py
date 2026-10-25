class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        memo = {}
        
        def solve(s: str) -> list[int]:
            if s.isdigit(): return [int(s)]
            if s in memo: return memo[s]
            
            res = []
            for i, c in enumerate(s):
                if c in '+-*':
                    left, right = solve(s[:i]), solve(s[i+1:])
                    res.extend(
                        l + r if c == '+' else l - r if c == '-' else l * r
                        for l in left for r in right
                    )
            memo[s] = res
            return res

        return solve(expression)

        