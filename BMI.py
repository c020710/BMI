x = input('Please enter the weight(kg):')
y = input('Please enter your height(m):')
x = float(x)
y = float(y)
y = (y/ 100)
z = (x/ pow(y, 2))
if z < 18.5:
	print('Thinness')
elif z >= 18.5 and z <25:
	print('Normal')
elif z >= 25 and z <30:
	print('Overweight')
else:
	print('Obesity')