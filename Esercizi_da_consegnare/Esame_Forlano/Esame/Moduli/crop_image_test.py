##
# Testo che ci sia ugualianza tra la roi ottentua con la la funzione e una roi di test.

# Importo le librerie
import unittest
import cv2 as cv
from crop_image import roi

'''
Con questa classe andiamo a testare il modulo crop_image 
e la funzione roi andando ad inserire i valori di esempio che vengono printati nel terminale.
Andiamo a confrotnare l'array roi_img derivante dalla funzione con un array roi_img_test.
'''
class test_roi(unittest.TestCase):
    def test_roi(self):
        PATH_IMG = ".\\Esame\\immagini\\DSCF0336.jpg"
        img = cv.imread(PATH_IMG, cv.IMREAD_GRAYSCALE)

        roi_img = roi(img) # Funzione da testare

        roi_img_test = img[800:1000 ,2000:2400] # Valori dell'esempio nella funzione
        
        # assertEqual -> funzione di libreria unittest che viene utilizzata per verificare l'uguaglianza di due valori.
        self.assertEqual(roi_img.all(), roi_img_test.all()) # array.all() per verificare l'ugualianza di tutti i valori nell'array

if __name__ == "__main__":
    unittest.main()
