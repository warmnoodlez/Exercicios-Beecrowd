# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

numeros = []
for n in range(1, 101):
    numero = int(input())
    numeros.append(numero)

maior = max(numeros)
print(maior)
print(numeros.index(maior)+1)