class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        elements = []
        curr_len = len(grid[0])
        counts = defaultdict(int)
        repeating, missing = -1, -1

        for row in grid:
            elements.extend(row)
        
        for i in elements:
            counts[i] += 1
            if counts[i] > 1:
                repeating = i

        for i in range(1, curr_len**2 + 1):
            if i not in counts.keys():
                missing = i
                break
        
        return [repeating, missing]
