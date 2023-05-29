import random
import statistics as st
from matplotlib import pyplot as ptl
import numpy as np
import pandas as ps

flujocaja_number_bet = []

initial_bet = 20
max_losses = 1000

def martin_gale_bet(initial_bet, numeroTiradas):
    bet_number = 3
    total_money = 10000
    bet_amount = initial_bet
    losses = 0
    Tiradas = 0
    for i in range(0, numeroTiradas):
        if bet_amount > total_money:
            print("No tienes suficiente dinero para hacer la siguiente apuesta.")
            break
        print("Monto de apuesta actual", bet_amount)
        
        winning_number = random.randint(0, 36)
        if winning_number == bet_number:
            total_money += (bet_amount*35)
            flujocaja_number_bet.insert(i, total_money)
            print("Ganaste! Tu dinero total es:", total_money)
            bet_amount = initial_bet
            Tiradas+=1
        else:
            total_money -= bet_amount
            flujocaja_number_bet.insert(i, total_money)
            print("Perdiste. Tu dinero total es:", total_money)
            Tiradas+=1
            if Tiradas == numeroTiradas:
                print("You've reached the maximum number of losses.")
                break
            bet_amount *= 2
    return total_money




#winning_numbers = [32, 15, 19, 4, 21] # Ejemplo de números ganadores, reemplazar con números reales de la ruleta


#total_money = martin_gale_bet(initial_bet, max_losses)
#print("Final total money:", total_money)

#--------------------------------------------------------------------------------------------------------------------
#Color dependiendo del numero que salga

print('JUGANDO POR COLORES')
initial_bet = 20
numeroTiradas = 1000
initialmoney = 0
Colornumber = ['v','r','n','r','n','r','n','r','n','r','n','n','r','n','r','n','r','n','r','r','n','r','n','r','n','r','n','r','n','n','r','n','r','n','r','n','r']
FrRachaBuena = [0 for i in range(numeroTiradas)]
ContadorRacha = 0
flujocaja = []
PromediosFlujosCajas = [0 for i in range(numeroTiradas)]
tirada = 0

def martin_gale_bet_colors(initial_bet, numeroTiradas):
    bet_amount = initial_bet
    color_bet = 'r'
    total_money2 = initialmoney
    flujocaja.clear()
    ContadorRacha = 0
    

    wins = 0
    for i in range(0, numeroTiradas):
        """if bet_amount > total_money2:
            print("No tienes suficiente dinero para hacer la siguiente apuesta.")
            for j in range(i, 1000):
                    flujocaja.insert(j, total_money2) 
            break"""
        #print("Monto de apuesta actual", bet_amount)
        winning_number = random.randint(0, 36)
        if is_winning_color(color_bet,winning_number):
            total_money2 += bet_amount
            FrRachaBuena[ContadorRacha] += 1
            ContadorRacha = 1
            PromediosFlujosCajas[i] += total_money2
            flujocaja.insert(i, total_money2)
            #print("Ganaste! Tu dinero total es:", total_money2)
            bet_amount = initial_bet
    
        else:
            total_money2 -= bet_amount
            ContadorRacha += 1
            flujocaja.insert(i, total_money2)
            PromediosFlujosCajas[i] += total_money2
            #print("Perdiste. Tu dinero total es:", total_money2)

            bet_amount *= 2
    return total_money2



def is_winning_color(color_bet,winning_number):
    if Colornumber[winning_number] == color_bet:
        return True
    else: 
        return False



#------------------Grafico Flujo Caja Una Corrida----------------#
total_money2 = martin_gale_bet_colors(initial_bet, numeroTiradas)
#total_money = martin_gale_bet(initial_bet, numeroTiradas)
print("Final total money:", total_money2)
print(flujocaja)
df2 = ps.DataFrame(flujocaja)
df2.plot(linewidth=1, title= 'Flujo de caja', xlabel = 'n (numero de tiradas)', ylabel = 'cc (cantidad de capital)')
ptl.axhline(y= initialmoney, color = 'y', linestyle = '--')
ptl.show()
#------------------Grafico Flujo de Caja comparacion pleno vs rojo/negro----------------#

"""ptl.plot(flujocaja)
ptl.plot(flujocaja_number_bet)
ptl.axhline(y= initialmoney, color = 'y', linestyle = '--')
ptl.show()"""

#------------------Graficos Flujos----------------#
numerorondas = 30
for k in range(0, numerorondas):
    total_money2 = martin_gale_bet_colors(initial_bet, numeroTiradas)
    ptl.plot(flujocaja)

ptl.axhline(y= initialmoney, color = 'y', linestyle = '--')
ptl.show()

#------------------Grafico Frecuencia Relativa Rachas ----------------#

df1 = ps.DataFrame(FrRachaBuena)
print(df1)
df1.plot(color="r",linewidth=10, kind='bar', title= 'Frecuencia relativa de obtener la apuesta favorable segun n', xlabel = 'n (numero de tiradas)', ylabel = 'fr (frecuencia relativa)')
ptl.show()

#------------------Promedio de Flujos de Caja --------------------------#

for i in range(0, numeroTiradas):
    print (PromediosFlujosCajas[i])
    PromediosFlujosCajas[i] = (PromediosFlujosCajas[i]/numerorondas)
    print (PromediosFlujosCajas[i])

ptl.axhline(y= initialmoney, color = 'y', linestyle = '--')
ptl.plot(PromediosFlujosCajas)
ptl.show()

#------------------Promedio de Fr Relativas --------------------------#

numerorondas = 30
for k in range(0, numerorondas):
    total_money2 = martin_gale_bet_colors(initial_bet, numeroTiradas)
for i in range(0, numeroTiradas):
    FrRachaBuena[i] = FrRachaBuena[i]/numerorondas

df1 = ps.DataFrame(FrRachaBuena)
print(df1)
df1.plot(color="r",linewidth=1, kind='bar', title= 'Promedio Frecuencia relativa de obtener la apuesta favorable segun n', xlabel = 'n (numero de tiradas)', ylabel = 'fr (frecuencia relativa)')
ptl.show()