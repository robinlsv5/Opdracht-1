def prime_factor(num):
	"""Maximum prime number."""
	best = None
	factor = 2
	while factor * factor <= num:
		while num % factor == 0:
			best = factor
			num /= factor
		factor += 1
	if (num > 1):
		return num
	return best
	
	
print(prime_factor(600851475143))