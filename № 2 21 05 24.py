y = float ( input ('Введите курс доллар в рублях : '))
 
p = []
for i in range (1, 21):
    p.append(i * y)
 
k = 0
for j in range (0, 4):
    print (str(p[j+k:j+k+5]) + '\t')
    k+=4