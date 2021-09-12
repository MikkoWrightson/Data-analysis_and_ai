from random import randint

a = randint(0, 10)
b = randint(0, 10)

def summa(int1, int2):
    c = (a+b)
    print (f'Lukujen {a} ja {b} summa on: {c}')

summa(a, b)