import os
import time
import subprocess as sp

for anadizin, klasor, dosya  in os.walk(os.getcwd()):	
	for ata in dosya:
		metin = anadizin +"/"+ ata		
		sp.run(["chmod","755",metin])
		sp.run(["ls","-l",anadizin])
		time.sleep(.2)

	for bir in klasor:
		metin = anadizin +"/"+ bir		
		sp.run(["chmod","755",metin])
		sp.run(["ls","-l",anadizin])
		time.sleep(.2)


# Bütün mp4 uzantiları cekme
#not -> klasorleri 01-02-03... seklinde sırala 

import os
import time
import subprocess as sp

dizinYolu = "/home/ersin/Desktop/dersler/tasinacak_klasor"
sayi = 0 

yol = os.listdir(os.getcwd())
yol.sort()

for anadizin, klasorler, dosyalar in os.walk(os.getcwd()):
	klasorler.sort()
	
	for dosya in dosyalar:
		if dosya.endswith(".mp4"):
			veri = anadizin+"/"+dosya
			Yol = dizinYolu + str(sayi)
			sp.run(["cp", veri ,Yol])
			sayi+=1
			time.sleep(.2)
