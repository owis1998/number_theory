def trial_division(n):
	if n < 2:
		return False

	for i in range(2, int(n ** 0.5) + 2):
		if n % i == 0 and i != n:
			return False
	else:
		return True
