a_int_low = float(input("Inserire il valore dell'estremo inferiore dell'intervallo a ...")) #estremo inferiore dell'intervallo in cui cercare lo zero   #! check -5
b_int_up = float(input("Inserire il valore dell'estremo superiore dell'intervallo b ..."))  #estremo superiore dell'intervallo in cui cercare lo zero   #! check 10
m_div = int(input("Inserire il valore di suddivisioni dell'intervallo [a,b] ..."))  #suddivisioni dell'intervallo [a,b]                                 #! check 5
h_largh_div = (b_int_up-a_int_low)/m_div                                                                                                                #! da m_div=5 ->h_larg_int=3
sub_int_est = []                                                                            #! lista che contiene gli estremi dei sottointervalli
x_mid_sub_int = []                                                                          #! lista che contiene i punti medi degli estremi dei sottointervalli
h_rect = []                                                                                 #! lista che contiene le altezze di ogni rettangolo
sub_areas = []                                                                                                                                  #! lista che contiene le basi dei rettangoli?
    
for i in range(0,m_div):
    sub_int_est.append([float((a_int_low+i*h_largh_div)), float((a_int_low+(i+1)*h_largh_div))])    #!append degli estremi dei sottointervalli come lista di lista
    x_mid_sub_int.append(sum(sub_int_est[i])/2)                                                         #! append dei punti medi nella relativa lista
    h_rect.append(x_mid_sub_int)                                                                #! append dei valori di f(x_med_i)
    sub_areas.append(h_rect[i]*abs(sum(sub_int_est[i])))                                                #! append dei valori delle aree dei rettangoli i-esimi
area_tot = sum(sub_areas)

print(sub_int_est)
print(x_mid_sub_int)
print(h_rect)
print(sub_areas)
print(area_tot)