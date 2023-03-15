# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
      """
      To determine whether a binary tree is complete or not, we can use the following approach:
      Perform a level-order traversal of the tree using a queue. While traversing,
      we can mark the nodes with their indices as we encounter them from left to right.
      If we encounter a node that is not at the next index we expect, then the tree is not complete.
      If we reach the end of the level and all nodes are at their expected indices,
      we can continue to the next level. If there are any nodes in the queue after this step, then the tree is not complete.
      """
        if not root:
            return True
        
        queue = deque([(root, 1)])
        expected_index = 1
        last_level = False
        
        while queue:
            node, index = queue.popleft()
            
            if index != expected_index:
                return False
            
            if node.left:
                queue.append((node.left, 2*index))
            
            if node.right:
                queue.append((node.right, 2*index + 1))
            
            if last_level and queue:
                return False
            
            if not queue:
                last_level = True
            
            expected_index += 1
        
        return True
