mayor=lambda numero1,numero2 : 1 if (numero1 > numero2) else -1
imprimir = lambda valor: "El numero mayor es el primer numero" if (valor==1) else "El numero mayor es el segundo numero"


valor=(mayor(6,8))
print (imprimir (valor))