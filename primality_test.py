def trial_division(n):
	for i in range(2, int(n ** 0.5)):
		if n % i == 0:
			return False
	else
		return True
