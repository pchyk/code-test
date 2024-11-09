#1트
from sys import stdin
N, M = map(int, stdin.readline().split())
a = [0] * N
for _ in range(M):
    i, j, k = map(int, stdin.readline().split())
    a[i-1:j] = [k] * (j-i+1)
print(*a) # *로 언패킹

#2트
N, M = map(int, input().split())
a = [0] * N
for i in range(M):
  i,j,k = map(int, input().split())
  for x in range(i-1,j):  #for문을 하나 더 쓰기
    a[x] = k
print(*a)

#3트
N, M = map(int, input().split())
a = [0] * N
for _ in range(M):
    i, j, k = map(int, input().split())
    a[i-1:j] = [k] * (j-i+1)  
for x in a:           
    print(a, end=" ")     #언패킹을 for문으로
