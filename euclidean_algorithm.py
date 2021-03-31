def euclidean_algorithm(x, y):
	mx, mn = max(x, y), min(x, y)

	while True:
		tmp = mx
		for i in range(1, mx):
			if i * mn == mx:
				return mn

			if i * mn > mx:
				mx, mn = mn, mx - (i - 1) * mn
				break

		if tmp == mx:
			return -1
