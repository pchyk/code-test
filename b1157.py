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
