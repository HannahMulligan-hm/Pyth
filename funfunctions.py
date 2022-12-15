# arr = 2001
# def odd_even(num):
# 	for i in range (num):
# 		if i % 2 == 0:
# 			print ("Number is {}. " "This is an even number.".format(i))
# 		else:
# 			print ("Number is {}. " " This is an odd number.".format(i)) 

# print odd_even(arr)

a = [2,4,10,16]
def multiply(num, x):
	for i in range(len(num)):
		num[i] = num[i] * x
	print num

print multiply(a,5)


