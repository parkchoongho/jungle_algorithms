test_case_num = int(input())

score_list = []
for i in range(test_case_num):
    subsequent_o = 0
    score = 0
    ox_list = input()
    for ch in ox_list:
        if ch == "O":
            subsequent_o += 1
        else:
            subsequent_o = 0
        score += subsequent_o
    score_list.append(score)
for score in score_list:
    print(score)