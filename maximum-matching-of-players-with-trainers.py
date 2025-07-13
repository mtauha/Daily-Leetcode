class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        
        players.sort()
        trainers.sort()
        ans = 0
        m, n = len(players), len(trainers)
        i, j = 0, 0

        while i < m and j < n:
            while j < n and players[i] > trainers[j]:
                j += 1
            if j < n:
                ans += 1
            i += 1
            j += 1

        return ans

        
