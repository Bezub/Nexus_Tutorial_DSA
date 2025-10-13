if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr2 = []
    
    for i in arr:
        if i not in arr2:
            arr2.append(i)         
    arr2.sort()
print(arr2[-2]) 
