import random

oikein = 0
for i in range (0,5):
    a = random.randint(0,10)
    b = random.randint(0,10)
    
    print (f'{a} x {b} = ')
    vastaus = int(input())
    if vastaus == a * b:
        oikein += 1
        
print (f'Sait {oikein} oikein :-)')