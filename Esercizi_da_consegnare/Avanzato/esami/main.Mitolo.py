import progetto_Mitolo

def main():
    """entry point"""
    url = "https://s3.amazonaws.com/vrai.univpm/FI/2021/11/geodata_cdp.json"
    diz_soggetti_contratti = {}
    n = 1
    descrizioni = [] 
    lista_matchata = []
    str1 = str(input("inserisci la parola da cercare: "))
    #nel main creo le variabili che andrò ad usare nel codice
    progetto_Mitolo.creazione_testo(url)
    progetto_Mitolo.operazioni_lista(diz_soggetti_contratti,n)
    progetto_Mitolo.my_plot(diz_soggetti_contratti)
    progetto_Mitolo.ricerca_cantiere(descrizioni,str1,lista_matchata)
    #richiamo le funzioni

main()