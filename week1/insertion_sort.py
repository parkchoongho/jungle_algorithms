count = int(input())

num_list = []

for _ in range(count):
    num = int(input())
    num_list.append(num)

def insertion_sort():
    for i in range(1, len(num_list)):
        j = i
        while j > 0 and num_list[j] < num_list[j - 1]:
            num_list[j - 1], num_list[j] = num_list[j], num_list[j - 1]
            j -= 1

insertion_sort()

for num in num_list:
    print(num)