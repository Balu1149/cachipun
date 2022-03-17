#Juego de cachipun paradigmas sec 1 profesora María Loreto Arriagada Verdugo
#Integrantes:
#Klaus Molt
#Javier Aguilera
#Camila Martinez
#Joaquin Leal
#Benjamin Lillo

#Se importan las librerias a usar
from json.tool import main
import random
from tkinter.tix import Tree
import sys
import time

#1.- Se definen los dibujos de los elementos "Piedra, papel y tijera" (Javier Aguilera)
def dibujos():
    piedra = """
                #####@###
           ####@##### #####   #
      #  ############## ##########
    #####@###### #@########@## #####
  ############## ######## ############
    ####@## ######## #####@##### ###
        #########@##############
            ## ###### # # #
                ##########
                """
    papel = """
             #########################
             ########################
             ######################
             #####################
             #####################
             #####################
             #####################
           #######################
          ########################
                """
    tijera = """
              #      #
             ###    ###
             ###    ### 
             ###    ###
             ###    ###
              ##    ##
                 ##   
            ####   ####
           #    # #    #
           #    # #    #
            ####   ####
                """
    return(piedra, papel, tijera)

#2.- Se define la desición del jugador y la elección aleatoria del enemigo. (Camila Martinez)
def decicion():
    while True:
        print('Por favor ingresa la eleccion que quieras hacer:\nPiedra(1), Papel(2), Tijera(3) o Salir(4)')
        eleccion = input('Tu eleccion: ')
        eleccion = eleccion.lower()
        lista_validos = ['piedra', '1', 'papel', '2', 'tijeras', 'tijera', '3', 'salir', '4']
        if eleccion in lista_validos:
            break
        else:
            print('Ingrese un valor valido.')
            continue
    
    dic = {'piedra': 1, '1': 1, 'papel': 2, '2': 2, 'tijeras': 3, 'tijera': 3, '3': 3, 'salir': 4, '4': 4}
    eleccion = dic[eleccion]
    eleccion_enemigo =random.randint(1,3)
    return eleccion, eleccion_enemigo

#3.- Se establecen las relaciones de victoria, derrota y empate. (Klaus Molt)
def relaciones(eleccion, e_enemigo):
    if (eleccion ==1 and e_enemigo ==1) or (eleccion ==2 and e_enemigo ==2) or (eleccion ==3 and e_enemigo ==3) :
        #3 es empate
        return 3
    if (eleccion ==1 and e_enemigo ==2) or (eleccion ==2 and e_enemigo ==3) or (eleccion ==3 and e_enemigo ==1):
        #0 es perder
        return 0
    if (eleccion ==1 and e_enemigo ==3) or (eleccion ==2 and e_enemigo ==1) or (eleccion ==3 and e_enemigo ==2):
        #1 es ganar
        return 1

#Contador de victorias y derrotas (Joaquin Leal)
def contador(resultado):
    global puntaje_e
    global puntaje_j
    
    if resultado == 1:
        puntaje_j+= 1
    elif resultado == 0:
        puntaje_e+= 1
    return

#Se establece el juego, la emisión de los dibujos y la impresión de resultados (Benjamin Lillo)
def display(d_jugador, d_enemigo, resultado):
    global nombre_jugador
    global puntaje_j
    global puntaje_e
    
    print('Sacaste:')
    for c in d_jugador + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)
    
    print('El enemigo saco:')
    for c in d_enemigo + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)
    
    dic = {3: 'empataste.', 0: 'perdiste.', 1: 'ganaste.'}
    resultado = dic[resultado]
    print('Por lo tanto', resultado)
    print('Puntaje de', nombre_jugador, puntaje_j,'\n' + 'Puntaje de cpu:', puntaje_e)
    
#Nombre de los jugadores y se llaman als funciones, además de dando la opción de finalizar el juego.
if __name__ == "__main__":
    global nombre_jugador
    global puntaje_j
    global puntaje_e

    puntaje_j = 0
    puntaje_e = 0

    print('Bienvenido a nuestro juego de cachipún, por favor ingresa tu nombre: ')

    nombre_jugador = input()
    piedra, papel, tijera = dibujos()
    dic = {1: piedra, 2: papel, 3: tijera}

    while True:
        eleccion, eleccion_enemigo = decicion()
        if eleccion == 4:
            print('Gracias por jugar!')
            sys.exit()

        resultado = relaciones(eleccion, eleccion_enemigo)
        contador(resultado)
        d_jugador = dic[eleccion]
        d_enemigo = dic[eleccion_enemigo]
        display(d_jugador, d_enemigo, resultado)