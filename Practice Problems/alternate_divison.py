test = int(input())
for _ in range(test):
    n = int(input())
    num = {i for i in range(1, n+1)}
    array, index = [], 0

    while index < n:
        temp = num.pop()
        temp2 = temp*2

        if temp2 in num:
            num.remove(temp2)
        
        if index == n-1 and n%2 == 1:
            array.append(temp)
            index += 1
        else:
            array.append(temp)
            array.append(temp2)
            index += 2
    
    print(*array)
        

