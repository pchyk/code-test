#1트
'''T = int(input())
a = []
for _ in range(T):
    R, S = input().split()
    for i in range(len(S)):
        a.append(S[i]*int(R))
    print(*a)'''

#2트 clear로 초기화
'''T = int(input())
a = []
for _ in range(T):
    R, S = input().split()
    for i in S:
        for j in range(int(R)):   
            a.append(i)
    print(''.join(a))
    a.clear()'''

#3트 a=[]로 초기화
T = int(input())
for _ in range(T):
    a = []
    R, S = input().split()
    for i in S:
        for j in range(int(R)):   
            a.append(i)
    print(''.join(a))
