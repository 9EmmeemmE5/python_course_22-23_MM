"""Esercizio Massa-Molla-Smorzatore con forzante parametrica"""
#TODO: plottare il grafico spostamento: sistema massa molla smorzatore forzato su base input utente
#TODO: codificare con possibilità di variare la funzione e non usare solo funzione consegna
#*DONE: creare una seconda funzione che restituisca i valori da impostare in input alla 1° funzione

import numpy as np
import matplotlib.pyplot as plt

def mass_spring_damper(input_params_into_msd_funct, user_values):
    """Mass-spring-damper function"""
    sim_data_to_extract=np.zeros((input_params_into_msd_funct[4],2), dtype=np.uint16)
    for i in range (input_params_into_msd_funct[4]):
        time_interval_value=i*input_params_into_msd_funct[4]
        force=user_values[2]*np.cos(input_params_into_msd_funct[4]*time_interval_value)
        if i==0:
            y_h1=0
            y_h0=0
        elif i==1:
            y_h0=0
            y_h1=y_h2
        else:
            y_h0=sim_data_to_extract[i][1]
            y_h1=sim_data_to_extract[i+1][1]
        y_h2= input_params_into_msd_funct[0]*y_h1+input_params_into_msd_funct[1]*y_h0+force
        #TODO: codificare inserimento in matrice
    return sim_data_to_extract

def m_s_d_param_vect(user_values):
    """This function returns the mass-spring-damper parameters vactor to be inserted into the algorithm"""
    input_params_into_msd_funct = []
    alfa=(2*user_values[2]-user_values[4]*user_values[5])/user_values[2]
    beta=-(user_values[2]-user_values[4]*user_values[5]+user_values[3]*user_values[5]**2)/user_values[2]
    gamma=(user_values[5]**2)/user_values[2]
    n_samples =int((user_values[6]/user_values[5])+2)
    input_params_into_msd_funct.append(alfa)
    input_params_into_msd_funct.append(beta)
    input_params_into_msd_funct.append(gamma)
    input_params_into_msd_funct.append(n_samples)
    #TypeError sui tempi, sulla massa, k, b, in quanto non negativi
    return input_params_into_msd_funct

def user_input_val():
    """Function that creates a vector of 6 zeros to be input by user"""
    input_values=np.zeros(7) #equivale a dire [0,0,0,0,0,0,0,0] vettore nullo
    for i in range (7):      #for di inserimento degli input
        input_values[i]=float(input("inserisci valore (in ordine w_f, A_f, m, k, b, t_c, t_sim)"))
    return input_values

def main():
    """Entrypoint"""
    user_values=user_input_val()
    freq_f=user_values[0]
    mass = user_values[2]
    stiffness=user_values[3]
    damp_ratio=user_values[4]
    CYCLE_TIME=user_values[5]
    SIM_TIME=user_values[6]
    amplitude_f=user_values[1]
    print(f"I valori inseriti sono: \n frequenza della forzante {user_values[0]}, \n")
    #TODO: aggiungere controllo delle eccezioni per i valori definiti positivi
    
    #TODO: risolvere chiamate di funzioni
    funct_input_param = m_s_d_param_vect(user_values)
    sim_data = mass_spring_damper(funct_input_param, user_values)
    time_list = sim_data[:,[1]]
    travel_list = sim_data[:,[2]]
    #* plot
    fig,ax = plt.subplots()
    ax.plot(time_list, travel_list)     
    ax.set(xlabel='time (s)', ylabel='y(t) - Mass travel', title='Mass-Spring-Damper simulation')
    ax.grid()
    plt.show()
main()
