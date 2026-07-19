class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # search for a node with the given data
    # return the node if found, None if not found
    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return current_node
            current_node = current_node.next
        return None

    # append a new node at the end of the list
    # and return the new node
    def append(self, data):
        new_node = Node(data)
        # empty list, set head to new node
        if not self.head:
            self.head = new_node
            self.size += 1
            return new_node
        # otherwise, find the last node and set its next to new node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        self.size += 1
        return new_node

    # delete a node with the given data
    # return True if the node is deleted, False if not found
    def delete(self, data):
        # two pointers: current_node to traverse the list
        # previous_node to keep track of the previous node
        current_node = self.head
        previous_node = None
        while current_node:
            if current_node.data == data:
                # should remove current_node from the list
                if previous_node is None:
                    self.head = current_node.next
                else:
                    previous_node.next = current_node.next
                self.size -= 1
                return True
            previous_node = current_node
            current_node = current_node.next
        return False

    # insert a node after a given node
    # return the new node
    def insert_after(self, prev_node, data):
        if prev_node is None:
            return None
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.size += 1
        return new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

# Test
if __name__ == "__main__":
    list = LinkedList()
    list.append(1)
    list.print_list() # print 1
    list.append(2)
    list.append(3)
    list.print_list() # print 1, 2, 3
    node = list.search(2)
    print(node.data) # print 2
    list.insert_after(node, 4)
    list.print_list() # print 1, 2, 4, 3
    list.delete(1)
    list.print_list() # print 2, 4, 3
