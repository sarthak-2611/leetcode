class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        return "".join(sorted(str(n))) in {"".join(sorted(str(1 << i))) for i in range(30)}

        
        