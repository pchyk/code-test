#나중에 다시 풀어보기


'''abc = 'qwertyuiopasdfghjklzxcvbnm'
ABC = abc.upper()
a = {x: (abc[x], ABC[x]) for x in range(len(abc))}
al = input()
b = []
for i in al:
    for key, value in a.items():
        if i in value:
            b.append(key)
from collections import Counter
counter = Counter(b)
most_common = counter.most_common(1)
'''

'''from collections import Counter
word = input().strip().upper()
counter = Counter(word)
most_common = counter.most_common()
max_freq = most_common[0][1]
most_frequent = [char for char, freq in most_common if freq == max_freq]
if len(most_frequent) > 1:
    print('?')
else:
    print(most_frequent[0])'''

'''a = input().strip()
a.upper()
b = []
visit = []
for i in a:
    if i not in visit:
        b.append(a.count(i))
        visit.append(i)
M = max(b)
for i, j in a:
    if a.count(i) == M:
        if a.count(j) == M:
            print('?')
        else:
            print(i)'''

'''c = input().strip()
a = [x.upper() for x in c]
b = []
visit = []
for i in a:
    if i not in visit:
        b.append(a.count(i))
        visit.append(i)
M = max(b)
for i, j in a:
    if a.count(i) == M:
        if a.count(j) == M:
            print('?')
        else:
            print(i)'''

'''
word = input().strip().upper()
alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

counts = {i : word.count(i) for i in alphabet}
Max = max(counts.values())
for i, j in counts.keys():
    if i == j == Max:
        print('?')
        break
    elif i == Max:
        print(counts[i])''' # 딕셔너리의 KEY의 경우 FOR문으로 i, j 등 두개 이상의 변수를 반복할 수 없다.

답 1
'''word = input().strip().upper()
ALPHABET = [chr(x) for x in range(ord('A'), ord('Z') +1)]

counts = {i : word.count(i) for i in ALPHABET}
Max = max(counts.values())
Max_char = [char for char, count in counts.items() if count == Max]

if len(Max_char) > 1:
    print('?')
else:
    print(Max_char[0])'''

답2
word = input().strip().upper()
l = [word.count(chr(i)) for i in range(ord('A'), ord('Z') +1)]
print('?') if l.count(max(l)) > 1 else print(chr(l.index(max(l))+ord('A')))




