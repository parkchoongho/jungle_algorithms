import sys
from abc import abstractmethod

row, column, height = map(int, sys.stdin.readline().split())

tomato_box = [[] for _ in range(height)]

for i in range(height):
    for j in range(column):
        tomato_box[i].append(list(map(int, sys.stdin.readline().rstrip().split())))


class Node:
    def __init__(self, x, y, z, days):
        self.x = x
        self.y = y
        self.z = z
        self.days = days
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


def check(height, column, row):
    for i in range(height):
        for j in range(column):
            if tomato_box[i][j].count(0) > 0:
                return True
    return False


queue = Queue()

for i in range(height):
    for j in range(column):
        for k in range(row):
            if tomato_box[i][j][k] == 1:
                queue.enqueue(Node(i, j, k, 0))

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while queue.size > 0:
    node = queue.dequeue()
    x = node.x
    y = node.y
    z = node.z
    days = node.days

    for i in range(6):
        nx = node.x + dx[i]
        ny = node.y + dy[i]
        nz = node.z + dz[i]
        ndays = days + 1

        if 0 <= nx < height and 0 <= ny < column and 0 <= nz < row:
            if tomato_box[nx][ny][nz] == 0:
                tomato_box[nx][ny][nz] = 1
                queue.enqueue(Node(nx, ny, nz, ndays))

if check(height, column, row):
    days = -1

print(days)
