while True:
    n = int(input())
    for i in range(1,n):
        if i ** 2 > n:break
    print(i)