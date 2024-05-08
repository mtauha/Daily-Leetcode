class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        n = len(score)
        rank = [0] * n
        sorted_scores = sorted(score, reverse=True)
        for i in range(n):
            index = score.index(sorted_scores[i])
            if i == 0:
                rank[index] = "Gold Medal"
            elif i == 1:
                rank[index] = "Silver Medal"
            elif i == 2:
                rank[index] = "Bronze Medal"
            else:
                rank[index] = f"{i+1}"

        return rank
