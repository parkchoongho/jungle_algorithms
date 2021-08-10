import sys


def heapify(arr, length, heap_index):
    largest_index = heap_index
    left_child_index = 2 * heap_index + 1
    right_child_index = 2 * heap_index + 2

    if left_child_index < length and arr[largest_index] < arr[left_child_index]:
        largest_index = left_child_index

    if right_child_index < length and arr[largest_index] < arr[right_child_index]:
        largest_index = right_child_index

    if largest_index != heap_index:
        arr[largest_index], arr[heap_index] = arr[heap_index], arr[largest_index]

        heapify(arr, length, largest_index)


def heapSort(arr):
    length = len(arr)

    for i in range(length // 2 - 1, -1, -1):
        heapify(arr, length, i)

    for i in range(length - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


test_num = int(sys.stdin.readline().rstrip())

input_list = [None] * test_num

for i in range(test_num):
    input_list[i] = int(sys.stdin.readline().rstrip())

heapSort(input_list)

for i in input_list:
    print(i)

# 동료 풀이


# N = int(sys.stdin.readline())
# numbers = []

# for x in range(N):
#     tmp = int(sys.stdin.readline())
#     numbers.append(tmp)


# def heapify():
#     for i in range(1, N):
#         c = i
#         while c > 0:
#             root = (c - 1) // 2
#             if numbers[c] > numbers[root]:
#                 numbers[c], numbers[root] = numbers[root], numbers[c]
#             c = root
#     return


# def heap_sort():
#     for i in range(N - 1, -1, -1):
#         numbers[0], numbers[i] = numbers[i], numbers[0]

#         root, c = 0, 1
#         while c < i:
#             c = root * 2 + 1
#             if c < i - 1 and numbers[c] < numbers[c + 1]:
#                 c += 1

#             if c < i and numbers[c] > numbers[root]:
#                 numbers[c], numbers[root] = numbers[root], numbers[c]
#             root = c
#     return


# heapify()
# heap_sort()

# for i in numbers:
#     print(i)
