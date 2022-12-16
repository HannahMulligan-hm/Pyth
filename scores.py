import random 
random_num = random.randint(59,101)

def scores(x):
	if x < 60:
		return "F"
	elif x < 69:
		return "D"
	elif x < 79:
		return "C"
	elif x < 89:
		return "B"
	elif x < 100:
		return "A"
s = scores(random_num)
print ("Score: {}; Your grade is {} ").format(random_num , s)



