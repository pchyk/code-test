#1트 실패
'''import sys
s = sys.stdin.readline().strip()
a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
c = [x for x in s]
d = {}
n = 0
for i in range(len(c)-1):
    ij = c[i] + c[i+1] 
    if ij in a:
        n += 1
print(len(c)-n)'''

#2트 정답
cro = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
a = input()
for i in cro:
    a = a.replace(i, '@')
print(len(a))
