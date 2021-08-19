from abc import abstractmethod
import sys

vertex_num, edge_num, start_vertex = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(vertex_num + 1)]

for _ in range(edge_num):
    src, dest = map(int, sys.stdin.readline().split())
    graph[src].append(dest)
    graph[dest].append(src)

for i in range(vertex_num + 1):
    if i != 0:
        graph[i].sort()

visited = [False] * (vertex_num + 1)


def dfs(graph, vertex):
    visited[vertex] = True
    print(vertex, end=' ')

    for i in graph[vertex]:
        if not visited[i]:
            dfs(graph, i)


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


visited2 = [False] * (vertex_num + 1)

queue = Queue()


def bfs(graph, vertex):
    visited2[vertex] = True
    print(vertex, end=' ')

    queue.enqueue(Node(vertex))

    while queue.size > 0:
        node = queue.dequeue()
        for i in graph[node.val]:
            if not visited2[i]:
                visited2[i] = True
                print(i, end=' ')
                queue.enqueue(Node(i))


dfs(graph, start_vertex)
print()
bfs(graph, start_vertex)
print()
