a = int(input("Введите число A: ")) 
b = int(input("Введите число B: ")) 
 
if a < b: 
    result = ' '.join(str(i) for i in range(a, b+1)) 
else: 
    result = ' '.join(str(i) for i in range(a, b-1, -1)) 
 
print("Числа от A до B:", result)