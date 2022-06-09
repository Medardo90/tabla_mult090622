# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 07:50:54 2022

@author: Alumno Patricio Haro
"""
suma=0
promedio=0
for j in range (1,16):
    print("La Tabla de N°:",j)
    print("\n")
    par=0
    impar=0
    for i in range (1,16):
        res=i*j
        suma+=res
        promedio=suma //15
        print(i,"x",j,"=",res)
        if res%2==0:
            par=par+1
        else:
            impar=impar+1
        
    print("La 'SUMA' de los números es:",suma)
    print("El 'PROMEDIO' de los números es:",promedio)
    print("Hay",par,"números pares.")
    print("Hay",impar,"números impares.")
    print("\n"*2)
 