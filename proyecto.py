import json 
import os 
import time
Contra = ("d102")
Usua = ("Steven")

    

print("=================================")
print("BIENVENIDO CAMPER A CAMPUS LANDS")
print("=================================")
time.sleep(1.5)
os.system("cls")

print("Que Desea Hacer")
time.sleep (1.0)

print("|===================================|")
print("|       WELCOME A CAMPUSLANDS       |")
print("|===================================|")
print("| -> (1) Estudiantes                |")
print("| -> (2) Trainer                    |")
print("| -> (3) Coordinador                |")
print("| -> (0) Salir                      |")
print("|===================================|")
print("|_______Seleccione una opcion_______|")
print("|===================================|")
print(" ")
opc=input("")
os.system("cls")


if opc == "1":
    print("Hola Estimado Estudiante")
    print("Que deseas hacer")
    print("")
    print("|==========================|")
    print("|                          |")
    print("| -> (1) Iniciar Sesion    |")
    print("| -> (2) Registrarme       |")
    print("|                          |")
    print("|==========================|")
    input ("")

if opc == "0":
    print("Gracias por hacer parte de Campus Lands")
    time.sleep(2.0)
    os.system("cls")

if opc == "3":

  ingreso_exitoso = False
  while not ingreso_exitoso:
    print("========================================")
    print("/////Ingrese Los Datos Solicitados/////")  
    print("========================================")
    print(" ")
    print("Ingrese Su Usuario")
    Usu=input()
    print("Ingrese Su Contraseña")
    Con=input()
    
    if Usu != Usua or Con != Contra:
      print("Usuario o Contraseña incorrectos")
      print("Presione (N) para intentarlo de nuevo ")
      rta = input()
      if rta != "N":
        break 
      os.system("cls")
    
    else:
      os.system("cls")
      ingreso_exitoso = True 
      print("Hola Coodinador", Usua , "Un gusto verlo de nuevo...")
        
      time.sleep(1.5)
      print("         Que Desea Hacer Hoy          ")
      print(" ")
      print("|------------BASE DE DATOS-----------|")
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
      print("|------------------------------------|")
      print("|------------------------------------|")
      print("")
      ads=input()
      if ads == "1":
             Camper_json = "n/Lista.json"
             with open(Camper_json, encoding= "utf-8")as file:
                datos_json = json.load(file)
                print(datos_json)



 

