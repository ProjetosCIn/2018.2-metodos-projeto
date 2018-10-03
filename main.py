from sympy import sympify

def euler(y0, t0, h, func):
	expr = sympify(func)
	print(expr)
	for step in range (0, h):
		pass
	return 0


def main():
	readFile('entradas.txt')

def readFile(path):
	with open(path) as f:
		for line in f:
			inputs = line.split()
			if(inputs[0] == 'euler'):
				euler(float(inputs[1]), float(inputs[2]), int(inputs[3]), inputs[4])
			elif(inputs[0] == 'euler_inverso'):
				pass
			elif(inputs[0] == 'euler_aprimorado'):
				pass

main()