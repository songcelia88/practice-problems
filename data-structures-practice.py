# linked list
# Node with data and next node
# Linked list class with head and tail
# traverse the linked list
class LLNode(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class LinkedList(object):
    def __init__(self, head_data=None):
        """initialize linked list with optional head"""
        self.head = None
        self.tail = None

        if head_data:
            self.add_node(head_data)

    def add_node(self, data):
        """Add node to the linked list"""
        # if there is no head, then make the node the head and the tail
        # if there is a head and tail, get the tail info, set it's next node to the new node,
        # set the new tail to be the new node
        new_node = LLNode(data)

        if self.head is None:
            self.head = new_node    
        else:
            current = self.head
            
            # find the last node
            while current:
                current = current.next
            
            current.next = new_node

        self.tail = new_node


# tree
class TreeNode(object):
    def __init__(self, data, children=None):
        # children is a list
        self.data = data
        self.children = []
        if children:
            self.children.extend(children)

    def add_children(self, children):
        # children is a list of tree nodes
        self.children.extend(children)

    def find_node(self, node_data):
        # returns True if found
        # returns False if not found

        # start at the root
        # keep track of nodes we need to see 
        # for BFS add nodes to end and take from beginning
        # for DFS add nodes to the end and take from the end
        # loop through these nodes until you find the node or the list is empty

        nodes_to_check = [self]

        while nodes_to_check:
            current = nodes_to_check.pop(0) # pop from the beginning for BFS
            if current.data == node_data:
                return True
            nodes_to_check.extend(current.children)

        return False

    def find_node_recursive(self, node_data):
        # base case is if the self.data is equal to node_data
        # else go through each of the children and run the find_node_recursive function and return their values
            # use the Python any function on the list of returned values from the children
        # else return False

        if self.data == node_data:
            return True
        elif self.children:
            values = []
            for child in self.children:
                values.append(child.find_node_recursive(node_data))
            return any(values) # returns True if any of the values are True
        else:
            return False
        


class Tree(object):
    def __init__(self, root=None):
        self.root = root



# binary tree has left and right data

# graph
class GraphNode(object):
    def __init__(self, data, adjacent=None):
        # adjacent is input as a list, make it a set
        self.data = data
        self.adjacent = set()

        if adjacent:
            for node in adjacent:
                self.adjacent.add(node)

class Graph(object):
    def __init__(self):
        self.nodes = set()


    def add_node(self, new_node):
        self.nodes.add(new_node)


    def add_connection(self, node1, node2):
        node1.adjacent.add(node2)
        node2.adjacent.add(node1)


    def find_node(self, node_data):
        # add all nodes to the to_check list
        # keep track of nodes we have seen
        # only add nodes to_check if we haven't seen them yet
        seen = set()
        to_check = self.nodes

        while to_check:
            current = to_check.pop()
            if current.data == node_data:
                return True
            seen.add(current)

            for node in current.adjacent:
                if node not in seen:
                    to_check.add(current)

        return False

    def find_node_recurse(self, node_data, seen=set()):
        # CHECK THIS, not sure if this works, 
        if self.data = node_data:
            return True
        elif self.adjacent:
            values = []
            seen.add(current) # current node
            for node in self.adjacent:
                if node not in seen:
                    values.append(self.find_node_recurse(), seen)
            return any(values)

        else:
            return False


# stacks (last in, first out) - implement with a Python list
# reverse stack 
# Write a function called get_reverse_stack which takes a stack and returns a stack, 
# which has all the same elements from the argument, but reversed.
# loop through stack pop and append to new list
# test case [1,2,3,4] => [4,3,2,1]

"""Write a method on a Stack class (assuming you have other typical Stack methods 
and attributes) called get_max which determines and returns the maximum value in a Stack. 
You can assume the Stack elements are integers.
"""
# keep track of max so far
class Stack(object):
    def __init__(self):
        self.data = []
        self.max = None

    def pop(self):
        return self.data.pop()

    def add(self, data):
        self.data.append(data)
        if self.max is None or data > self.max:
            self.max = data
        

    def peek(self):
        return self.data[-1]

    def get_max(self):
        return self.max

    def get_max_alt(self):
        # loop through the stack
        if self.data:
            max_num = self.data[0]
        else:
            max_num = None

        for num in self.data:
            if num > max_num:
                max_num = num

        return max_num


# queues (first in first out) - more easily implemented with a linked list (add to end and pop from beginning)













