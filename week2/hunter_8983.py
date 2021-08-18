import sys

shooting_point_count, animal_count, shooting_range = map(int, sys.stdin.readline().split())

shooting_point = list(map(int, sys.stdin.readline().split()))

animal_point = []

for i in range(animal_count):
    val = sys.stdin.readline().split()
    if int(val[1]) > shooting_range:
        continue
    animal_point.append([int(val[0]), int(val[1])])

shooting_point.sort()
animal_point.sort(key=lambda x: x[0])


count = 0

for animal in animal_point:
    start = 0
    end = len(shooting_point) - 1
    while start <= end:
        mid = (start + end) // 2
        shoot_length = abs(shooting_point[mid] - animal[0]) + animal[1]
        if shoot_length <= shooting_range:
            count += 1
            break
        else:
            if animal[0] == shooting_point[mid]:
                break
            elif animal[0] < shooting_point[mid]:
                end = mid - 1
            else:
                start = mid + 1

print(count)
