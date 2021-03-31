def integer_factorization(n):
	factors_list = []
	
	while n != 1:
	 	for i in range(2, n):
	 		if n % i == 0:
	 			factors_list.append(i)
	 			n = int(n / i)
	 			break
	 	else:
	 		factors_list.append(n)
	 		return factors_list
