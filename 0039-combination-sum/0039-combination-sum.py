class Solution:

  def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
    dp = [[] for _ in range(target + 1)]
    dp[0] = [[]]

    for c in candidates:
      for i in range(c, target + 1):
        for comb in dp[i - c]:
          dp[i].append(comb + [c])

    return dp[target]

        