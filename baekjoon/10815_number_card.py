import sys

have_cards_cnt = int(sys.stdin.readline().rstrip())

have_cards_list = list(map(int, sys.stdin.readline().split()))

check_cards_cnt = int(sys.stdin.readline().rstrip())

check_cards_list = list(map(int, sys.stdin.readline().split()))

have_cards_list.sort()


def binary_search(have_cards_list, check_card):
    list_length = len(have_cards_list)
    start = 0
    end = list_length - 1

    while start <= end:
        middle = (start + end) // 2
        if have_cards_list[middle] > check_card:
            end = middle - 1
        elif have_cards_list[middle] < check_card:
            start = middle + 1
        else:
            return 1
    return 0


for card in check_cards_list:
    print(binary_search(have_cards_list, card), end=' ')

print()
