from abc import abstractmethod
import sys


class Node:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
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


R, C = map(int, sys.stdin.readline().split())


game_map = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


value_queue = Queue()
for i in range(len(game_map)):
    for j in range(len(game_map[i])):
        if game_map[i][j] == '*':
            value_queue.enqueue(Node(i, j, '*'))
        elif game_map[i][j] == 'S':
            hedgehog_node = Node(i, j, 0)
value_queue.enqueue(hedgehog_node)


def bfs(value_queue: Queue):
    while value_queue.size > 0:
        node = value_queue.dequeue()
        for i in range(4):
            nx = node.x + dx[i]
            ny = node.y + dy[i]
            if node.z == '*' and 0 <= nx < R and 0 <= ny < C:
                if game_map[nx][ny] == '.' or game_map[nx][ny] == 'S':
                    game_map[nx][ny] = '*'
                    value_queue.enqueue(Node(nx, ny, '*'))
            elif type(node.z) is int and 0 <= nx < R and 0 <= ny < C:
                if game_map[nx][ny] == '.':
                    game_map[nx][ny] = 'S'
                    value_queue.enqueue(Node(nx, ny, node.z + 1))
                elif game_map[nx][ny] == 'D':
                    return node.z + 1
    return "KAKTUS"


print(bfs(value_queue))
