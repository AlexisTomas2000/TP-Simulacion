import random
import statistics as st
from matplotlib import pyplot as ptl
import numpy as np
import pandas as ps

print('JUGANDO POR COLORES')
initial_bet = 20
numeroTiradas = 1000
initialmoney = 0
Colornumber = ['v','r','n','r','n','r','n','r','n','r','n','n','r','n','r','n','r','n','r','r','n','r','n','r','n','r','n','r','n','n','r','n','r','n','r','n','r']
flujocaja = []
FrRachaBuena = [0 for i in range(numeroTiradas)]
ContadorRacha = 0
PromediosFlujosCajas = [0 for i in range(numeroTiradas)]


def dalember_bet_colors(initial_bet, numeroTiradas):
    bet_amount = initial_bet
    color_bet = 'r'
    total_money2 = initialmoney
    tirada = 0
    flujocaja.clear()
    ContadorRacha = 0
    for i in range(0, numeroTiradas):
        """if bet_amount > total_money2:
            print("No tienes suficiente dinero para hacer la siguiente apuesta.")
            for j in range(i, numeroTiradas):
                flujocaja.insert(j, total_money2)
            break    """
        print("Monto de apuesta actual", bet_amount)
        winning_number = random.randint(0, 36)
        if is_winning_color(color_bet,winning_number):
            total_money2 += bet_amount
            flujocaja.insert(i, total_money2)
            FrRachaBuena[ContadorRacha] += 1
            ContadorRacha = 1
            PromediosFlujosCajas[i] += total_money2
            print("Ganaste! Tu dinero total es:", total_money2)
            if bet_amount == 1:
                bet_amount = initial_bet
            else:
                bet_amount -= 1
            tirada += 1
            if tirada == numeroTiradas:
                #print("You've reached the maximum number of losses.")
                break
        else:
            total_money2 -= bet_amount
            flujocaja.insert(i, total_money2)
            ContadorRacha += 1
            PromediosFlujosCajas[i] += total_money2
            #print("Perdiste. Tu dinero total es:", total_money2)
            tirada += 1
            if tirada == numeroTiradas:
                #print("You've reached the maximum number of losses.")
                break
            bet_amount += 1
    return total_money2



def is_winning_color(color_bet,winning_number):
    if Colornumber[winning_number] == color_bet:
        return True
    else: 
        return False



#------------------Grafico Flujo Caja Una Corrida----------------#
"""total_money2 = dalember_bet_colors(initial_bet, numeroTiradas)
print("Final total money:", total_money2)
print(flujocaja)
ptl.plot(flujocaja)
ptl.axhline(y= initialmoney, color = 'y', linestyle = '--')
ptl.show()
"""
#------------------Graficos Flujos----------------#
numerorondas = 30

for k in range(0, numerorondas):
    total_money2 = dalember_bet_colors(initial_bet, numeroTiradas)
    ptl.plot(flujocaja)

ptl.axhline(y= initialmoney, color = 'y', linestyle = '--')
ptl.show()


#------------------Grafico Frecuencia Relativa Rachas ----------------#

"""df1 = ps.DataFrame(FrRachaBuena)
print(df1)
df1.plot(color="r",linewidth=1, kind='bar',  title= 'Frecuencia relativa de obtener la apuesta favorable segun n', xlabel = 'n (numero de tiradas)', ylabel = 'fr (frecuencia relativa)')
ptl.show()"""


#------------------Promedio de Flujos de Caja --------------------------#

"""numerorondas = 30
for i in range(0, numeroTiradas):
    print (PromediosFlujosCajas[i])
    PromediosFlujosCajas[i] = (PromediosFlujosCajas[i]/numerorondas)
    print (PromediosFlujosCajas[i])

ptl.axhline(y= initialmoney, color = 'y', linestyle = '--')
ptl.plot(PromediosFlujosCajas)
ptl.show()"""
#----------------------------------------------------------------------
for k in range(0, numerorondas):
    total_money2 = dalember_bet_colors(initial_bet, numeroTiradas)
for i in range(0, numeroTiradas):
    FrRachaBuena[i] = FrRachaBuena[i]/numerorondas

df1 = ps.DataFrame(FrRachaBuena)
print(df1)
df1.plot(color="r",linewidth=1, kind='bar', title= 'Promedio Frecuencia relativa de obtener la apuesta favorable segun n', xlabel = 'n (numero de tiradas)', ylabel = 'fr (frecuencia relativa)')
ptl.show()