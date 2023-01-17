
class TreeNode:
    def __init__(self, v):
        self.v = v
        self.left = None # Node() -> infinite recursion
        self.right = None
        self.children = []

def make_binary_tree():
    root = TreeNode(v=5)

    # root.left = TreeNode(v=4)
    # root.right = TreeNode(v=8)

    # root.left.left = TreeNode(v=11)

    # root.right.left = TreeNode(v=13)
    # root.right.right = TreeNode(v=4)

    # root.left.left.left = TreeNode(v=7)
    # root.left.left.right = TreeNode(v=2)

    # root.right.right.left = TreeNode(v=5)
    # root.right.right.right = TreeNode(v=1)

    root.left = TreeNode(v=1)
    root.right = TreeNode(v=5)

    root.left.left = TreeNode(v=5)
    root.left.right = TreeNode(v=5)

    root.right.right = TreeNode(v=5)

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

def compute_sum(root):
    if root is None: return 0
    leftsum = compute_sum(root.left)
    rightsum = compute_sum(root.right)
    return root.v + leftsum + rightsum

# Bottom up DFS
# Time: O(n)
# Space: O(n)
def diameter(root):
    max_diameter=[0]
    def helper(root):
        lmax = rmax = 0
        if root.left is not None:
            lmax = helper(root.left) + 1
        if root.right is not None:
            rmax = helper(root.right)+1
        curr_height = max(lmax, rmax)
        curr_diameter = lmax+rmax
        max_diameter[0]=max(max_diameter[0], curr_diameter)
        return curr_height
    if root is None:
        return
    helper(root)
    return max_diameter[0] 

# Time: O(n)
# Space: O(n) - Height of the tree (worst case)
def univalue_subtrees(root):
    univalue_subtrees = [0]
    def helper(root):
        
        if root.left is None and root.right is None:
            univalue_subtrees[0] += 1
            return True

        l_true = r_true = True # must be true

        if root.left is not None:
            l_true = helper(root.left) and (root.v == root.left.v) # COMPARISON MUST GO AFTER!!!
        if root.right is not None:
            r_true = helper(root.right) and root.v == root.right.v
        if l_true and r_true: univalue_subtrees[0] += 1
        return l_true and r_true
    if root is None:
        return 0
    helper(root)
    return univalue_subtrees[0]

if __name__ == "__main__":
    root = make_binary_tree()
    r = univalue_subtrees(root)
    print(r)

