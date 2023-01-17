
class TreeNode:
    def __init__(self, v):
        self.v = v
        self.left = None # Node() -> infinite recursion
        self.right = None
        self.children = []

def make_binary_tree():
    root = TreeNode(v=5)

    root.left = TreeNode(v=4)
    root.right = TreeNode(v=8)

    root.left.left = TreeNode(v=11)

    root.right.left = TreeNode(v=13)
    root.right.right = TreeNode(v=4)

    root.left.left.left = TreeNode(v=7)
    root.left.left.right = TreeNode(v=2)

    root.right.right.left = TreeNode(v=5)
    root.right.right.right = TreeNode(v=1)

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

# # review optimizations!! 
# def root_to_leaf_sum(root, target):
#     # value type can't be updated from outside this scope. 
#     # must be a reference type 
#     has_found = [False] # make into a ref type
#     def helper(root, target):
#         if root is None: 
#             return False
#         target -= root.v
#         if root.left is None and root.right is None and target == 0:
#             has_found[0] = True
#             return
#         return helper(root.left, target) or helper(root.right, target)

#     helper(root, target)
#     return has_found[0]

# Time: O(n) - touching each node once 
# Space: O(n) - height of a tree in max case (max stack trace)
def root_to_leaf_sum(root, target):
    if root is None: return False
    target -= root.v
    if root.left is None and root.right is None:
        return target == 0
    return root_to_leaf_sum(root.left, target) or root_to_leaf_sum(root.right, target)

# Time: total # of leaf nodes: (n+1)/2 -> balance tree: O(nlog(n)) # leafs (this many copies) * height
# Space: height (system stack) + nlog(n) for output => O(nlogn)
def root_to_leaf_sum_all(root, target):
    result = []
    def helper(root, target, slate=[]):
        if root is None: return
        target -= root.v
        slate.append(root.v)
        if root.left is None and root.right is None:
            if target == 0:
                result.append(slate[:])
                slate.pop() # unnecessary 
                return
        helper(root.left, target, slate) # can make copy of the slate here too
        helper(root.right, target, slate)
        slate.pop()
    helper(root, target)
    return result

if __name__ == "__main__":
    root = make_binary_tree()
    print('#113. path sum II:', root_to_leaf_sum_all(root, 22))