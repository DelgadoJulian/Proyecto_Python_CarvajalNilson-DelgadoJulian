import json 
import os 
import time
Contra = ["d102"]
Usua = ["Steven"]
Cordinador = {"usuario1": "contraseña1", "usuario2": "contraseña2",}
def inicio_secion():

 while 
   username = input("Nombre de usuario; ")
   password = input("contraseña: ")
if username in Cordinador and Cordinador[username]==password:
      print("que bien contraseña correcta, {}!".format(username))
      return
else:
      print("usuario o contraseña incorrecto")
    

print("=================================")
print("BIENVENIDO CAMPER A CAMPUS LANDS")
print("=================================")
time.sleep(2.0)
os.system("cls")

print("Que Desea Hacer")
time.sleep (1.0)

print("|===================================|")
print("|              Welcome              |")
print("|                                   |")
print("|    (1) Estudiantes                |")
print("|    (2) Trainer                    |")
print("|    (3) Coordinador                |")
print("|    (0) Salir                      |")
print("|                                   |")
print("|===================================|")
print(" ")
print("Seleccione una opcion")
opc=input("")
os.system("cls")


if opc == "1":
    print("Hola Estimado Estudiante")
    print("Que deseas hacer")
    print("")
    print("|==========================|")
    print("|                          |")
    print("|(1) Iniciar Sesion        |")
    print("|(2) Registrarme           |")
    print("|                          |")
    print("|==========================|")
    input ("")

if opc == "0":
    print("Gracias por hacer parte de Campus Lands")
    time.sleep(2.0)
    os.system("cls")

if opc == "3":
    
  print("Ingresar Usuario")
  Usu=str(input())
  print("Ingrese Contraseña")
  Con=input()
  if Usu != Usua:
      print("Usuario incorrecto")
  elif Contra != Con:
    print ("Contraseña Incorrecta") 
  
  


  
  time.sleep(2.0)
  print("  Hola Cordinador que desea hacer hoy ")
  print("|***********BASE DE DATOS************|")
  print("|------------------------------------|")
  print("| 1.Notas de los campers             |")
  print("|------------------------------------|") 
  print("| 2.Lista de los campers             |")
  print("|------------------------------------|")
  print("| 3.Lista de los trainers            |")
  print("|------------------------------------|")
  print("| 4.Asignación de rutas a trainers   |")
  print("|------------------------------------|")
  print("| 5.Rutas de entrenamiento           |")
  print("|                                    |")
  print("|************************************|")
  print("")

    
Camper_json = "n/Lista.json"

with open(Camper_json, encoding= "utf-8")as file:
    datos_json = json.load(file)

    print(datos_json)