"""Cicli 2"""
# TODO: calcolare la somma dei primi N numeri...
# TODO: N specificato dall'utente...

n_value = int(input("dammi N..."))

iter_count =0
my_sum_value = 0

while iter_count<=n_value:
    my_sum_value += iter_count
    iter_count+=1
    print(f"la somma dei primi {n_value} numeri e' {my_sum_value}")
    #if(iter_count>n_value):
    # qui non serve l'if perche non ho un while True, in quanto ho un if intrinseco nel while
        #break