def wordloop(n, func, func2):

	characters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'w', 'x', 'y', 'z', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '=', '+', '\\', '|', '[', ']','{', '}', ':', ';', '"', '\'', ',', '<', '>', '.', '/', '?', 'A', 'B', 'C','D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
	array = [0]
	t1 = datetime.datetime.now()

	for count in range(1, n+1):
		output = ""
		a = 0
		for each in array:
			if each == len(characters):
				array[a] = 0

				if len(array) > a+1:
					array[a+1] += 1
				else:
					array.append(0)
			a += 1

		for everyOne in array:
			output += characters[everyOne]
		array[0] += 1
		func(output)
	func2(datetime.datetime.now()-t1)
