def A(m, N):
	alph = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	d_m = []
	for c in m:
		x = alph.index(c) + N
		if x > 25:
			x -= 26
		d_m.append(alph[x])
	return d_m

def cypher(N):
	alph = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	l = {}
	for i in range(len(alph)):
		x = i + N
		if x > (len(alph) -1):
			x = x - len(alph)
		l[alph[i]] = alph[x]
	return l
	
m = input("Input your message: ").upper()
shift = int(input("Shift number: "))

a = A(m, shift)
print("Encoded Message:", ''.join(a))
