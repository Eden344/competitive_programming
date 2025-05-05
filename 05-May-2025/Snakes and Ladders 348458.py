# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        def get_position(pos):
      
            row = n - 1 - (pos - 1) // n
            col = (pos - 1) % n
            if (n - 1 - row) % 2 == 1:
                col = n - 1 - col
            return board[row][col]
        
        queue = deque([1])
        visited = set([1])
        moves = 0
        
        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                if current == n * n:
                    return moves
                for next_pos in range(current + 1, min(current + 7, n * n + 1)):
                    destination = get_position(next_pos)
                    if destination != -1:
                        next_pos = destination
                    if next_pos not in visited:
                        visited.add(next_pos)
                        queue.append(next_pos)
            moves += 1
        
        return -1