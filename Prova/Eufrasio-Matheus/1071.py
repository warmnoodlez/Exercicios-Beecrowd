# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

x=int(input(""))
y=int(input(""))

maior = max(x,y)
menor = min(x,y)
soma=0
for n in range(menor+1, maior):
    if n%2!=0:
        soma += n
print(soma)