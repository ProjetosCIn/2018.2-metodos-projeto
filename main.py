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
	expr = sympify(func)
	
	ctes = [1901/720, -1387/360, 109/30, -637/360, 251/720]

	y__4 = float(y0[0])
	y__3 = float(y0[1])
	y__2 = float(y0[2])
	y__1 = float(y0[3])
	y =  float(y0[4])

	print("Metodo Adan-Bashforth")
	print("y(", t0, ") = ", y__4)
	print("h = ", h)
	print("0 ", y__4)
	print("1 ", y__3)
	print("2 ", y__2)
	print("3 ", y__1)
	print("4 ", y)
	for step in range (5, qntSteps + 1):
		
		f = expr.subs([("t", t0 + 4 * h), ("y", y)])
		f__1 = expr.subs([("t", t0 + 3 *  h), ("y", y__1)])
		f__2 = expr.subs([("t", t0 + 2 * h), ("y", y__2)])
		f__3 = expr.subs([("t", t0 + 1 * h), ("y", y__3)])
		f__4 = expr.subs([("t", t0 ), ("y", y__4)])

		y__4 = y__3
		y__3 = y__2
		y__2 = y__1
		y__1 = y
		y = y + h*(				ctes[0] * f + 
											ctes[1] * f__1 +
											ctes[2] * f__2 +
											ctes[3] * f__3 +
											ctes[4] * f__4 )
		print(step, " ", y)
		t0 += h
	return

def adam_bashforth_6(y, t0, h, qntSteps, func):
	expr = sympify(func)
	
	ctes = [4277/1440, -2641/480, 4991/720, -3649/720, 959/480, -95/288]

	y__5 = float(y0[0])
	y__4 = float(y0[1])
	y__3 = float(y0[2])
	y__2 = float(y0[3])
	y__1 = float(y0[4])
	y =  float(y0[5])

	print("Metodo Adan-Bashforth")
	print("y(", t0, ") = ", y__5)
	print("h = ", h)
	print("0 ", y__5)
	print("1 ", y__4)
	print("2 ", y__3)
	print("3 ", y__2)
	print("4 ", y__1)
	print("5 ", y)

	for step in range (6, qntSteps + 1):
		
		f = expr.subs([("t", t0 + 5 * h), ("y", y)])
		f__1 = expr.subs([("t", t0 + 4 *  h), ("y", y__1)])
		f__2 = expr.subs([("t", t0 + 3 * h), ("y", y__2)])
		f__3 = expr.subs([("t", t0 + 2 * h), ("y", y__3)])
		f__4 = expr.subs([("t", t0 + 1 * h ), ("y", y__4)])
		f__5 = expr.subs([("t", t0 ), ("y", y__5)])

		y__5 = y__4
		y__4 = y__3
		y__3 = y__2
		y__2 = y__1
		y__1 = y
		y = y + h*(				ctes[0] * f + 
											ctes[1] * f__1 +
											ctes[2] * f__2 +
											ctes[3] * f__3 +
											ctes[4] * f__4 +
											ctes[5] * f__5)
		print(step, " ", y)
		t0 += h
	return

def adam_bashforth_7(y0, t0, h, qntSteps, func):
	expr = sympify(func)
	
	ctes = [198721/60480, -18637/2520, 235183/20160, -10754/945, 135713/20160, -5603/2520, 19087/60480]

	y__6 = float(y0[0])
	y__5 = float(y0[1])
	y__4 = float(y0[2])
	y__3 = float(y0[3])
	y__2 = float(y0[4])
	y__1 = float(y0[5])
	y =  float(y0[6])

	print("Metodo Adan-Bashforth")
	print("y(", t0, ") = ", y__6)
	print("h = ", h)
	print("0 ", y__6)
	print("1 ", y__5)
	print("2 ", y__4)
	print("3 ", y__3)
	print("4 ", y__2)
	print("5 ", y__1)
	print("6 ", y)

	for step in range (7, qntSteps + 1):
		
		f = expr.subs([("t", t0 + 6 * h), ("y", y)])
		f__1 = expr.subs([("t", t0 + 5 *  h), ("y", y__1)])
		f__2 = expr.subs([("t", t0 + 4 * h), ("y", y__2)])
		f__3 = expr.subs([("t", t0 + 3 * h), ("y", y__3)])
		f__4 = expr.subs([("t", t0 + 2 * h ), ("y", y__4)])
		f__5 = expr.subs([("t", t0 + 1 * h ), ("y", y__5)])
		f__6 = expr.subs([("t", t0 ), ("y", y__6)])

		y__6 = y__5
		y__5 = y__4
		y__4 = y__3
		y__3 = y__2
		y__2 = y__1
		y__1 = y
		y = y + h*(				ctes[0] * f + 
											ctes[1] * f__1 +
											ctes[2] * f__2 +
											ctes[3] * f__3 +
											ctes[4] * f__4 +
											ctes[5] * f__5 +
											ctes[6] * f__6)
		print(step, " ", y)
		t0 += h
	return

def adam_bashforth_8(y0, t0, h, qntSteps, func):
	expr = sympify(func)
	
	[16083/4480, -1152169/120960, 242653/13440, -296053/13440, 2102243/120960, -115747/13440, 32863/13440, -5257/17280]

	y__7 = float(y0[0])
	y__6 = float(y0[1])
	y__5 = float(y0[2])
	y__4 = float(y0[3])
	y__3 = float(y0[4])
	y__2 = float(y0[5])
	y__1 = float(y0[6])
	y =  float(y0[7])

	print("Metodo Adan-Bashforth")
	print("y(", t0, ") = ", y__7)
	print("h = ", h)
	print("0 ", y__7)
	print("1 ", y__6)
	print("2 ", y__5)
	print("3 ", y__4)
	print("4 ", y__3)
	print("5 ", y__2)
	print("6 ", y__1)
	print("7 ", y)

	for step in range (8, qntSteps + 1):
		
		f = expr.subs([("t", t0 + 7 * h), ("y", y)])
		f__1 = expr.subs([("t", t0 + 6 *  h), ("y", y__1)])
		f__2 = expr.subs([("t", t0 + 5 * h), ("y", y__2)])
		f__3 = expr.subs([("t", t0 + 4 * h), ("y", y__3)])
		f__4 = expr.subs([("t", t0 + 3 * h ), ("y", y__4)])
		f__5 = expr.subs([("t", t0 + 2 * h ), ("y", y__5)])
		f__6 = expr.subs([("t", t0 + 1 * h), ("y", y__6)])
		f__7 = expr.subs([("t", t0 ), ("y", y__7)])

		y__7 = y__6
		y__6 = y__5
		y__5 = y__4
		y__4 = y__3
		y__3 = y__2
		y__2 = y__1
		y__1 = y
		y = y + h*(				ctes[0] * f + 
											ctes[1] * f__1 +
											ctes[2] * f__2 +
											ctes[3] * f__3 +
											ctes[4] * f__4 +
											ctes[5] * f__5 +
											ctes[6] * f__6 +
											ctes[7] * f__7)
		print(step, " ", y)
		t0 += h
	return

# Função que chama o metodo de adam bashforth a depender do grau
def adam_bashforth(input):
	print(input)
	ordem = input[len(input) - 1] 
	if(ordem == "2"):
		adam_bashforth_5(input[0:2], float(input[2]), float(input[3]), int(input[4]), input[5])
	elif(ordem == "3"):
		adam_bashforth_3(input[0:3], float(input[3]), float(input[4]), int(input[5]), input[6])
	elif(ordem == "4"):
		adam_bashforth_5(input[0:4], float(input[4]), float(input[5]), int(input[6]), input[7])
	elif(ordem == "5"):
		adam_bashforth_5(input[0:5], float(input[5]), float(input[6]), int(input[7]), input[8])
	elif(ordem == "6"):
		adam_bashforth_5(input[0:6], float(input[6]), float(input[7]), int(input[8]), input[9])
	elif(ordem == "7"):
		adam_bashforth_5(input[0:7], float(input[7]), float(input[8]), int(input[9]), input[10])
	elif(ordem == "8"):
		adam_bashforth_5(input[0:8], float(input[8]), float(input[9]), int(input[10]), input[11])
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