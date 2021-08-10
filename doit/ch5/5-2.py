input_list = input().split()

num1 = int(input_list[0])
num2 = int(input_list[1])

def gcd(a, b):
    if a > b:
        if a % b == 0:
            return b
        else:
            return gcd(a % b, b)
    else:
        if b % a == 0:
            return a
        else:
            return gcd(a, b % a)

print(gcd(num1, num2))
