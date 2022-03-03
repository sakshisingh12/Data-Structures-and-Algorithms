"""
Problem URL - https://www.codechef.com/problems/MAGICMOD
"""
import math
test = int(input())

def check(array:list, n:int, x:int):
    h = {}
    for i in range(n):
        h[i+1] = 0

    for i in range(n):
        rem = array[i]%x
        if rem in h:
            h[rem] += 1
            
    for key, val in h.items():
        if val != 1:
            return "NO"
            
    return "YES"
    

def checkone(array:list, n:int):
    v = set()
    for i in range(n):
        if array[i] in v:
            return "NO"
        
        v.add(array[i])
    
    for i in range(n):
        if (i+1) not in v:
            return "NO"
    
    return "YES"
    
    
for _ in range(test):
    n = int(input())
    array = list(map(int, input().split()))
    s = sum(array)
    flag = False
    sr = (n*(n+1))//2
    q = s - sr
    x = int(math.sqrt(q))
    
    one = checkone(array, n)
    if one == "YES":
        print("YES", n+1)
    
    else:
        for i in range(1, x+1):
            if q%i == 0:
                ans = check(array, n, i)
                if ans == "YES":
                    print("YES", i)
                    flag = True
                    break
                
                ans = check(array, n, q//i)
                if ans == "YES":
                    print("YES", q//i)
                    flag = True
                    break
    
        if flag is False:
            print("NO")
    
