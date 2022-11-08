from math import cos
import matplotlib.pyplot as plt
def main ():
    m=float (input ("inserisci la massa della molla: m-"))
    b=float (input ("inserisci il coefficiente di smorzamento: b-"))
    k=float (input ("inserisci la rigidezza della molla: k-"))
    mi=float (input ("Inseirsci la frequenza della forzante:mi-"))
    f0=float (input ("inserisci l'ampiezza della forzante armonica f: f0=") )
    tC=float (input ("inserisci il tempo di campionamento in secondi: tC=") ) #-->tempo di campionamento sufficientemente piccolo 
    tSim=float (input ("inserisci il tempo di simulazione in secondi: ts="))
    alfa=(2*m-b*tC)/m
    beta=-(m-b*tC+k*tC**2) /m
    gamma= (tC**2) /m
    y_imeno1=0
    y_imeno2=3
    numero_di_campionamenti_in_tS=int(tSim/tC)
    spostamenti=[]
    tempi=[]
    for i in range (numero_di_campionamenti_in_tS):
        t=i*tC
        y_i=alfa*y_imeno1+beta*y_imeno2+gamma*(f0*(cos(mi*t)))
        spostamenti.append(y_i)
        tempi.append (t)
        y_imeno2=y_imeno1
        y_imeno1=y_i
    #Plot del grafico del massa molla smorzatore
    plt.plot (tempi, spostamenti)
    plt.xlabel ("tempo (s) ")
    plt.ylabel ("spostamento (m) ")
    plt.show()
main()
