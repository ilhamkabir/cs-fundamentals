# from queue import Queue
from collections import deque
import math

class TreeNode:
    def __init__(self, v):
        self.v = v
        self.left = None # Node() -> infinite recursion
        self.right = None
        self.children = []

def make_binary_tree():
    root = TreeNode(v=3)

    root.left = TreeNode(v=9)
    root.right = TreeNode(v=20)

    root.left.left = TreeNode(v=4)
    root.left.right = TreeNode(v=8)

    root.right.left = TreeNode(v=15)
    root.right.right = TreeNode(v=7)

    root.left.left.left = TreeNode(v=2)
    root.left.left.right = TreeNode(v=5)

    root.right.left.left = TreeNode(v=13)
    root.right.left.right = TreeNode(v=6)

    return root

def make_n_ary_tree():
    root = TreeNode(v=3)

    for v in [3, 2, 4]:
        node = TreeNode(v)
        root.children.append(node)

    for v in [5, 6]:
        node = TreeNode(v)
        root.children[0].children.append(node)

    return root

# Time: O(n)
# Space: O(n) ... Aux: queue + tmp. queue: (n+1)/2
def BFS_binary(root):
    result = []
    q = deque()
    q.append(root)
    while len(q):
        tmp = []
        count = len(q)        
        while count > 0:
            count -= 1
            curr_node = q.popleft()
            if curr_node.left: # don't add None
                q.append(curr_node.left)
            if curr_node.right:
                q.append(curr_node.right)
            tmp.append(curr_node.v)
        result.append(tmp)
    return result
    
# Time: O(n)
# Space: O(n) ... Aux: queue + tmp. queue: (n+1)/2
def BFS_n_ary(root):
    result = []
    q = deque()
    q.append(root)
    while len(q):
        tmp = []
        count = len(q)        
        while count > 0:
            count -= 1
            curr_node = q.popleft()
            for child in curr_node.children:
                q.append(child)
            tmp.append(curr_node.v)
        result.append(tmp)
    return result

def BFS_binary_zigzag(root):
    result = []
    q = deque()
    q.append(root)
    left_to_right = True
    while len(q):
        tmp = []
        count = len(q) 
        while count > 0:
            count -= 1
            curr_node = q.popleft()
            if curr_node.left: # don't add None
                q.append(curr_node.left)
            if curr_node.right:
                q.append(curr_node.right)
            tmp.append(curr_node.v)
        if left_to_right:
            result.append(tmp)
        else:
            result.append(tmp[::-1])
        left_to_right = not left_to_right
        
    return result

def right_side_view(root):
    result = []
    q = deque()
    q.append(root)
    while len(q):
        tmp = None
        count = len(q) 
        while count > 0:
            count -= 1
            curr_node = q.popleft()
            if curr_node.left: # don't add None
                q.append(curr_node.left)
            if curr_node.right:
                q.append(curr_node.right)
            tmp = curr_node.v
        result.append(tmp)
        
    return result

if __name__ == "__main__":
    root = make_binary_tree()

    r = right_side_view(root)
    print(r)