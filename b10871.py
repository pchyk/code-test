#1트
N, X = map(int, input().split())
A = list(map(int, input().split()))
B = []
for i in A:
    if i < X:
        B.append(i)
B = ' '.join(B)
print(B)

#2트
N, X = map(int, input().split())
A = list(map(int, input().split()))
B = []
for i in A:
    if i < X:
        B.append(i)
B = ' '.join(map(str,B))
print(B)'''
#join, split 매서드는 문자열 <-> 리스트 간 상효작용이므로 숫자를 문자로 만들어 줘야함
