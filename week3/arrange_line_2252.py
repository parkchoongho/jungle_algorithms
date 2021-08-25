from abc import abstractmethod
import sys


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self):
        result = "{ "
        result += str(self.val)
        result += " }"
        return result


class QueueInterface:
    @abstractmethod
    def enqueue(self, node: Node) -> None:
        pass

    @abstractmethod
    def dequeue(self) -> Node:
        pass

    @abstractmethod
    def search(self, index) -> Node:
        pass

    @abstractmethod
    def __str__(self):
        pass


class NoSuchElementException(Exception):
    pass


class WrongIndex(Exception):
    pass


class Queue(QueueInterface):
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, node: Node) -> None:
        if self.size == 0:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            node.prev = self.last
            self.last = node
        self.size += 1
        return

    def dequeue(self) -> Node:
        if self.size == 0:
            raise NoSuchElementException()
        if self.size == 1:
            node = self.first
            self.first = None
            self.last = None
        else:
            node = self.first
            self.first = self.first.next
            self.first.prev = None
            node.next = None
        self.size -= 1
        return node

    def search(self, index) -> Node:
        if index < 0 or index > self.size - 1:
            raise WrongIndex()
        start_index = 0
        node = self.first
        while start_index != index:
            start_index += 1
            node = node.next
        return node

    def peek(self) -> Node:
        if self.size == 0:
            raise NoSuchElementException()
        return self.first

    def __str__(self):
        node = self.first
        result = "None "
        while node is not None:
            result += "<- "
            result += str(node.val)
            result += " -> "
            node = node.next
        result += "None"
        return result


stu_num, comparison_num = map(int, sys.stdin.readline().split())

indegree = [0] * (stu_num + 1)

graph = [[] for _ in range(stu_num + 1)]

for _ in range(comparison_num):
    source, dest = map(int, sys.stdin.readline().split())
    graph[source].append(dest)
    indegree[dest] += 1


def topological():
    result_list = []

    arrange_queue = Queue()

    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            arrange_queue.enqueue(Node(i))

    while arrange_queue.size > 0:
        node = arrange_queue.dequeue()
        result_list.append(node.val)
        for dest in graph[node.val]:
            indegree[dest] -= 1
            if indegree[dest] == 0:
                arrange_queue.enqueue(Node(dest))

    for i in result_list:
        print(i, end=' ')


topological()

print()
