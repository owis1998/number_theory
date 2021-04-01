def sieve_eratosthenes(n):
	primes = [2]
	for i in range(2, n + 1):
		if i * i > n:
			return primes

		if i == 2:
			for j in range(2, n + 1):
				if j % i != 0:
					primes.append(j)

		else:
			for j in primes:
				if j % i == 0 and i != j:
					primes.remove(j)
