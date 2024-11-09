#1트
N = int(input())
nums = list(map(int,input().split()))
print(min(nums), max(nums))

#2트
from sys import stdin
_, *a = map(int, stdin.buffer.read().split())
print(min(a), max(a))
#stdin.buffer.read()는 입력은 byte로 한 번에 받음
