#너무어렵다

'''n = int(input())  # 입력받은 n

# 위쪽 삼각형
for i in range(1, n + 1):  # 1부터 n까지 반복
    print(' ' * (n - i) + '*' * (2 * i - 1))

# 아래쪽 삼각형
for i in range(n - 1, 0, -1):  # n-1부터 1까지 반복
    print(' ' * (n - i) + '*' * (2 * i - 1))'''

n=int(input())
for i in range(1-n, n, 1):
    print(' '*abs(i)+'*'*abs(1-2*n+2*abs(i))
