"""Cicli 1"""

# quando ci sono porzioni di codice che si ripetono,
# allora si sta entrando in un loop, ossia in un ciclo

# while tra le tradizioni in italiano coincide con finche e mentre,
# invece tutte le altre non sono del tutto corrette ed applicabili per la codifica del ciclo

print("hello")
print("hello")
print("hello")
print("hello")
print("hello")

# NO; NON SI PUO' VEDERE UNA RIPETIZIONE SCRITTA IN QUESTO MODO!
i = 0
while True:  
    # se si scrive true allora si ha un potenziale warning,
    # dato che la sezione di codice successiva diventa inaccessibile
    print(f"Current value: {i}") 
    # dato che non si esce mai da while perche non si hanno condizioni per cui si avra' un False
    # e percio' andra' avanti all'infinito
    i+=1
    # incremento la i di 1, ma senza un domani perche siamo dentro ad un
    # compound statement infinito dato dal while true
    if(i > 5):
        break
    # adesso la porzione di codice alla riga successiva e' disponibile 
    # perche python permette di uscire da un while TRUE grazie alla funzione break
print("done")
