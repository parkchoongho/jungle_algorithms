input_list = input().split()

climbing_distance = int(input_list[0])
slipping_distance = int(input_list[1])
all_distance = int(input_list[2])

num = (all_distance - climbing_distance) // (climbing_distance - slipping_distance)
left = (all_distance - climbing_distance) % (climbing_distance - slipping_distance)

if climbing_distance == all_distance:
    print(1)
elif (climbing_distance - slipping_distance) > (all_distance - climbing_distance):
    print(2)
elif left == 0:
    print(num + 1)
else:
    print(num + 2)
