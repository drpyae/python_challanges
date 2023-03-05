class Solution:
    def minJumps(self, arr: List[int]) -> int:
      """ breadth-first search to wxplore all possible paths from the starting index to the last index"""

        n = len(arr)
        q = deque([(0, 0)]) # tuple: (index, num_jumps)
        visited = set([0])
        
        while q:
            i, jumps = q.popleft()
            
            if i == n-1:
                return jumps
            
            for j in range(i-1, i+1):
                if  0 <= j < n and j not in visited:
                    q.append((j, jumps + 1))
                    visited.add(j)
                    
            for k in range(n):
                if arr[k] == arr[i] and k != i and k not in visited:
                    q.append((k, jumps +1))
                    visited.add(i)
        
        return -1 # Not possible to reach the end
"""
