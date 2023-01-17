from collections import deque

class TreeNode:
    def __init__(self, v):
        self.v = v
        self.left = None # Node() -> infinite recursion
        self.right = None
        self.children = []

# 102
def level_order(root):
    result=[]
    q= deque()
    q.append(root)
    while q:
        count = len(q)
        tmp = []
        for i in range(count):
            curr = q.popleft()
            tmp.append(curr.v)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        result.append(tmp)
    return result

#429 
def n_ary_level_order(root):
    result = []
    q = deque()
    q.append(root)
    while q:
        count = len(q)
        tmp = []
        for i in range(count):
            curr = q.popleft()
            tmp.append(curr.v)
            for child in curr.children:
                q.append(child)
        result.append(tmp)
    return result

# 149 Binary Tree Right Side View
def right_side_view(root):
    result = []
    q = deque()
    q.append(root)
    while q:
        count = len(q)
        tmp = []
        for i in range(count):
            curr = q.popleft()
            tmp.append(curr.v)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        if tmp:
            result.append(tmp[-1])
    return result

# 112
def path_sum(root, sum):
    ans = [False]
    def helper(root, target):
        target = target-root.v
        if target == 0 and root.left is None and root.right is None:
            ans[0] = True
            return
        if target < 0: # remove this if negative numbers are allowed
            return
        if root.left:
            helper(root.left, target)
        if root.right:
            helper(root.right, target)
    helper(root, sum)
    return ans[0]

def array_to_bst(array):
    pass
    
# Time: O(n) (if done w/ a hashmap or dict)
# Space: O(n) + logn
def make_tree(pre_order, in_order):
    pass

# 426
def tree_to_dll(root):
    pass

def binary_root():
    root = TreeNode(3)

    root.left = TreeNode(9)
    root.right = TreeNode(20)

    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root

def _n_ary_root():
    root = TreeNode(3)

    for i in [3,2,4]:
        curr = TreeNode(i)
        root.children.append(curr)

    root.children[0].children.append(TreeNode(5))
    root.children[0].children.append(TreeNode(6))

    return root

if __name__ == "__main__":
    
    root = binary_root()

    print('tree:', tree_to_list(root))

    print('level order:', level_order(root))

    n_ary_root = _n_ary_root()

    print('n-ary level order:', n_ary_level_order(n_ary_root))

    print('right side view:', right_side_view(root))

    print('path sum:', path_sum(root, 12))