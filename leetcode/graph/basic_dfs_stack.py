from abc import abstractmethod


class NoSuchElementException(Exception):
    pass


class WrongIndex(Exception):
    pass


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None

    def __str__(self):
        result = "{ "
        result += str(self.val)
        result += " }"
        return result


class StackInterface:
    @abstractmethod
    def push(self, node: Node) -> None:
        pass

    @abstractmethod
    def pop(self) -> Node:
        pass

    @abstractmethod
    def search(self, index) -> Node:
        pass

    @abstractmethod
    def peek(self) -> Node:
        pass

    @abstractmethod
    def __str__(self):
        pass


class Stack(StackInterface):
    def __init__(self):
        self.last = None
        self.size = 0

    def push(self, node: Node) -> None:
        if self.size == 0:
            self.last = node
        else:
            node.prev = self.last
            self.last = node
        self.size += 1
        return

    def pop(self) -> Node:
        if self.size == 0:
            raise NoSuchElementException()
        if self.size == 1:
            node = self.last
            self.last = None
        else:
            node = self.last
            self.last = self.last.prev
            node.prev = None
        self.size -= 1
        return node

    def search(self, index) -> Node:
        if index < 0 or index > self.size - 1:
            raise WrongIndex()
        start_index = 0
        node = self.last
        while start_index != index:
            start_index += 1
            node = node.prev
        return node

    def peek(self) -> Node:
        if self.size == 0:
            raise NoSuchElementException()
        return self.last

    def __str__(self):
        current_node = self.last
        result = "last\n"
        result += " |\n v\n"
        while current_node is not None:
            result += "["
            result += str(current_node.val)
            result += "]\n |\n v\n"
            current_node = current_node.prev
        result += "None"
        return result


graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


def dfs(v: int):
    visited = []

    stack = Stack()
    stack.push(Node(v))

    while stack.size > 0:
        vertex = stack.pop()
        visited.append(vertex.val)

        for dst in graph[vertex.val]:
            if dst not in visited:
                stack.push(Node(dst))

    return visited


print(dfs(1))
