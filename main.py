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


def adam_bashforth_2(y0, t0, h, qntSteps, func):
	return
def adam_bashforth_3(y0, t0, h, qntSteps, func):
	return
def adam_bashforth_4(y0, t0, h, qntSteps, func):
	return
def adam_bashforth_5(y0, t0, h, qntSteps, func):
	return
def adam_bashforth_6(y, t0, h, qntSteps, func):
	expr = sympify(func)
	
	ctes = [float(4277/1440), float(-2641/480), 4991/720, -3649/720, 959/480, -95/288]
	y__5 = float(y[0])
	y__4 = float(y[1])
	y__3 = float(y[2])
	y__2 = float(y[3])
	y__1 = float(y[4])


	print("Metodo Adan-Bashforth")
	print("y(", t0, ") = ", y__5)
	print("h = ", h)
	print("0 ", y__5)
	print("1 ", y__4)
	print("2 ", y__3)
	print("3 ", y__2)
	print("4 ", y__1)
	#Y_1 = yn+1
	y = y__1
	for step in range (5, qntSteps + 1):
		
		f = expr.subs([("t", t0), ("y", y)])
		f__1 = expr.subs([("t", t0 + h), ("y", y__1)])
		f__2 = expr.subs([("t", t0 + 2 * h), ("y", y__2)])
		f__3 = expr.subs([("t", t0 + 3 * h), ("y", y__3)])
		f__4 = expr.subs([("t", t0 + 4 * h), ("y", y__4)])
		f__5 = expr.subs([("t", t0 + 5 * h), ("y", y__5)])
		y = y + h*(				ctes[0] * f + 
											ctes[1] * f__1 +
											ctes[2] * f__2 +
											ctes[3] * f__3 +
											ctes[4] * f__4 +
											ctes[4] * f__5 )

		print(step, " ", y)
		t0 += h

	
	print(y, h, func)
	return
def adam_bashforth_7(y0, t0, h, qntSteps, func):
	return
def adam_bashforth_8(y0, t0, h, qntSteps, func):
	return

def adam_bashforth(input):
	print(input)
	ordem = input[len(input) - 1] 
	print(ordem)
	if(ordem == "2"):
		pass
	elif(ordem == "3"):
		pass
	elif(ordem == "4"):
		pass
	elif(ordem == "5"):
		pass
	elif(ordem == "6"):
		adam_bashforth_6(input[0:5], float(input[5]), float(input[6]), int(input[7]), input[8])
		pass
	elif(ordem == "7"):
		pass
	elif(ordem == "8"):
		pass
	else:
		print("Deu ruim")
def main():
	readFile('entradas.txt')

def readFile(path):
	with open(path) as f:
		for line in f:
			inputs = line.split()
			if(inputs[0] == 'euler'):
				euler(float(inputs[1]), float(inputs[2]), float(inputs[3]), int(inputs[4]), inputs[5])
			elif(inputs[0] == 'euler_inverso'):
				euler_inverso(float(inputs[1]), float(inputs[2]), float(inputs[3]), int(inputs[4]), inputs[5])
			elif(inputs[0] == 'euler_aprimorado'):
				euler_aprimorado(float(inputs[1]), float(inputs[2]), float(inputs[3]), int(inputs[4]), inputs[5])
			elif(inputs[0] == 'runge_kutta'):
				runge_kutta(float(inputs[1]), float(inputs[2]), float(inputs[3]), int(inputs[4]), inputs[5])
			elif(inputs[0] == 'adam_bashforth'):
				adam_bashforth(inputs[1:])
main()