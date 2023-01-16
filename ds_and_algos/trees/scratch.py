from collections import deque
# from tree_node import TreeNode

class TreeNode:
    def __init__(self, v):
        self.v = v
        self.left = None # Node() -> infinite recursion
        self.right = None
        self.children = []

# def insert(root, key):
#     # TODO: keep track of previous!!
#     prev = None
#     curr = root
#     while curr:
#         if key == curr.v:
#             raise ValueError
#         prev = curr
#         if key < curr.v:
#             curr = curr.left
#         else:
#             curr = curr.right

#     if key < prev.v:
#         prev.left = TreeNode(key)
#     else:
#         prev.right = TreeNode(key)
#     return root

# root = TreeNode(10)
# root = insert(root, 8)
# root = insert(root, 12)
# root = insert(root, 17)
# root = insert(root, 6)
# root = insert(root, 13)

# def search(root, key):
#     pass

# # search(root, 17)
# # search(root, 3)

def tree_to_list(root):
    result = []
    q = deque()
    q.append(root)
    while len(q):
        curr_node = q.popleft()
        if curr_node is None:
            result.append(None)
            continue
        result.append(curr_node.v)
        q.append(curr_node.left)
        q.append(curr_node.right)
    return result

def make_tree_pre(pre_order, in_order):
    def helper(pre_order, pos, poe, in_order, ios, ioe):
        if pos == poe:
            return TreeNode(pre_order[pos])

        # create a hashmap of the inorder elems and indexes to optimize time complexity
        # otherwise time for just this is O(n)
        root_index = in_order.index(pre_order[pos])

        in_order_left = root_index - ios

        root = TreeNode(v=pre_order[pos])

        root.left = helper(
            pre_order = pre_order, 
            pos=pos+1, 
            poe=pos+in_order_left, 
            in_order = in_order, 
            ios = ios, 
            ioe = root_index-1
        )

        root.right = helper(
            pre_order=pre_order, 
            pos=pos+1+in_order_left, 
            poe=poe, 
            in_order=in_order, 
            ios=root_index+1, 
            ioe=ioe
        )
        
        return root
    root = helper(pre_order, 0, len(pre_order)-1, in_order, 0, len(in_order)-1)
    return tree_to_list(root)

r = make_tree_pre(
    pre_order=[3, 9, 20, 15, 7],
    in_order=[9, 3, 15, 20, 7]
)
print(r)

# def make_tree_post(in_order, post_order):
#     def f(i_s, i_e, p_s, p_e):
#         # base case 
#         if p_s == p_e:
#             return TreeNode(post_order[p_e])
#         root_index = in_order.index(post_order[p_e])
#         in_order_left_size = root_index - i_s
        
#         root = TreeNode(in_order[root_index])
#         root.left = f(
#             i_s = i_s,
#             i_e = root_index,
#             p_s = p_s, 
#             p_e = p_s + in_order_left_size
#         )
#         root.right = f(
#             i_s = root_index + 1,
#             i_e = i_e,
#             p_s = p_s + in_order_left_size,
#             p_e = p_e - 1
#         )
#         return root
#     root = f(0, len(in_order)-1, 0, len(post_order)-1)
#     return root

# r = make_tree_post(
#     in_order=[9, 3, 15, 20, 7],
#     post_order=[9, 15, 7, 20, 3]
# )
# print(r)