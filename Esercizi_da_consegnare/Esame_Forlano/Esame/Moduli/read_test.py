##
# Testo che venga solleata un'eccezione nel caso in cui l'immagine non esiste

import unittest
from read import read_img

class test_read (unittest.TestCase):
    def test_read_img(self):
        PATH_IMG = ".\\Esame\\immagini\\"
        NOME_ERR = "SSCF0336.jpg" # Con NOME_ERR il test deve essere positivo
        NOME_OK = "DSCF0336.jpg" # Con NOME_OK il test deve fallire
        with self.assertRaises(ValueError):
            img = read_img(PATH_IMG, NOME_ERR)

if __name__ == "__main__":
    unittest.main()
