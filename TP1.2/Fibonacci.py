import random
import statistics as st
import matplotlib.pyplot as ptl
import numpy as np
import pandas as ps
total=1000
fibo=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
Nroapostado=18
Rojos=[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
PP=[]

def TA(TotalApuesta:list):
    p=0
    for a in TotalApuesta:
        p+=a
    return p

def seq(i):
    p= i % len(fibo)
    return fibo[p]
def max(FlujoCapitalRojoCL:list):
    for p in FlujoCapitalRojoCL:
        if p>0:
            m=p
    return m
def CI(x):
    return TotalParaApostar
def MaxMin(List:list,n):
    mm=0
    if n==1:
        for a in List:
            if a>mm:
                mm=a
    if n==2:
        for a in List:
            if a<mm:
                mm=a
    return mm
def PdP(a,q):
    r=0
    if q==1:
        r=st.mean(PP)
    elif q==2:
        r=10000
    return r

def graf(figure,x,data,xlabel,ylabel,title): #Funcion para setear valores de las graficas
    ptl.figure(figure) #Nombre figura
    ptl.plot(x,data) #Datos para graficar
    ptl.xlim(0,total) #Rango del eje de las abscisas
    ptl.xlabel(xlabel) #Cartel de las abscisas
    ptl.ylabel(ylabel) #Cartel del eje ordenadas
    ptl.title(title) #Titulo del grafico
    ptl.grid() #Grilla
            
for p in range(30):
    TotalParaApostar=100
    FlujoCapitalRojoSL=[]
    FlujoCapitalRojoCL=[]
    PromSL=[]
    PromCL=[]
    Fr=[]
    FR=[]
    NroRuleta=[]
    TotalParaApostar=10000
    for i in range(total):
        NroRuleta.append(random.randint(0,36))

    #Sin limite
    apuesta=1
    apuesta2=1
    f=0
    w=0
    g=0
    m=0
    l=0
    for a in NroRuleta:
        if a in Rojos:
            if f >1:
                apuesta=seq(f:=f-2)
            else:
                apuesta=seq(f:=0)
            if len(FlujoCapitalRojoSL)==0:
                FlujoCapitalRojoSL.append(apuesta)
            else:
                FlujoCapitalRojoSL.append(apuesta)#FlujoCapitalRojo[len(FlujoCapitalRojo)-1]
            w+1
        else:
            if f<=1:
                apuesta=seq(f)
                f+=1
            else:
                apuesta=seq(f:=f+1)
            if len(FlujoCapitalRojoSL)>0:
                FlujoCapitalRojoSL.append(-apuesta) #FlujoCapitalRojo[len(FlujoCapitalRojo)-1]
            else:
                FlujoCapitalRojoSL.append(-apuesta)
        PromSL.insert(l, st.mean(FlujoCapitalRojoSL))
        l+=1
    l=0
    #Con limite
    for a in NroRuleta:
        m=TotalParaApostar-apuesta2
        if m>0 :
            if a in Rojos:
                if f >1:
                    apuesta2=seq(g:=g-2)
                else:
                    apuesta2=seq(g:=0)
                if len(FlujoCapitalRojoCL)==0:
                    FlujoCapitalRojoCL.append(TotalParaApostar+apuesta2)
                else:
                    FlujoCapitalRojoCL.append(TotalParaApostar+apuesta2)#FlujoCapitalRojo[len(FlujoCapitalRojo)-1]
                TotalParaApostar+=apuesta2
            else:
                if f<=1:
                    apuesta2=seq(g)
                    f+=1
                else:
                    apuesta2=seq(g:=g+1)
                if len(FlujoCapitalRojoCL)>0:
                    FlujoCapitalRojoCL.append(m) #FlujoCapitalRojo[len(FlujoCapitalRojo)-1]
                else:
                    FlujoCapitalRojoCL.append(m)
                TotalParaApostar-=apuesta2
        else:
            FlujoCapitalRojoCL.append(max(FlujoCapitalRojoCL))
        PromCL.insert(l, st.mean(FlujoCapitalRojoCL))
        l+=1
    PP.insert(p,st.mean(FlujoCapitalRojoSL))           
    x = np.arange(0,total,1)    

    graf('Flujo capital sin limite',x,FlujoCapitalRojoSL,'Tiradas','Capital','Flujo de capital sin limite')
    graf('Promedio sin limite',x,PromSL,'Tiradas','Capital','Promedio del flujo de capital sin limite')
    graf('Flujo capital con limite',x,FlujoCapitalRojoCL,'Tiradas','Capital','Flujo de capital con limite')
    graf('Promedio con limite',x,PromCL,'Tiradas','Capital','Promedio del flujo de capital con limite')

ptl.figure('Promedio sin limite')#Ubicar grafico por nombre
ptl.plot(x, [PdP(q,1) for q in x], color='k', label='Promedio esperado ('+str(PdP(1,1))+')')
ptl.legend(loc='upper left')
ptl.figure('Promedio con limite')#Ubicar grafico por nombre
ptl.plot(x, [PdP(q,2) for q in x], color='k', label='Capital Inicial (10000)')
ptl.legend(loc='upper left')
ptl.figure('Flujo capital con limite')#Ubicar grafico por nombre
ptl.plot(x, [PdP(q,2) for q in x], color='k', label='Capital Inicial (10000)')
ptl.legend(loc='upper left')
ptl.show()