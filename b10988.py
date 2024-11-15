'''a = list(input().strip())
b = a[::-1]
if a == b :
    print(1)
else:
    print(0)'''

import sys

Palindrome = sys.stdin.readline().strip()
left, right = 0, len(Palindrome) - 1
while left < right:
    if Palindrome[left] != Palindrome[right]:
        print(0)
        break
    left += 1
    right -= 1
else:
    print(1)
