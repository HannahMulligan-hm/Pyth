# #input
# listss = ['magical unicorns', 19, 'hello',98.98,'world']
# #output
# "The list you entered is of mixed type"
# "String: magical unicorns hello world"
# "Sum: 117.98"

# input
listss = [2,3,1,7,4,12]
#output
"The list you entered is of integer type"
"Sum: 29"



x = ""
y = 0
t = [0,0,0] 
for lists in listss:
	if isinstance(lists, str):
		x = x + " " + lists + " "
	elif isinstance(lists, int):
		y = y + lists
	elif isinstance(lists, float):
		y = y + lists

if y > 1 and len(x) > 0: 
	print "The list you entered is of the mixed type" 
	print "String:" + x
	print "Sum:" + str(y)
elif y == 0:
	print "The list you entered is of the string type"
	print "String:" + x
elif len(x) == 0:
	print "The list you entered is of the integer type."
	print "Sum:" + str(y)

