pt = input("Input a plaintext: ").upper()
k = input("Input a key: ").upper()
# Help from Mrs. Karp

alph = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

keyStream = []
encodedPhrase = []

def keyStreamCreator(k, pt):
	j = 0
	
	for i in range(len(pt)):
		j = i
		
		while j >= len(k):
			j = j - len(k)
		
		keyStream.append(k[j])
	
	print(keyStream)

keyStreamCreator(k, pt)

def vigenereCypher(ks, pt):
	for i in range(len(pt)):
		x = alph.index(pt[i])
		y = alph.index(ks[i])
		z = x + y
		
		if z > 25:
			z-=len(alph)
			
		encodedPhrase.append(alph[z])
	print(encodedPhrase)

vigenereCypher(keyStream,pt)


