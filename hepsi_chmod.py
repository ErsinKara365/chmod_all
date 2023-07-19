import os
import time
import subprocess as sp




for anadizin, klasor, dosya  in os.walk(os.getcwd()):
	
	for ata in dosya:
		metin = anadizin +"/"+ ata		
		sp.run(["chmod","755",metin])
		sp.run(["ls","-l",anadizin])
		time.sleep(.5)

	for bir in klasor:
		metin = anadizin +"/"+ bir		
		sp.run(["chmod","755",metin])
		sp.run(["ls","-l",anadizin])
		time.sleep(.5)
        
            
        
    
        
    


# for ata in os.scandir(os.getcwd()):
#     if ata == "hepsi_chmod.py" :
#         continue
#     print(os.stat(ata).st_size)
	
