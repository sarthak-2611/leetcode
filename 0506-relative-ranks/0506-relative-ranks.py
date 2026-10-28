class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        d = {s: str(i) for i, s in enumerate(sorted(score, reverse=True), 1)}
        d.update(zip(sorted(score, reverse=True)[:3], ["Gold Medal", "Silver Medal", "Bronze Medal"]))
        return [d[s] for s in score]
