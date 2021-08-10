post = [0] * 4
flag_a = [False] * 4
flag_b = [False] * 7
flag_c = [False] * 7

def put():
    for i in range(4):
        print(f"{post[i]:2}", end='')
    print()

def set(i):
    for j in range(4):
        if(not flag_a[j] 
            and not flag_b[i + j] 
            and not flag_c[i - j + 3]):
            post[i] = j
            if i == 3:
                put()
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 3] = True
                set(i + 1)
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 3] = False

set(0)