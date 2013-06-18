# ex 33: While Loops
def six_array(lim, increment):
	stop=lim
	i=0

	for i in range(0,stop, increment):

#	while i < limit:
		print "At the top i is %d" % i
#		numbers.append(i)

		i = i+increment
		print "Numbers now: ", range(0, i, increment)
		print "At the bottom i is %d" % i

	print "The numbers:"
#	print range(0, i, increment)
#
	for num in range(0,i,increment):
		print num
six_array(5,2)