# # import re

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.search('My number is 415-555-4242 and 981-807-9566.')
# print('Phone number found: ' + mo.group())

# # nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
# # str1 = 'First Name: Al Last Name: Sweigart'
# # mo = nameRegex.search(str1).group()
# # print mo
# print(mo.group(1) + '\n' + mo.group(2) + '\n' + mo.group())

# str1 = "Home"
# str2 = "I am afraid of Going Home alone. I am Home sick. I am home. Homeless"
# ms = re.search(str1, str2)
# print(ms)

def main():
	x = [None]*100
	y = [1]
	x[0] = 5
	y[0] = 10

	def sum():
		x[0] = 10
		print 'Sum:', x[0]+y[0]
	def mul():
		print 'Mul:',x[0]*y[0]
		print len(x)
		
	sum()
	mul()
	print x[0], y[0]

main()