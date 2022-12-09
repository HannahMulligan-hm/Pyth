# list_one = [1,2,5,6,2]
# list_two = [1,2,5,6,2]

# list_one = [1,2,5,6,5]
# list_two = [1,2,5,6,5,3]

# list_one = [1,2,5,6,5]
# list_two = [1,2,5,6,5,3

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

j = 1
x = 0

if len(list_one) >= len(list_two):
	x = len(list_one)
else: 
	print "The lists are not the same."

for i in range (0,x):
	if list_one[i] == list_two[i]:
		j = j+ 1
		if j == x :
			print "The lists are the same"
	else:
		print "The lists are not the same."