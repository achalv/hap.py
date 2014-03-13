def contract(a):
	hesh = dict{}
	contracted = []
	for nums in a:
		if not nums in hesh:
			hesh[nums] = 1
			print nums, hesh[nums]	
		else:
			hesh[nums]=hesh[nums]+1
			print nums, hesh[nums]

	for k in hesh.keys():
		contracted.append(k)

	print sorted(hesh)
	print sorted(contracted)


if __name__ == '__main__':
		
	a = [2,1,2,3,4,5,5]
	d = [2,2,3,4,4,4,5,1,6,7]
	b = [34,55,20,19,47,47,55]
	c = [222,33,444,444,55]
	contract(a)
	contract(b)
	contract(c)
	contract(d)
