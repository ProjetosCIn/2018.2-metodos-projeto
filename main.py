from sympy import sympify
from sympy.solvers import solve
from sympy import Symbol

def euler(y0, t0, h, qntSteps, func):
	expr = sympify(func)
	print("Metodo de Euler")
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

# Bonusss, sem metodo de previsao
# yn+1 = yn + h * f(tn+1, yn+ 1)
# yn + h * f(tn+1, yn+ 1) - yn+1 = 0
def euler_inverso(y0, t0, h, qntSteps, func):
	expr = sympify(func)
	print("Metodo de Euler Inverso")
	print("y(", t0, ") = ", y0)
	print("h = ", h)
	lastY = y0
	y = Symbol('y')
	# y = yn+1
	# lastY = yn
	for step in range (0, qntSteps + 1):
		print(int(step), " ", lastY)
		lastY = solve((lastY + expr * h - y).subs("t", t0 + h), y)[0]
		t0 += h
	print("")
	return 0

def euler_aprimorado(y0, t0, h, qntSteps, func):
	expr = sympify(func)
	print("Metodo de Euler Aprimorado")
	print("y(", t0, ") = ", y0)
	print("h = ", h)
	lastY = y0
	currentY = lastY
	for step in range (0, qntSteps + 1):
		print(step, " ", currentY)

		# Este é o calculo de fn
		# Lembrar que para calcular fn+1 , é necessário calcular o Y+1
		# Para utilizar na fórmula
		fn = expr.subs([("t", t0) , ("y", lastY)])
		fn_1 = expr.subs([("t", t0 + h), ("y", fn * h + lastY)])

		currentY = lastY + (fn + fn_1) * h / 2
		lastY = float(currentY)
		t0 += h
		
	print("")
	return 0

def runge_kutta(y0, t0, h, qntSteps, func):
	expr = sympify(func)

	print("Metodo de Runge-Kutta")
	print("y(", t0, ") = ", y0)
	print("h = ", h)
	lastY = y0
	currentY = lastY

	for step in range (0, qntSteps + 1):
		print(step, " ", currentY)
		
		k1 = expr.subs([("t", t0) , ("y", float(lastY))])
		k2 = expr.subs([("t", t0 + h / 2) , ("y", float(lastY) + h / 2 * k1)])
		k3 = expr.subs([("t", t0 + h / 2) , ("y", float(lastY) + h / 2 * k2)])
		k4 = expr.subs([("t", t0 + h) , ("y", float(lastY) + h * k3)])

		currentY = lastY + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
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
			#if(inputs[0] == 'euler'):
			#	euler(float(inputs[1]), float(inputs[2]), float(inputs[3]), int(inputs[4]), inputs[5])
			if(inputs[0] == 'euler_inverso'):
				euler_inverso(float(inputs[1]), float(inputs[2]), float(inputs[3]), int(inputs[4]), inputs[5])
			#elif(inputs[0] == 'euler_aprimorado'):
			#	euler_aprimorado(float(inputs[1]), float(inputs[2]), float(inputs[3]), int(inputs[4]), inputs[5])
			#elif(inputs[0] == 'runge_kutta'):
			#	runge_kutta(float(inputs[1]), float(inputs[2]), float(inputs[3]), int(inputs[4]), inputs[5])

main()