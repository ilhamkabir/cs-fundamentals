from collections import deque

class TreeNode:
    def __init__(self, v):
        self.v = v
        self.left = None # Node() -> infinite recursion
        self.right = None
        self.children = []

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

def sorted_array_to_bst(array):
    # Time: O(n)
    # Space: O(n) + logn
    def helper(array, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(v=array[start])
        # mid = start+(end-start)//2 # this works too
        mid = (start+end)//2
        root = TreeNode(v=array[mid])
        root.left = helper(array, start, mid-1)
        root.right = helper(array, mid+1, end)
        return root
    root = helper(array, 0, len(array)-1)
    return tree_to_list(root)
    
# Time: O(n) (if done w/ a hashmap or dict)
# Space: O(n) + logn
def make_tree(pre_order, in_order):
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

# 426
def tree_to_dll(root):
    
    def dfs(node):
        nonlocal head, tail

        if not node: return

        dfs(node.left)

        # in-order traversal 
        if tail:
            tail.right = node
            node.left = tail
        else:
            head = node

        tail = node

        dfs(node.right)

    head, tail = None, None

    dfs(root)

    head.left = tail
    tail.right = head

    return head




if __name__ == "__main__":
    # r = sorted_array_to_bst([-10, -3, 0, 5, 9]) 
    # print(r)

    r = make_tree(
        pre_order=[3, 9, 20, 15, 7],
        in_order=[9, 3, 15, 20, 7]
    )
    print(r)