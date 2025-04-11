# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

while True:
    try:
        n = int(input())
        senha = n - 1
        print(senha)
    except EOFError:
        break