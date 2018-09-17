n1 = 0
n2 = 1
count = 0

nterms = 15

if nterms <= 0:
	print("Please enter positive number..")
elif nterms == 1:
	print("Fibonacci sqeuence yp to", nterms, ":")
	print(n1)
else:
	print("fibonacci sqeuence up to:",nterms,":")
	while count < nterms:
		print(n1, end=' , ')
		nth = n1 + n2
		n1 = n2
		n2 = nth
		count += 1