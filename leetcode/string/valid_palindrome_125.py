import sys


class Solution(object):
    def isPalindrome(self, s: str):
        new_str = ''
        for ch in s:
            asc = ord(ch)
            if 48 <= asc <= 57:
                new_str += ch
            elif 65 <= asc <= 90:
                new_str += ch.lower()
            elif 97 <= asc <= 122:
                new_str += ch
            else:
                continue

        for i in range(len(new_str) // 2):
            if new_str[i] != new_str[-(i + 1)]:
                return False
        return True


solution = Solution()

s = sys.stdin.readline()
print(solution.isPalindrome(s))
