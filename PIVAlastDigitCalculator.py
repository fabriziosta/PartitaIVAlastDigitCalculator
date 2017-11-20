print("Partita IVA last digit calculator v1.0")

continua = True

while continua:
	partitaIVA = input("Digita le prime 10 cifre della partita IVA: ")
	
	if(partitaIVA == "esci"):
		print("Programma terminato.")
		break
	elif(len(partitaIVA) == 10):
		try:
			partitaIVAnumerica = int(partitaIVA) #controllo se sono 10 numeri
		except:
			print("Inserire una partita IVA numerica!")
			print("Se vuoi interrompere il programma scrivi \"esci\"")
			continue
		
		#splitto tutto in una lista per poter lavorarci.
		partitaIVAsplittata = list(str(partitaIVAnumerica)) 
		
		#trasformo ogni elemento in numero di nuovo per poter fare operazioni matematiche
		for x in range(0, len(partitaIVAsplittata)): 
			partitaIVAsplittata[x] = int(partitaIVAsplittata[x])
			
		X = partitaIVAsplittata[0] + partitaIVAsplittata[2] + partitaIVAsplittata[4] + partitaIVAsplittata[6] + partitaIVAsplittata[8]
		Y = (partitaIVAsplittata[1]*2-9 if partitaIVAsplittata[1]*2 > 9 else partitaIVAsplittata[1]*2) + (partitaIVAsplittata[3]*2-9 if partitaIVAsplittata[3]*2 > 9 else partitaIVAsplittata[3]*2) + (partitaIVAsplittata[5]*2-9 if partitaIVAsplittata[5]*2 > 9 else partitaIVAsplittata[5]*2) + (partitaIVAsplittata[7]*2-9 if partitaIVAsplittata[7]*2 > 9 else partitaIVAsplittata[7]*2) + (partitaIVAsplittata[9]*2-9 if partitaIVAsplittata[9]*2 > 9 else partitaIVAsplittata[9]*2)
		T = (X + Y) % 10
		C = (10 - T) % 10
		print("L'ultima cifra è: ", C)
		print("Se vuoi interrompere il programma scrivi \"esci\"")
		print(X,Y,T,C)
	else:
		print("Inserire 10 cifre!")
