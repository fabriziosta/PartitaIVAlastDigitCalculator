# PartitaIVAlastDigitCalculator
Calcola in automatico l'ultima cifra della partita IVA italiana

Per eseguire lo script basta avere un'installazione di python di qualsiasi tipo, digitare le prime 10 cifre della partita IVA italiana e premere invio.

Come è composta una partita IVA?
1) da 1 a 7 cifre random progressive assegnate dall'agenzia delle entrate.
2) da 8 a 10 codice ufficio provinciale (086 ENNA, 058 ROMA, 048 FIRENZE)
3) 11A cifra codice di controllo calcolato cosi:
	
	L'algoritmo impiegato per calcolare la cifra di controllo è la Formula di Luhn:
	Sia X la somma delle prime cinque cifre in posizione DISPARI
	Sia Y la somma dei doppi delle cinque cifre in posizione pari, sottraendo 9 se il doppio della cifra è superiore a 9
	Sia T=(X+Y) mod 10 l'unità corrispondente alla somma dei numeri sopra calcolati
	Allora la cifra di controllo C = (10-T) mod 10
	
Quindi se partita iva è 1234567 048 C?

X = 1 + 3 + 5 + 7 + 4 = 20
Y = 2*2 + 4*2 + ((6*2)-9) + 0*2 + ((8*2)-9) = 4 + 8 + 5 + 0 + 7 = 24
T = (20 + 24) mod 10 = 4
C = (10 - 4) mod 10 = 6


#Questo script è stato creato al fine di testing
