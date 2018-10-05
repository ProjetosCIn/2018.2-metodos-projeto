from sympy import sympify

def euler(y0, t0, h, qntSteps, func):
	expr = sympify(func)
	print("Metodo de Euler")
	print(expr)
	print("y(", t0, ") = ", y0)
	print("h = ", h)
	lastY = y0
	currentY = lastY
	for step in range (0, qntSteps + 1):
		print(int(step), " ", currentY)
		currentY = lastY + (expr.subs([("y", float(lastY)), ("t", t0)]))*h
		lastY = float(currentY)
		t0 += h
	print("")
	return 0

def euler_aprimorado(y0, t0, h, qntSteps, func):
	expr = sympify(func)
	print("Metodo de Euler Aprimorado")
	print(expr)
	print("y(", t0, ") = ", y0)
	print("h = ", h)
	lastY = y0
	currentY = lastY
	for step in range (0, qntSteps + 1):
		print(step, " ", currentY)

		fn = expr.subs([("t", t0) , ("y", float(lastY))])
		fn_1 = expr.subs([("t", t0 + 1), ("y", float(fn))])

		currentY = lastY + ((fn + fn_1) * h) / 2
		lastY = float(currentY)
		t0 += h
		
	print("")
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
				euler_aprimorado(float(inputs[1]), float(inputs[2]), float(inputs[3]), int(inputs[4]), inputs[5])

main()