from abc import abstractmethod
import sys


class PriorityQueueInterface:
    @abstractmethod
    def insert(self, value: int) -> None:
        pass

    @abstractmethod
    def delete(self) -> int or None:
        pass

    @abstractmethod
    def heapify(self) -> None:
        pass

    @abstractmethod
    def peek(self) -> int or None:
        pass


class MinPriorityQueue(PriorityQueueInterface):
    def __init__(self):
        self.data_list = []

    def insert(self, value: int) -> None:
        self.data_list.append(value)
        position = len(self.data_list) - 1
        while position > 0:
            parent = (position - 1) // 2
            if self.data_list[position] < self.data_list[parent]:
                self.data_list[position], self.data_list[parent] = self.data_list[parent], self.data_list[position]
            else:
                break
            position = parent

    def delete(self) -> int or None:
        if len(self.data_list) == 0:
            return
        if len(self.data_list) == 1:
            return self.data_list.pop()
        self.data_list[0], self.data_list[-1] = self.data_list[-1], self.data_list[0]
        value = self.data_list.pop()
        self.heapify()
        return value

    def heapify(self) -> None:
        min = self.data_list[0]

        parent = 0

        while parent < len(self.data_list) // 2:
            left_child = 2 * parent + 1
            right_child = left_child + 1
            child = right_child if right_child <= len(self.data_list) - 1 and self.data_list[right_child] < self.data_list[left_child] else left_child
            if min < self.data_list[child]:
                break
            self.data_list[parent] = self.data_list[child]
            parent = child
        self.data_list[parent] = min

    def peek(self) -> int:
        if len(self.data_list) == 0:
            return
        return self.data_list[0]


test_num = int(sys.stdin.readline())

min_priority_queue = MinPriorityQueue()

for i in range(test_num):
    val = int(sys.stdin.readline())
    min_priority_queue.insert(val)


sum = 0

while len(min_priority_queue.data_list) != 1:
    min_num = min_priority_queue.delete()
    min_num2 = min_priority_queue.delete()
    sum += min_num + min_num2
    min_priority_queue.insert(min_num + min_num2)


print(sum)
