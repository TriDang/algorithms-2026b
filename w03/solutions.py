from LinkedList import Node, LinkedList

# # Problem 1
# # Remove a loop in a linked list
def remove_loop(head):
    if head is None:
        return
    slow = head
    fast = head
    loop_found = False
    # first, detect if there is a loop
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            loop_found = True
            break
    if not loop_found:
        return

    # count the number of nodes in the loop
    loop_length = 1
    current = fast.next
    while current != fast:
        loop_length += 1
        current = current.next
    
    # move one pointer ahead by loop_length steps
    fast = head
    for _ in range(loop_length):
        fast = fast.next
    
    # move both pointers one step at a time until their nexts meet
    # they will meet at the start of the loop
    slow = head
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next

    # now fast.next is the start of the loop, break the loop    
    fast.next = None

# test
# create 10 linked nodes
# one point to the next, and the last one points back to the 4th node
# head = Node(1)
# current = head
# for i in range(2, 11):
#     current.next = Node(i)
#     current = current.next
# current.next = head.next.next.next # create a loop

# # before removing loop, let print the list 20 times, it will print 1 to 10,
# # and then print 4 to 10 again, and then print 4 to 10 again
# print("Before removing loop:")
# current = head
# for _ in range(20):
#     print(current.data)
#     current = current.next
#     if not current:
#         break

# # remove the loop
# print("After removing loop:")
# remove_loop(head)
# # after removing loop, let print the list 20 times, it will print 1 to 10 once and then stop
# current = head
# for _ in range(20):
#     print(current.data)
#     current = current.next
#     if not current:
#         break

# Problem 2
# Implement a circular linked list with two methods: append and delete
# class CircularLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.size = 0

#     # append a node with the given data to the end of the list
#     # return the new node
#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#         if self.tail:
#             self.tail.next = new_node
#         self.tail = new_node
#         new_node.next = self.head
#         self.size += 1
#         return new_node

#     # delete a node after a given node
#     def delete(self, prev_node, delete_node):
#         # if the list is empty, return False
#         if self.size == 0:
#             return False
#         # if the node to delete is the head node
#         if delete_node == self.head:
#             if self.size == 1: # only one node in the list
#                 self.head = None
#                 self.tail = None
#             else:
#                 self.head = delete_node.next
#                 self.tail.next = self.head
#             self.size -= 1
#             return True
#         # if the node to delete is the tail node
#         if delete_node == self.tail:
#             prev_node.next = self.head
#             self.tail = prev_node
#             self.size -= 1
#             return True
#         # if the node to delete is in the middle
#         prev_node.next = delete_node.next
#         self.size -= 1
#         return True

# # test
# circular_list = CircularLinkedList()
# # original Josephus problem with 41 people and step size 3
# for i in range(1, 42):
#     circular_list.append(i)
# current = circular_list.head
# while circular_list.size > 1:
#     # move current pointer 1 step (2nd position)
#     current = current.next
#     # delete the next node (3rd position)
#     print("Eliminate:", current.next.data)
#     circular_list.delete(current, current.next)
#     current = current.next # move to the 1st of next round
# # the last remaining node is the survivor
# print("The last one is:", circular_list.head.data)

# Problem 3
# class Queue:
#     def __init__(self):
#         self.capacity = 100
#         self.items = [None] * self.capacity
#         self.size = 0
#         self.front = 0
#         self.rear = 0

#     def enqueue(self, item):
#         if self.size < self.capacity:
#             self.items[self.rear] = item
#             self.rear = (self.rear + 1) % self.capacity
#             self.size += 1

#     def dequeue(self):
#         if self.size > 0:
#             item = self.items[self.front]
#             self.front = (self.front + 1) % self.capacity
#             self.size -= 1
#             return item
#         return None

# class Event:
#     def __init__(self, arrival, duration):
#         self.arrival = arrival
#         self.duration = duration

# # test
# queue = Queue()
# queue.enqueue(Event(0, 5))
# queue.enqueue(Event(3, 3))
# queue.enqueue(Event(4, 4))
# queue.enqueue(Event(100, 4))

# n = queue.size
# next_available_time = 0
# total_waiting_time = 0
# max_waiting_time = 0

# while queue.size > 0:
#     evt = queue.dequeue()
#     next_available_time = max(next_available_time, evt.arrival)
#     waiting_time = next_available_time - evt.arrival
#     max_waiting_time = max(max_waiting_time, waiting_time)
#     total_waiting_time += waiting_time
#     next_available_time += evt.duration

# print(f"Max waiting time {max_waiting_time}")
# print(f"Total waiting time {total_waiting_time}")
# print(f"Average waiting time {total_waiting_time / n}")


# Problem 4
class Stack:
    def __init__(self):
        self.size = 0
        self._items = []

    def push(self, item):
        self._items.append(item)
        self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self._items.pop()
        return None

    def peek(self):
        if self.size > 0:
            return self._items[-1]
        return None

    def is_empty(self):
        return self.size == 0

# str = input("Enter an expression that contains parentheses: ")
# stack = Stack()
# balanced = True
# for char in str:
#     if char in '([{':
#         stack.push(char)
#     else:
#         if stack.is_empty():
#             balanced = False
#             break
#         top = stack.pop()
#         if ((char == ')' and top != '(')) or \
#            ((char == ']' and top != '[')) or \
#            ((char == '}' and top != '{')):
#             balanced = False
#             break
# if not stack.is_empty():
#     balanced = False
# if balanced:
#     print("The parentheses are balanced.")
# else:
#     print("The parentheses are not balanced.")


# Problem 5
def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

# str = input("Enter an infix expression: ")
# tokens = str.split()
# stack = Stack()
# postfix = []

# for token in tokens:
#     if token == '(':
#         stack.push(token)
#         continue
#     elif token == ')':
#         while stack and stack.peek() != '(':
#             postfix.append(stack.pop())
#         stack.pop()  # Pop the '(' from the stack
#         continue
#     if token.isalnum():  # If the token is an operand
#         postfix.append(token)
#     else:  # If the token is an operator
#         while (stack and precedence(stack.peek()) >= precedence(token)):
#             postfix.append(stack.pop())
#         stack.push(token)

# while not stack.is_empty():
#     postfix.append(stack.pop())

# print("Postfix expression:", " ".join(postfix))

# # evaluate the postfix expression
# eval_stack = Stack()
# for token in postfix:
#     if token.isalnum():  # If the token is an operand
#         eval_stack.push(int(token))
#     else:  # If the token is an operator
#         second = eval_stack.pop()
#         first = eval_stack.pop()
#         if token == '+':
#             eval_stack.push(first + second)
#         elif token == '-':
#             eval_stack.push(first - second)
#         elif token == '*':
#             eval_stack.push(first * second)
#         elif token == '/':
#             eval_stack.push(first / second)
# print("Evaluation result:", eval_stack.pop())