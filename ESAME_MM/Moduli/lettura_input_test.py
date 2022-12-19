"""Questo è un modulo di test per le funzioni presenti nel modulo lettura_input"""
import unittest
from lettura_input import lettura_immagine, lettura_input_testo
# ---------------------------------------------------------------------------------------------- #
# Creazione della classe dei test con la libreria unittest
# ---------------------------------------------------------------------------------------------- #
class TestLetturaInput(unittest.TestCase):
    """Classe di test del modulo lettura_input.py"""
# ---------------------------------------------------------------------------------------------- #
# Funzione di test del raise dell'eccezione nel caso di errori nel percorso relative al nome del
# file immagine (errato)
# ---------------------------------------------------------------------------------------------- #
    def test_lettura_immagine_errore_nome(self):
        """Funzione di test del caricamento dell'immagine"""
        percorso_immagini =".\\ESAME_MM\\Immagini\\" #!cambiare prima della consegna
        nome_file_immagine_errato = "SSCF0336.jpg"
# ---------------------------------------------------------------------------------------------- #
# >Con il nome errato il test è positivo
# ---------------------------------------------------------------------------------------------- #
        with self.assertRaises(IOError):
            lettura_immagine(percorso_immagini, nome_file_immagine_errato)
# ---------------------------------------------------------------------------------------------- #
# Funzione di test del raise dell'eccezione nel caso di errori nel percorso di posizionamento
# delle immagini
# ---------------------------------------------------------------------------------------------- #
    def test_lettura_immagine_errore_percorso(self):
        """Funzione di test del caricamento dell'immagine"""
        percorso_immagini_errato =".\\ESAME_MM\\Immagini-file\\"
# ---------------------------------------------------------------------------------------------- #
# >Con il percorso corretto il test è positivo
# ---------------------------------------------------------------------------------------------- #
        nome_file_immagine = "DSCF0336.jpg"
        with self.assertRaises(IOError):
            lettura_immagine(percorso_immagini_errato, nome_file_immagine)
# ---------------------------------------------------------------------------------------------- #
# Funzione di test del raise dell'eccezione nel caso di errori nel percorso di posizionamento
# del file di testo contenente le immagini
# ---------------------------------------------------------------------------------------------- #
    def test_lettura_file_testo(self):
        """Funzione di test dell'apertura del file contenente i nomi dei file di immagine"""
        percorso_lista_file=".\\ESAME_MM\\lista_file_immagini.txt" #!cambiare prima della consegna
        lista_testo_diviso=lettura_input_testo(percorso_lista_file)
        self.assertIsInstance(lista_testo_diviso, list)
# ---------------------------------------------------------------------------------------------- #
# >Se il percorso in cui si è inserito il file testo con i nomi immagini è corretto, allora
# >il test è positivo
# ---------------------------------------------------------------------------------------------- #
if __name__=="__main__":
    unittest.main()
