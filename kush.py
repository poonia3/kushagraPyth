def wordloop(n):
	import datetime
	chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z',' ']
	array = [0]
	z = 0
	for x in range(0, n+1):
		z += len(chars) ** x
	for count in range(0, z-1):
		t1 = datetime.datetime.now()
		a = 0
		output = ""
		for each in array:
			if each == len(chars):
				array[a] = 0
				if len(array) > a+1:
					array[a+1] += 1
				else:
					array.append(0)
			a += 1
		for everyOne in array:
			output += chars[everyOne]
		array[0] += 1
	print("'"+output+"'")
	print(datetime.datetime.now()-t1)
