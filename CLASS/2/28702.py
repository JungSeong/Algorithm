import sys

input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()
s3 = input().rstrip()

def print_num(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0 and num % 5 != 0:
        return "Fizz"
    elif num % 3 != 0 and num % 5 == 0:
        return "Buzz"
    else:
        return str(num)

idx = 1

while True:
    if print_num(idx) == s1 and print_num(idx + 1) == s2 and print_num(idx + 2) == s3:
        print(print_num(idx + 3))
        break
    idx += 1