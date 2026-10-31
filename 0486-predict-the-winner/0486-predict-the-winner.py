class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        if len(nums) % 2 == 0 or len(nums) <= 2: return True
        
        dp = list(nums)
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])
                
        return dp[-1] >= 0

        