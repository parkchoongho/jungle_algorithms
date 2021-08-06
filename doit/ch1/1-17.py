area = int(input())

for i in range(1, area):
    if i * i > area: break
    if area % i == 0:
        print(f"{i} X {area // i}")