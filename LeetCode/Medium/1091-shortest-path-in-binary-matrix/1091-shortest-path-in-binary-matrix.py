from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        shortest_len = -1
        row = len(grid)
        if grid[0][0] != 0 or grid[row-1][row-1] == 1: return shortest_len
        visited = [[False] * row for _ in range(row)]
        queue = deque()
        queue.append((0, 0, 1))
        delta = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1),
         (1, -1), (1, 0), (1, 1)]

        while queue:
            cur_r, cur_c, cur_len = queue.popleft()
            if cur_r == row - 1 and cur_c == row - 1:
                shortest_len = cur_len
                break
            for dr, dc in delta:
                next_r = cur_r + dr
                next_c = cur_c + dc
                if next_r >= 0 and next_r < row and next_c >=0 and next_c < row:
                    if grid[next_r][next_c] == 0 and not visited[next_r][next_c]:
                        queue.append((next_r, next_c, cur_len + 1))
                        visited[next_r][next_c] = True

        return shortest_len