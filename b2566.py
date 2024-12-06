#1트
'''import sys
s = sys.stdin.readline
Max = []
Max_Max = None
I = 0
J = 0
for i in range(9):
    x = list(map(int, s().split()))
    Max.append(max(x))
    Max_Max = max(Max)
    if max(x) == Max_Max:
        I = i       
    J = x.index(max(x)) + 1

print(Max_Max)
print(I, J)'''

#2트
import sys
s = sys.stdin.readline

Max = -float('inf')
I = 0
J = 0

for i in range(9):
    row = list(map(int, s().split()))
    row_max = max(row)
    if row_max > Max:
        Max = row_max
        I = i + 1
        J = row.index(row_max) + 1

print(Max)
print(I, J)

#3
li = []
for i in range(9):
    li += list(map(int,input().split()))
n = max(li)
y,x = divmod(li.index(n),9)
print(n)
print(y + 1, x + 1)
