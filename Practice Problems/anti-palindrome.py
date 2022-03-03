"""
Problem URL - https://www.codechef.com/START24C/problems/ANTI_PAL
"""

from collections import Counter
test = int(input())

def sort(s:str, n:int):
    h = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e':0, 'f':0,
    'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k':0, 'l':0,
    'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q':0, 'r':0,
    's': 0, 't': 0, 'u': 0, 'v': 0, 'w':0, 'x':0,
    'y': 0, 'z': 0 }
    
    for char in s:
        h[char] += 1
    
    sh = ""
    for key, val in h.items():
        if val > n/2:
            return False
        x = key*val
        sh += x
    
    return sh
    
def anti_palindrome(s:str, n:int):
    if n%2 == 1:
        return "NO"
    string = sort(s, n)
    if string is False:
        return "NO"
    
    ans = ""
    for i in range(n//2 - 1, -1, -1):
        ans += string[i]
    
    for i in range(n//2, n):
        ans += string[i]
    
    return ["YES", ans]

        
for _ in range(test):
    n = int(input())
    s = input()
    ans = anti_palindrome(s, n)
    if ans == "NO":
        print("NO")
    
    else:
        print(ans[0])
        print(ans[1])
