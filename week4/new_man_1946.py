import sys

TestNum = int(sys.stdin.readline())

ans_list = []
for _ in range(TestNum):
    new_man_num = int(sys.stdin.readline())

    score_list = []

    for _ in range(new_man_num):
        docu, interview = map(int, sys.stdin.readline().split())
        score_list.append([docu, interview])

    score_list.sort(key=lambda score: score[0], reverse=True)

    ans_ele = 0
    one_list = [False] * len(score_list)
    min_False = 0
    for i in range(len(score_list)):
        one_list[score_list[i][1] - 1] = True
        if score_list[i][1] - 1 > min_False:
            ans_ele += 1
        while 0 <= min_False < len(score_list) and one_list[min_False] == True:
            min_False += 1

    ans_list.append(len(score_list) - ans_ele)

for ans in ans_list:
    print(ans)
