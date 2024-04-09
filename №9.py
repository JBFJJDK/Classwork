number = int(input("Введите число: "))

if ((number > 999 and number < 10000) and ((number % 7 == 0) or (number % 17 == 0))):
    print("YES")
else:
    print("NO")
