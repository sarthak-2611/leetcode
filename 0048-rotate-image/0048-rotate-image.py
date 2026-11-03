class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        matrix[:] = [list(row) for row in zip(*matrix[::-1])]
        