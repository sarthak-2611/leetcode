from functools import cache


class Solution:

    def partition(self, s: str) -> list[list[str]]:
        @cache
        def dfs(i: int) -> list[list[str]]:
            if i == len(s):
                return [[]]
            return [
                [s[i : j + 1]] + rest
                for j in range(i, len(s))
                if s[i : j + 1] == s[i : j + 1][::-1]
                for rest in dfs(j + 1)
            ]

        return dfs(0)

        