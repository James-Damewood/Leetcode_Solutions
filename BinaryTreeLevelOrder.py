# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if root == None:
            return []
        
        queue = collections.deque()
        
        queue.appendleft((root,0))
        
        lvl_ord = []
        depth = -1
        
        while queue:
            curr_node,curr_depth = queue.pop()
            if curr_depth > depth:
                lvl_ord.append([])
                depth = curr_depth
                
            lvl_ord[depth].append(curr_node.val)
            
            if (curr_node.left != None):
                queue.appendleft((curr_node.left,depth+1))
            if (curr_node.right != None):
                queue.appendleft((curr_node.right,depth+1))
                
        return lvl_ord
