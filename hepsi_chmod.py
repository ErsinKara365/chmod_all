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
