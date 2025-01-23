pt = input("Input a plaintext: ").upper()
k = input("Input a key: ").upper()

alph = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

KeyStream = []
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


