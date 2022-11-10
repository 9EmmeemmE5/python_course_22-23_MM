import numpy as np
import matplotlib.pyplot as plt

def input_values():
    values=np.zeros(6) #equivale a dire [0,0,0,0,0,0] vettore nullo
    for i in range (6):
        values[i]=float(input("inserisci un valore"))
    return values

def time(t_simulazione=0.0,t_step=0.0,massa=0.0,coeff_b=0.0,rigidezza=0.0,forzante=0.0): 
    """definisco la funzione tempo """
    my_time_list=[]
    h= int(t_simulazione/t_step)
    for i in range(h+2):
        my_time_list.append(i*t_step)
    #definisco y_value
    alpha_value= 2*massa - coeff_b*t_step
    print(alpha_value)
    beta_value= -(massa-coeff_b*t_step+rigidezza*t_step**2)
    print(beta_value)
    gamma_value= t_step**2/massa
    print(gamma_value)
    #definisco le condizioni al contorno
    my_y_list=[]

    for i in range (-2,h):
        if i==-2:
            y_h1=0
            y_h0=0
        elif i==-1:
            y_h0=0
            y_h1=y_h2 #type:ignore
        else:
            y_h0=my_y_list[i]
            y_h1=my_y_list[i+1]
        y_h2= alpha_value*y_h1 + beta_value*y_h0 #+ gamma_value*forzante
        my_y_list.append(y_h2)
    
    return my_time_list,my_y_list


def main ():
    """entry point"""
    input=input_values()
    m=input[0]
    b=input[1]
    k=input[2]
    f=input[3]
    t_c=input[4]
    t_sim=input[5]
    t_axis=time(t_sim,t_c,m,b,k,f)
    plt.plot(t_axis[0],t_axis[1])
    plt.show()
    
    print(t_axis)

main()
