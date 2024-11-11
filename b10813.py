#1트 실패, replace는 문자열에서만
'''N,M = map(int,input().split())
bascket = []
for x in range(N):
    bascket.append(x+1)
for y in range(M):
    i,j = map(int,input().split())
    p = bascket[i-1]
    q = bascket[j-1]
    bascket.replace(p, q)
    bascket.replace(q, p)
print(*bascket)'''

#2트 성공, list에서 my_list[0] = a
'''N,M = map(int,input().split())
bascket = []
for x in range(N):
    bascket.append(x+1)
for y in range(M):
    i,j = map(int,input().split())
    p = bascket[i-1]
    q = bascket[j-1]
    bascket[j-1] = p
    bascket[i-1] = q
print(*bascket)'''


#3트, 0을 포함한 리스트 생성 i,j 에 -1할 필요가 없어짐 good
'''n, m = map(int, input().split())
arr = list(range(n+1))

for a in range (m):
    i, j = map(int, input().split())
    arr[i], arr[j] = arr[j], arr[i]

print(*arr[1:])'''

#4트, 위에랑 똑같음
n, m = map(int, input().split())
arr = list(range(1, n+1))

for a in range (m):
    i, j = map(int, input().split())
    arr[i-1], arr[j-1] = arr[j-1], arr[i-1]

print(*arr)


#5트, print를 예쁘게 썼다-또다른 언패킹 방식
'''
n,m=map(int, input().split())
a=list(range(1,n+1))
for i in range(m):
    i,j=map(int, input().split())
    a[i-1],a[j-1]=a[j-1],a[i-1]
for number in a:
    print(number, end=' ')'''
