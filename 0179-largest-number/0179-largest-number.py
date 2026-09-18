class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        res = "".join(sorted(map(str, nums), key=cmp_to_key(lambda x, y: 1 if x + y < y + x else -1)))
        return res if res[0] != "0" else "0"
        