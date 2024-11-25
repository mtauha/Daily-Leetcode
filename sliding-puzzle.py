class Solution:
    """
        On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

        The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

        Given the puzzle board board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.
    """
    directions = [
        [1, 3],
        [0, 2, 4],
        [1, 5],
        [0, 4],
        [3, 5, 1],
        [4, 2],
    ]

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def _swap(s, i, j):
            s = list(s)
            s[i], s[j] = s[j], s[i]
            return "".join(s)

        start_state = "".join(str(num) for row in board for num in row)

        visited = {}

        def _dfs(state, zero_pos, moves):
            if state in visited and visited[state] <= moves:
                return
            visited[state] = moves

            for next_pos in self.directions[zero_pos]:
                new_state = _swap(
                    state, zero_pos, next_pos
                ) 
                _dfs(
                    new_state, next_pos, moves + 1
                ) 

        _dfs(start_state, start_state.index("0"), 0)

        return visited.get("123450", -1)
