from sympy import sympify

def euler(y0, t0, h, qntSteps, func):
	expr = sympify(func)
	print(expr)
	print("y(", t0, ") = ", y0)
	print("h = ", h)
	lastY = y0
	for step in range (0, qntSteps):
		currentY = lastY + (expr.subs([("y", float(lastY)), ("t", t0)]))*h
		lastY = float(currentY)
		t0 += h

		print(int(step + 1), " ", currentY)
	return 0


def main():
	readFile('entradas.txt')

def readFile(path):
	with open(path) as f:
		for line in f:
			inputs = line.split()
			if(inputs[0] == 'euler'):
				euler(float(inputs[1]), float(inputs[2]), float(inputs[3]), int(inputs[4]), inputs[5])
			elif(inputs[0] == 'euler_inverso'):
				pass
			elif(inputs[0] == 'euler_aprimorado'):
				pass

main()