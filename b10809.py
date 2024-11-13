#1트 실패
'''import string
abc = string.ascii_lowercase
a = [-1]*26
l = input()
for i in abc:
    if i in l:
        a[abc.index(i)] = abc.index(i)
print(a)'''

#2트 gpt
'''import string
abc = list(string.ascii_lowercase)
S = list(input())
result = []
for i in abc:
    if i in S:
        result.append(S.index(i))
    else:
        result.append(-1)
print(*result)'''

#3트 아스키 코드
'''s = input()
for i in range(97,123):
    print(s.find(chr(i)), end=' ')'''

#4트 그냥
S = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in alphabet:
    x = S.find(i)
    print(x, end=' ')
