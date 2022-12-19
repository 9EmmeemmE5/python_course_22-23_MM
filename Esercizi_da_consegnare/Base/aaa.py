etichette=[10,10,10,10,2,2,2,2,2,1,1,1,1,0,0,0,0,3,5,5,7,7,7,7,7,7,7,7,7,7,7,7]
id_cluster=list(set(etichette))

print(id_cluster)
lista_dim_cluster=[]


for i in range(len(id_cluster)):
    counter=0
    for j in range(len(etichette)):
        if id_cluster[i]==etichette[j]:
            counter+=1
    lista_dim_cluster.append(counter)

print(lista_dim_cluster)