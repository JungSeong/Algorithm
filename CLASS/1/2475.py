import sys
input = sys.stdin.readline

nums = list(map(int, input().split()))
print(sum(map(lambda x : x**2, nums))%10)