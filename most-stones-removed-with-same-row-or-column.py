class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        """
            On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.
            A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.
            Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.
        """
        n = len(stones)
        adjacency_list = [[] for _ in range(n)]

        for i in range(n):
            for j in range(i+1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    adjacency_list[i].append(j)
                    adjacency_list[j].append(i)

        ans = 0
        visited = [False]*n

        def dfs(stone):
            visited[stone] = True
            for neigh in adjacency_list[stone]:
                if not visited[neigh]:
                    dfs(neigh)
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
                ans += 1
        
        return n - ans
