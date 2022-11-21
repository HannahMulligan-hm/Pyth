# word = "It's thanksgiving day. It's my birthday, too!"
# print word

# m = word.find('day')
# x = word.replace('day','month')

# print m
# print x

# Min and Max
# x = [2, 54, -2, 7, 12, 98]
# y = [1, 2, 0]

# print min(y)
# print max(y)

# # First and Last
# x = ["hello",2,54,-2,7,12,98,"world"]
# m = [x[0], x[len(x)-1]]
# print m

#New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x
x.sort()
print x
fl = x[:len(x)/2]
sl = x[len(x)/2:]
print "first", fl
print "second", sl
sl.insert(0,fl)
print sl
