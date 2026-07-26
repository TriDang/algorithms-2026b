# Problem 1
# binary tree traversal
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def visit(node):
    print(node.data)

# def pre_order_traversal(node):
#     if node:
#         visit(node)
#         pre_order_traversal(node.left)
#         pre_order_traversal(node.right)

# def in_order_traversal(node):
#     if node:
#         in_order_traversal(node.left)
#         visit(node)
#         in_order_traversal(node.right)

# def post_order_traversal(node):
#     if node:
#         post_order_traversal(node.left)
#         post_order_traversal(node.right)
#         visit(node)

# def breadth_first_traversal(root):
#     if not root:
#         return
#     # use a queue to store the nodes to visit
#     queue = [root]
#     while queue:
#         current_node = queue.pop(0)
#         visit(current_node)
#         if current_node.left:
#             queue.append(current_node.left)
#         if current_node.right:
#             queue.append(current_node.right)

# test the binary tree traversal
# construct a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

# #       1
# #      / \
# #     2   3
# #    / \  /
# #   4  5 6

# print("Pre-order traversal:")
# pre_order_traversal(root) # 1, 2, 4, 5, 3, 6
# print("In-order traversal:")
# in_order_traversal(root) # 4, 2, 5, 1, 6, 3
# print("Post-order traversal:")
# post_order_traversal(root) # 4, 5, 2, 6, 3, 1
# print("Breadth-first traversal:")
# breadth_first_traversal(root) # 1, 2, 3, 4, 5, 6

# Problem 2
# Check if a binary tree is a binary search tree
def is_bst(node, min_value=float('-inf'), max_value=float('inf')):
    if node is None:
        return True
    if node.data < min_value or node.data > max_value:
        return False
    return (is_bst(node.left, min_value, node.data) and \
            is_bst(node.right, node.data, max_value))

# print("Is the binary tree a BST?", is_bst(root)) # False

# construct a binary search tree
root2 = TreeNode(4)
root2.left = TreeNode(2)
root2.right = TreeNode(6)
root2.left.left = TreeNode(1)
root2.left.right = TreeNode(3)
root2.right.left = TreeNode(5)

#      4
#     / \
#    2   6
#   / \  /
#  1  3 5

# print("Is the binary tree a BST?", is_bst(root2)) # True

# Problem 3
class TreeNodeWithParent:
    def __init__(self, parent, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent

# root is the node whose parent is None

# calculate the level of a node
def calculate_level(node):
    level = 0
    while node.parent:
        node = node.parent
        level += 1
    return level

# use level to find the lowest common ancestor of two nodes
# and based on that, calculate the distance between two nodes
def calculate_distance(node1, node2):
    level1 = calculate_level(node1)
    level2 = calculate_level(node2)
    # make node1 the deeper node
    if level1 < level2:
        node1, node2 = node2, node1
        level1, level2 = level2, level1
    # move node1 up until it is at the same level as node2
    distance = 0
    for _ in range(level1 - level2):
        node1 = node1.parent
        distance += 1
    # move both nodes up until they are the same
    while node1 and node2 and node1 != node2:
        node1 = node1.parent
        node2 = node2.parent
        distance += 2
    return distance

# test
root3 = TreeNodeWithParent(None, 10)
root3.left = TreeNodeWithParent(root3, 6)
root3.right = TreeNodeWithParent(root3, 14)
root3.left.left = TreeNodeWithParent(root3.left, 4)
root3.left.right = TreeNodeWithParent(root3.left, 8)
root3.right.left = TreeNodeWithParent(root3.right, 12)
root3.right.right = TreeNodeWithParent(root3.right, 16)
#      10
#     /  \
#    6    14
#   / \   / \
#  4   8 12 16

print("Distance between 4 and 8:", calculate_distance(root3.left.left, root3.left.right)) # 2
print("Distance between 4 and 12:", calculate_distance(root3.left.left, root3.right.left)) # 4
print("Distance between 4 and 6:", calculate_distance(root3.left.left, root3.left)) # 1
print("Distance between 4 and 14:", calculate_distance(root3.left.left, root3.right)) # 3

# Problem 4
# Given a binary search tree and a value X, return the node containing the minimum value Y
# in the tree such that Y >= X. If no such value exists, return None.

def find_min_greater_equal(node, X):
    if node is None:
        return None
    if node.data == X:
        return node
    if node.data < X:
        return find_min_greater_equal(node.right, X)
    else:
        left_result = find_min_greater_equal(node.left, X)
        return left_result if left_result is not None else node
    
# test
print("Minimum value greater than or equal to 5:", find_min_greater_equal(root3, 5).data) # 6
print("Minimum value greater than or equal to 6:", find_min_greater_equal(root3, 6).data) # 6
print("Minimum value greater than or equal to 7:", find_min_greater_equal(root3, 7).data) # 8
print("Minimum value greater than or equal to 9:", find_min_greater_equal(root3, 9).data) # 10
print("Minimum value greater than or equal to 17:", find_min_greater_equal(root3, 17)) # None