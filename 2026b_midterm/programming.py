# Function 1
# complexity = O(N)
def longest_rising_sublist(readings):
    current_len = 1  # current length of the rising sublist
    max_len = 1  # maximum length of the rising sublist found so far

    for i in range(1, len(readings)):
        if readings[i] > readings[i - 1]:
            current_len += 1
        else:
            current_len = 1

        max_len = max(max_len, current_len)

    return max_len

# Function 2
# complexity = O(N)
def process_text_editor(actions):
    # every letter is stored in a stack
    # when undo occur, the top letter is removed from the stack

    stack = []
    for action in actions:
        if action[0] == "type":
            stack.append(action[1])
        elif action[0] == "undo":
            stack.pop()
    # join the letters in the stack list to form the final string
    return "".join(stack)

# Function 3

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# complexity = O(N)
def sum_single_child_nodes(root):
    # use post-order traversal to visit all nodes
    # when a node is being visited, the values of its
    # left and right sub-trees are available
    # the node value is added to the sum if it has exactly one child
    if root is None:
        return 0
    sum = sum_single_child_nodes(root.left) + sum_single_child_nodes(root.right)
    if root.left is None and root.right is not None:
        sum += root.value
    elif root.left is not None and root.right is None:
        sum += root.value
    return sum
    

# Client Code

# Function 1
# Example 1
numbers = [3, 4, 6, 2, 5, 7 ,8, 1]
print("Function 1 output 1:", longest_rising_sublist(numbers)) # Expected output 4

# Example 2
numbers = [5, 5, 5]
print("Function 1 output 2:", longest_rising_sublist(numbers)) # Expected output: 1

# Function 2
# Example 1
actions = [ ("type", "A"),
            ("type", "B"),
            ("undo",),
            ("type", "C") ]
print("Function 2 output 1:", process_text_editor(actions)) # Expected output: AC

# Example 2
actions = [ ("type", "A"),
            ("type", "B"),
            ("type", "C"),
            ("undo",),
            ("undo",),
            ("type", "D") ]
print("Function 2 output 2:", process_text_editor(actions)) # Expected output: AD

# Function 3
# Example 1
root1 = TreeNode(8)
root1.left = TreeNode(3)
root1.right = TreeNode(10)
root1.left.left = TreeNode(6)
root1.right.right = TreeNode(14)
print("Function 3 output 1:", sum_single_child_nodes(root1)) # Expected output: 13

# Example 2
root2 = TreeNode(3)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
print("Function 3 output 2:", sum_single_child_nodes(root2)) # Expected output: 0
