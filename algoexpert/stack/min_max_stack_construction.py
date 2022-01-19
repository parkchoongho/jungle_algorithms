# Feel free to add new properties and methods to the class.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None


class MinMaxStack:
    def __init__(self):
        self.top: Node = None
        self.array = []

    def peek(self):
        return self.top.value

    def pop(self):
        if self.top is None:
            pass
        else:
            node = self.top
            self.top = self.top.prev
            node.prev = None
            self.array.remove(node.value)
            return node.value

    def push(self, number):
        node = Node(number)
        node.prev = self.top
        self.top = node
        self.array.append(number)
        self.array.sort()

    def get_min(self):
        # Write your code here.
        if len(self.array) > 0:
            return self.array[0]

    def get_max(self):
        # Write your code here.
        if len(self.array) > 0:
            return self.array[len(self.array) - 1]
