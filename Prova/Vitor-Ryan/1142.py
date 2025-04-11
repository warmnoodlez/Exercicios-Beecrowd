# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

contador = int(input())
numero = 1

for l in range(1 , contador+1):
    for c in range(numero, numero+4):
        if (c%4 == 0):
            print(f"PUM")
            numero = numero+4
        else:
            print(c, end=" ")