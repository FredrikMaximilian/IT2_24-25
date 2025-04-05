from batteriTesting_Biblotek import *


"""
#test 1 Ønsket funksjon
b1 = Batteri("B1", "høy", 45)
b1.visinfo()
b1.lading()
b1.visinfo()
"""
#test 2 negativ startverdi
b1 = Batteri("B1", "høy", -45)
b1.visinfo()
b1.lading()
b1.visinfo()