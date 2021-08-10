pos = [0] * 4

print(pos)
def put():
    for i in range(4):
        print(f"{pos[i]:2}", end='')
    print()

def set(i):
    for j in range(4):
        pos[i] = j
        if i == 3:
            put()
        else:
            set(i + 1)

set(0)