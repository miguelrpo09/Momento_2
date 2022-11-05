import os
os.system ("cls")

def crearMenu():
    print("***************BANCO DE HIERRO ISLA DE BRAAVOS***************")
    print("(1) Ver Información de la cuenta")
    print("(2) Ingresar saldo a la cuenta")
    print("(3) Retirar saldo de la cuenta")
    print("(4) Limpiar pantalla")
    print("(5) Actualizar datos del cliente")
    print("(0) Terminar")


class Usuario:
  #constructor
  #dentro del constructor son los atributos
  def __init__(self,nombredado,apellidodado,ceduladada,ciudaddada):
    self.nombre=nombredado,
    self.apellido=apellidodado,
    self.cedula=ceduladada,
    self.ciudad=ciudaddada
  #metodos
  def salular(self):
    print(f'hola yo soy {self.nombre}')

class Cuenta:
  #constructor
  #dentro del constructor son los atributos
  def __init__(self,cuentadada,saldodado):
    self.cuenta=cuentadada,
    self.saldo=saldodado,

  #metodos
  def retirar(self):
    print(f'hola yo soy {self.nombre}')

#para usar una clase instanciamos en el objeto batman
cliente=Usuario("Miguel","Restrepo","71294243","Itagui")
cuenta=Cuenta("1","0")

i=1
crearMenu()
while(i!=0):
    #diccionario ciclista
    ciclista={

    }
    i=int(input("Digita una opcion: "))
    if(i==1):
        print("Consultar saldo de la cuenta")
        print("")
        print(f"el señor {cliente.nombre} identificado con documento: {cliente.cedula} tiene en su cuenta: {cuenta.saldo}: ")      
        print("")
        crearMenu()
    elif(i==2):
        print("Ingresar saldo a la cuenta")
        cuenta.saldo=int(input(f"Digita el saldo a ingresar a la cuenta: {cuenta.cuenta}"))
        os.system ("cls")
        crearMenu()               
    elif(i==3):
        print("Retirar saldo de la cuenta")
        print("")
        cuenta.saldo = cuenta.saldo - int(input(f"Digita el saldo a retirar de la cuenta: {cuenta.cuenta}: "))
        os.system ("cls")
        crearMenu();        
    elif(i==4):
        os.system ("cls")        
        crearMenu()
    elif(i==5):
        cliente.nombre=input(f"Actualiza tu nombre: ")
        cliente.apellido=input(f"Actualiza tu apellido: ")
        cliente.cedula=input(f"Actualiza tu cédula: ")
        cliente.ciudad=input(f"Actualiza tu ciudad: ")
        os.system ("cls")        
        crearMenu()   
    elif(i==0):
        break
    else:
        print("Digite una opcion valida.")
else:
    print("Digite una opcion valida.")