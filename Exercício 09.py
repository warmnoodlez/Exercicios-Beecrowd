# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

num = int(input())
horas_trab = int(input())
ganho_por_h = round(float(input()), 2)

salario = ganho_por_h * horas_trab

print(f"NUMBER = {num}")
print("SALARY = U$ %.2f" % salario)
