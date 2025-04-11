# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

preco = [4.0,4.5,5.0,2.0,1.5]

pedido = input().split()
codigo = int(pedido[0])-1
quantidade = int(pedido[1])

conta = preco[codigo]*quantidade

print(f"Total: R$ {conta:.2f}")