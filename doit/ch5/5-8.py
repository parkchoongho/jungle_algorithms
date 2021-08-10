pos = [0] * 4
flag = [False] * 4

def put():
    for i in range(4):
        print(f'{pos[i]:2}', end='')
    print()

def set(i):
    for j in range(4):
        if not flag[j]: # j행에 퀸을 배치하지 않았으면
            pos[i] = j  # 퀸을 j행에 배치
            if i == 3:  # 모든 열에 퀸 배치를 완료
                put()
            else:
                flag[j] = True
                set(i + 1)
                flag[j] = False

set(0)