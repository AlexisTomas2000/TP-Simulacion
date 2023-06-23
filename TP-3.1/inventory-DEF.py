import random
from numpy import log as ln

# Variables globales
cantidad = 900
InvMax = 0
NivelInvInicial = 1000
Nivel_Inv = 0
Tipo_Evento_Sig = 0
num_evento = 0
num_mes = 120
num_valor_demanda = 4
num_politicas = 9
InvMin = 0
area_BLC_InvPos = 0.0
area_BLC_InvNeg = 0.0
Costo_unidad = 115
Costo_Incremental_Uni = 100
MaxRetraso = 1.0
Promedio_Demandas = 0.20
MinRetraso = 0.50
Prob_Distribucion_Demanda = [0.0, 0.167, 0.5, 0.833, 1.0]
CostoConf = 5000.0
Costo_Unidad_Esca = 150
Tiempo_Actual = 0.0
Tiempo_Ult_Event = 0.0
Tiempo_Prox_Event = [0.0] * 5
Costo_Total_Pedido_Realizado = 0.0
Politica_Inv = [[20, 40], [20, 60], [20, 80], [20, 100], [40, 60], [40, 80], [40, 100], [60, 80], [60, 100]]

def expon(mean_interdemand):
    return -mean_interdemand * ln(random.random())

def random_integer(prob_distrib):
    u = random.random()  # Genera una variable aleatoria U(0,1)
    i = 1
    while u >= prob_distrib[i]:
        i += 1
    return i

def uniform(a, b):
    # Devuelve una variable aleatoria U(a,b).
    return a + random.random() * (b - a)

def main():
    global num_evento, NivelInvInicial, num_mes, num_politicas
    global num_valor_demanda, Promedio_Demandas, CostoConf, Costo_Incremental_Uni, Costo_unidad
    global Costo_Unidad_Esca, MinRetraso, MaxRetraso, Prob_Distribucion_Demanda, InvMin, InvMax, Tipo_Evento_Sig
    
    # Especifico numero de eventos
    num_evento = 4
        
    # Escribe el encabezado del informe y los parámetros de entrada
    print("Sistema de inventario de un solo producto\n")
    print(f"Nivel de inventario inicial {NivelInvInicial} items\n")
    print(f"Tamaños de la demanda {num_valor_demanda}\n")
    print("Función de distribución de tamaños de demanda ")
    for i in range(1, num_valor_demanda + 1):
        print(str(Prob_Distribucion_Demanda[i]))
    print("\n")
    print(f"Tiempo medio entre demanda {Promedio_Demandas}\n")
    print(f"Rango de retraso de entrega {MinRetraso} a {MaxRetraso} meses\n")
    print(f"Duración de la simulación {num_mes} meses\n")
    print(f"K = {CostoConf} i = {Costo_Incremental_Uni} h = {Costo_unidad} pi = {Costo_Unidad_Esca}\n")
    print(f"Número de políticas {num_politicas}\n\n")
    print(" \t\t Promedio \t Promedio \t\t Promedio \t\t Promedio")
    print(" Politica \tCosto total\tcosto de pedido\tcosto de mantenimiento\tcosto de escasez")

    # Ejecuta la simulación variando la política de inventario
    for i in range(num_politicas):
        
        # Lee la política de inventario y inicializa la simulación
        InvMin, InvMax = Politica_Inv[i]
        initialize()
        
        # Ejecuta la simulación hasta que termine después de un evento de fin de simulación (tipo 3)
        while Tipo_Evento_Sig != 3:
            # Determina el siguiente evento
            timing()
            # Actualiza los acumuladores estadísticos promedio de tiempo
            update_time_avg_stats()
            # Invoca la función de evento adecuada
            if Tipo_Evento_Sig == 1:
                order_arrival()
            elif Tipo_Evento_Sig == 2:
                demand()
            elif Tipo_Evento_Sig == 4:
                evaluate()
            elif Tipo_Evento_Sig == 3:
                report()

def initialize():
    global Tiempo_Actual, Nivel_Inv, Tiempo_Ult_Event, Costo_Total_Pedido_Realizado, area_BLC_InvPos, area_BLC_InvNeg, Tiempo_Prox_Event, Tipo_Evento_Sig

    Tipo_Evento_Sig = 0
    
    # Inicializa el reloj de la simulación
    Tiempo_Actual = 0.0

    # Inicializa las variables de estado
    Nivel_Inv = NivelInvInicial
    Tiempo_Ult_Event = 0.0

    # Inicializa los contadores estadísticos
    Costo_Total_Pedido_Realizado = 0.0
    area_BLC_InvPos = 0.0
    area_BLC_InvNeg = 0.0

    # Inicializa la lista de eventos. Dado que no hay pedidos pendientes, el evento de llegada de pedidos se elimina de la consideración.
    Tiempo_Prox_Event[1] = 1.0e+30
    Tiempo_Prox_Event[2] = Tiempo_Actual + expon(Promedio_Demandas)
    Tiempo_Prox_Event[3] = num_mes
    Tiempo_Prox_Event[4] = 0.0

def timing():
    global Tipo_Evento_Sig, Tiempo_Actual
    
    min_time_next_event = 1.0e+29
    Tipo_Evento_Sig = 0

    # Determino el tipo del proximo evento.
    for i in range(1, num_evento+1):
        if Tiempo_Prox_Event[i] < min_time_next_event:
            min_time_next_event = Tiempo_Prox_Event[i]
            Tipo_Evento_Sig = i

    # Me fijo si la lista de eventos esta vacia.
    if Tipo_Evento_Sig == 0:
        # Lista vacia, termino la simulacion.
        print(f"\nLista de eventos vacia en {Tiempo_Actual}")
        exit(1)

    # Lista no vacia, avanza el reloj de simulacion.
    Tiempo_Actual = min_time_next_event

def order_arrival():
    global Nivel_Inv, Tiempo_Prox_Event

    # Incrementa el nivel de inventario según la cantidad pedida
    Nivel_Inv += cantidad

    # Dado que no hay un pedido pendiente, elimina el evento de llegada de pedidos de la consideración
    Tiempo_Prox_Event[1] = 1.0e+30

def demand():
    global Nivel_Inv, Tiempo_Prox_Event

    # Decrementa el nivel de inventario según el tamaño de la demanda generado
    Nivel_Inv -= random_integer(Prob_Distribucion_Demanda)

    # Programa el tiempo de la próxima demanda
    Tiempo_Prox_Event[2] = Tiempo_Actual + expon(Promedio_Demandas)

def evaluate():
    global Nivel_Inv, cantidad, Costo_Total_Pedido_Realizado

    # Verificar si el nivel de inventario es menor que "smalls".
    if Nivel_Inv < InvMin:
        # El nivel de inventario es menor que "smalls", por lo tanto, realizar un pedido por la cantidad correspondiente.
        cantidad = InvMax - Nivel_Inv
        Costo_Total_Pedido_Realizado += CostoConf + Costo_Incremental_Uni * cantidad
        # Programar la llegada del pedido.
        Tiempo_Prox_Event[1] = Tiempo_Actual + uniform(MinRetraso, MaxRetraso)

    # Independientemente de la decisión de realizar un pedido, programar la próxima evaluación del inventario.
    Tiempo_Prox_Event[4] = Tiempo_Actual + 1.0

def report():
    # Calcula y escribe las estimaciones de las medidas de rendimiento deseadas.
    avg_holding_cost = Costo_unidad * area_BLC_InvPos / num_mes
    avg_ordering_cost = Costo_Total_Pedido_Realizado / num_mes
    avg_shortage_cost = Costo_Unidad_Esca * area_BLC_InvNeg / num_mes
    print(f"\n({InvMin:3d},{InvMax:3d}){avg_ordering_cost + avg_holding_cost + avg_shortage_cost:15.2f}{avg_ordering_cost:15.2f}{avg_holding_cost:15.2f}{avg_shortage_cost:15.2f}")

def update_time_avg_stats():
    global Tiempo_Ult_Event, Tiempo_Actual, area_BLC_InvNeg, area_BLC_InvPos
    
    # Calcula el tiempo transcurrido desde el último evento y actualiza el marcador de último evento.
    time_since_last_event = Tiempo_Actual - Tiempo_Ult_Event
    Tiempo_Ult_Event = Tiempo_Actual

    # Determina el estado del nivel de inventario durante el intervalo anterior.
    # Si el nivel de inventario durante el intervalo anterior fue negativo, actualiza area_shortage.
    # Si fue positivo, actualiza area_holding. Si fue cero, no se necesita actualización.
    if Nivel_Inv < 0:
        area_BLC_InvNeg -= Nivel_Inv * time_since_last_event
    elif Nivel_Inv > 0:
        area_BLC_InvPos += Nivel_Inv * time_since_last_event
        
if __name__ == "__main__":
    main()