"""mass-spring-damper simulation using numpy"""
import sys
import numpy as np
import matplotlib.pyplot as plt

def main():
    """Entrypoint for our sim"""
    if len(sys.argv)==8:    #(8 perche lo 0 è il nome del file per il sys.argv)
        mass = float(sys.argv[1])
        k_spring = float(sys.argv[2])
        damp_coeff = float(sys.argv[3])
        t_c = float(sys.argv[4])
        t_sim = float(sys.argv[5])
        position_t0=float(sys.argv[6])
        speed_t0=float(sys.argv[7])
        n_step=int(t_sim/t_c)
        #create the A, B matrix and state... 
        # #creo lo stato x_2(k) e lo x_1(k) se ho la forzante anche b
        #create the A matrix and state #parte 1 senza forzante
        A_discrete = np.zeros((2,2))
        #occorre inserire tra parentesi il comando
        #della dimensione perche si sta scrivendo la tuple
        x_discrete = np.zeros((2,1))
        #tra parentesi la shape di 2 righe e 1 colonna
        #populate A matrix
        A_discrete[0,0]=1
        A_discrete[0,1]=t_c
        A_discrete[1,0]=-t_c*k_spring/mass
        A_discrete[1,1]=1-t_c*damp_coeff/mass
        #initialize state
        # #creo il vettore dello stato iniziale per definire il valore di innesco
        x_discrete[0,0]=position_t0
        x_discrete[1,0]=speed_t0
        # x_discrete(k+1)=A_discrete*x_discrete(t)
        #crete a matrix which store, for each step, time, pos and speed
        data=np.zeros((n_step,3))
        #storing the initial values to history:
        #perche non devo partire dallo 0 nel range ma dallo step numero 2, ossia
        #quello successivo a quello iniziale
        data[0,0]=0.0   #istante iniziale, tempo iniziale
        data[0,1]=position_t0 #istante inizizale, posizione iniziale
        data[0,2]=speed_t0    #istante iniziale, velocità iniziale
        for i in range(1,n_step):
            x_discrete=np.matmul(A_discrete,x_discrete) 
            #con il matmul eseguo il matrix multiply
            #non funziona se metto
            #x_d1 perche non lo sto richiamando?
            #x_d perche assume sempre una nuova forma perche quello precedente
            #viene sovrascritto
            data[i,0]=i*t_c #nella prima posizione metto il tempo in cui sto simulando
            data[i,1]=x_discrete[0,0] #sto memorizzando la posizione, metto pos_t0
            data[i,2]=x_discrete[1,0] #sto memorizzando la velocità, metto spd_t0
        plt.plot(data[:,0], data[:,1])
        #con il ":" faccio il broadcasting di tutta la colonna dell'indice che lo segue
        plt.show()
    else:
        print("wrong number of input")