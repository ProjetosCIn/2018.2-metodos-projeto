from sympy import sympify
from sympy.solvers import solve
from sympy import Symbol

f_out = open("saida.txt","w")

# Ordem == -1, significa que pode printar
def euler(y0, t0, h, qntSteps, func, ordem):
	expr = sympify(func)
	
	pontos = []
	if(ordem == -1):
		f_out.write("Metodo de Euler \n")
		f_out.write("y(" + str(t0) + ") = " + str(y0) + "\n")
		f_out.write("h = " + str(h) + "\n")
	lastY = y0
	currentY = lastY
	for step in range (0, qntSteps + 1):
		if(ordem == -1):
			f_out.write(str(step) + " " + str(currentY) + "\n")
		pontos.append(currentY)
		currentY = lastY + (expr.subs([("y", float(lastY)), ("t", t0)]))*h
		lastY = float(currentY)
		t0 += h
	if(ordem == -1):
		f_out.write("\n")
	return pontos[0:ordem]

# Bonusss, sem metodo de previsao
# yn+1 = yn + h * f(tn+1, yn+ 1)
# yn + h * f(tn+1, yn+ 1) - yn+1 = 0
def euler_inverso(y0, t0, h, qntSteps, func, ordem):
	expr = sympify(func)

	pontos = []
	if(ordem == -1):
		f_out.write("Metodo de Euler Inverso\n")
		f_out.write("y(" + str(t0) + ") = " + str(y0) + "\n")
		f_out.write("h = " + str(h) + "\n")
	lastY = y0
	y = Symbol('y')
	# y = yn+1
	# lastY = yn
	for step in range (0, qntSteps + 1):
		if(ordem == -1):
			f_out.write(str(step) + " " + str(lastY) + "\n")
		pontos.append(lastY)
		lastY = solve((lastY + expr * h - y).subs("t", t0 + h), y)[0]
		t0 += h
	if(ordem == -1):
		f_out.write("\n")
	return pontos[0:ordem]

def euler_aprimorado(y0, t0, h, qntSteps, func, ordem):
	expr = sympify(func)

	pontos = []
	if(ordem == -1):
		f_out.write("Metodo de Euler Aprimorado\n")
		f_out.write("y(" + str(t0) + ") = " + str(y0) + "\n")
		f_out.write("h = " + str(h) + "\n")
	lastY = y0
	currentY = lastY
	for step in range (0, qntSteps + 1):
  		
		if(ordem == -1):
			f_out.write(str(step) + " " + str(currentY) + "\n")
		pontos.append(currentY)
		# Este é o calculo de fn
		# Lembrar que para calcular fn+1 , é necessário calcular o Y+1
		# Para utilizar na fórmula
		fn = expr.subs([("t", t0) , ("y", lastY)])
		fn_1 = expr.subs([("t", t0 + h), ("y", fn * h + lastY)])

		currentY = lastY + (fn + fn_1) * h / 2
		lastY = float(currentY)
		t0 += h
	
	if(ordem == - 1):
		f_out.write("\n")
	return pontos[0:ordem]

def runge_kutta(y0, t0, h, qntSteps, func, ordem):
	expr = sympify(func)

	pontos = []
	if(ordem == -1):
		f_out.write("Metodo de Runge-Kutta\n")
		f_out.write("y(" + str(t0) + ") = " + str(y0) + "\n")
		f_out.write("h = " + str(h) + "\n")
	lastY = y0
	currentY = lastY

	for step in range (0, qntSteps + 1):
		
		if(ordem == -1):
			f_out.write(str(step) + " " + str(currentY) + "\n")
		pontos.append(currentY)

		k1 = expr.subs([("t", t0) , ("y", float(lastY))])
		k2 = expr.subs([("t", t0 + h / 2) , ("y", float(lastY) + h / 2 * k1)])
		k3 = expr.subs([("t", t0 + h / 2) , ("y", float(lastY) + h / 2 * k2)])
		k4 = expr.subs([("t", t0 + h) , ("y", float(lastY) + h * k3)])

		currentY = lastY + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
		lastY = float(currentY)
		t0 += h
	
	if(ordem == -1):
		f_out.write("\n")	
	return pontos[0:ordem]


def adam_bashforth_2(y0, t0, h, qntSteps, func):
	expr = sympify(func)
	
	ctes = [3/2, -1/2]

	y__1 = float(y0[1])
	y =  float(y0[2])

	f_out.write("y(" + str(t0) + ") = " + str(y__1) + "\n")
	f_out.write("h = " + str(h) + "\n")
	f_out.write("0 " + str(y__1) + "\n")
	f_out.write("1 " + str(y) + "\n")
	for step in range (2, qntSteps + 1):
		
		f = expr.subs([("t", t0 + 1 * h), ("y", y)])
		f__1 = expr.subs([("t", t0), ("y", y__1)])

		y__1 = y
		y = y + h*(				ctes[0] * f + 
											ctes[1] * f__1)
		f_out.write(str(step) + " " + str(y) + "\n")
		t0 += h
	f_out.write("\n")
	return

def adam_bashforth_3(y0, t0, h, qntSteps, func):
	expr = sympify(func)
	
	ctes = [23/12, -4/3, 5/12]

	y__2 = float(y0[0])
	y__1 = float(y0[1])
	y =  float(y0[2])

	f_out.write("y(" + str(t0) + ") = " + str(y__2) + "\n")
	f_out.write("h = " + str(h) + "\n")
	f_out.write("0 " + str(y__2) + "\n")
	f_out.write("1 " + str(y__1) + "\n")
	f_out.write("2 " + str(y) + "\n")
	for step in range (3, qntSteps + 1):
		
		f = expr.subs([("t", t0 + 2 * h), ("y", y)])
		f__1 = expr.subs([("t", t0 + 1 *  h), ("y", y__1)])
		f__2 = expr.subs([("t", t0), ("y", y__2)])

		y__2 = y__1
		y__1 = y
		y = y + h*(				ctes[0] * f + 
											ctes[1] * f__1 +
											ctes[2] * f__2)
		f_out.write(str(step) + " " + str(y) + "\n")
		t0 += h
	f_out.write("\n")
	return

def adam_bashforth_4(y0, t0, h, qntSteps, func):
	expr = sympify(func)
	
	ctes = [55/24, -59/24, 37/24, -3/8]

	y__3 = float(y0[0])
	y__2 = float(y0[1])
	y__1 = float(y0[2])
	y =  float(y0[3])

	f_out.write("y(" + str(t0) + ") = " + str(y__3) + "\n")
	f_out.write("h = " + str(h) + "\n")
	f_out.write("0 " + str(y__3) + "\n")
	f_out.write("1 " + str(y__2) + "\n")
	f_out.write("2 " + str(y__1) + "\n")
	f_out.write("3 " + str(y) + "\n")
	for step in range (4, qntSteps + 1):
		
		f = expr.subs([("t", t0 + 3 * h), ("y", y)])
		f__1 = expr.subs([("t", t0 + 2 *  h), ("y", y__1)])
		f__2 = expr.subs([("t", t0 + 1 * h), ("y", y__2)])
		f__3 = expr.subs([("t", t0), ("y", y__3)])

		y__3 = y__2
		y__2 = y__1
		y__1 = y
		y = y + h*(				ctes[0] * f + 
											ctes[1] * f__1 +
											ctes[2] * f__2 +
											ctes[3] * f__3)
		f_out.write(str(step) + " " + str(y))
		t0 += h
	f_out.write("\n")
	return

def adam_bashforth_5(y0, t0, h, qntSteps, func):
	expr = sympify(func)
	
	ctes = [1901/720, -1387/360, 109/30, -637/360, 251/720]

	y__4 = float(y0[0])
	y__3 = float(y0[1])
	y__2 = float(y0[2])
	y__1 = float(y0[3])
	y =  float(y0[4])

	f_out.write("y(" + str(t0) + ") = " + str(y__4) + "\n")
	f_out.write("h = " + str(h) + "\n")
	f_out.write("0 " + str(y__4) + "\n")
	f_out.write("1 " + str(y__3) + "\n")
	f_out.write("2 " + str(y__2) + "\n")
	f_out.write("3 " + str(y__1) + "\n")
	f_out.write("4 " + str(y) + "\n")
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
		f_out.write(str(step) + " " + str(y)  + "\n")
		t0 += h
	f_out.write("\n")
	return

def adam_bashforth_6(y0, t0, h, qntSteps, func):
	expr = sympify(func)
	
	ctes = [4277/1440, -2641/480, 4991/720, -3649/720, 959/480, -95/288]

	y__5 = float(y0[0])
	y__4 = float(y0[1])
	y__3 = float(y0[2])
	y__2 = float(y0[3])
	y__1 = float(y0[4])
	y =  float(y0[5])

	f_out.write("y(" + str(t0) + ") = " + str(y__5) + "\n")
	f_out.write("h = " + str(h) + "\n")
	f_out.write("0 " + str(y__5) + "\n")
	f_out.write("1 " + str(y__4) + "\n")
	f_out.write("2 " + str(y__3) + "\n")
	f_out.write("3 " + str(y__2) + "\n")
	f_out.write("4 " + str(y__1) + "\n")
	f_out.write("5 " + str(y) + "\n")

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
		f_out.write(str(step) + " " + str(y) + "\n")
		t0 += h
	f_out.write("\n")
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

	f_out.write("y(" + str(t0) + ") = " + str(y__6) + "\n")
	f_out.write("h = " + str(h) + "\n")
	f_out.write("0 " + str(y__6) + "\n")
	f_out.write("1 " + str(y__5) + "\n")
	f_out.write("2 " + str(y__4) + "\n")
	f_out.write("3 " + str(y__3) + "\n")
	f_out.write("4 " + str(y__2) + "\n")
	f_out.write("5 " + str(y__1) + "\n")
	f_out.write("6 " + str(y) + "\n")

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
		f_out.write(str(step) + " " + str(y) + "\n")
		t0 += h
	f_out.write("\n")
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

	f_out.write("y(" + str(t0) + ") = " + str(y__7) + "\n")
	f_out.write("h = " + str(h) + "\n")
	f_out.write("0 " + str(y__7) + "\n")
	f_out.write("1 " + str(y__6) + "\n")
	f_out.write("2 " + str(y__5) + "\n")
	f_out.write("3 " + str(y__4) + "\n")
	f_out.write("4 " + str(y__3) + "\n")
	f_out.write("5 " + str(y__2) + "\n")
	f_out.write("6 " + str(y__1) + "\n")
	f_out.write("7 " + str(y) + "\n")

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
		f_out.write(str(step) + " " + str(y) + "\n")
		t0 += h
	f_out.write("\n")
	return

# Função que chama o metodo de adam bashforth a depender do grau
#
def adam_bashforth(input, printa):
  
	if(printa == True):
		f_out.write("Metodo Adan-Bashforth \n")
	ordem = input[len(input) - 1] 
	if(ordem == "2"):
		adam_bashforth_2(input[0:2], float(input[2]), float(input[3]), int(input[4]), input[5])
	elif(ordem == "3"):
		adam_bashforth_3(input[0:3], float(input[3]), float(input[4]), int(input[5]), input[6])
	elif(ordem == "4"):
		adam_bashforth_4(input[0:4], float(input[4]), float(input[5]), int(input[6]), input[7])
	elif(ordem == "5"):
		adam_bashforth_5(input[0:5], float(input[5]), float(input[6]), int(input[7]), input[8])
	elif(ordem == "6"):
		adam_bashforth_6(input[0:6], float(input[6]), float(input[7]), int(input[8]), input[9])
	elif(ordem == "7"):
		adam_bashforth_7(input[0:7], float(input[7]), float(input[8]), int(input[9]), input[10])
	elif(ordem == "8"):
		adam_bashforth_8(input[0:8], float(input[8]), float(input[9]), int(input[10]), input[11])
	else:
		f_out.write("Out of range\n")

def adam_bashforth_by_euler(y0, t0, h, qntSteps, func, ordem):
  
	retornoEuler = euler(y0, t0, h, qntSteps, func, int(ordem))
	entrada_adam_bashforth = retornoEuler + [t0, h, qntSteps, func, ordem]
	f_out.write("Metodo Adan-Bashforth por Euler\n")
	adam_bashforth(entrada_adam_bashforth, False)
	return

def adam_bashforth_by_euler_inverso(y0, t0, h, qntSteps, func, ordem):
  
	retornoEulerInverso = euler_inverso(y0, t0, h, qntSteps, func, int(ordem))
	entrada_adam_bashforth = retornoEulerInverso + [t0, h, qntSteps, func, ordem]
	f_out.write("Metodo Adan-Bashforth por Euler Inverso\n")
	adam_bashforth(entrada_adam_bashforth, False)
	return

def adam_bashforth_by_euler_aprimorado(y0, t0, h, qntSteps, func, ordem):
  
	retornoEulerAprimorado = euler_aprimorado(y0, t0, h, qntSteps, func, int(ordem))
	entrada_adam_bashforth = retornoEulerAprimorado + [t0, h, qntSteps, func, ordem]
	f_out.write("Metodo Adan-Bashforth por Euler Aprimorado\n")
	adam_bashforth(entrada_adam_bashforth, False)
	return

def adam_bashforth_by_runge_kutta(y0, t0, h, qntSteps, func, ordem):
  
	retornoRunge = runge_kutta(y0, t0, h, qntSteps, func, int(ordem))
	entrada_adam_bashforth = retornoRunge + [t0, h, qntSteps, func, ordem]
	f_out.write("Metodo Adan-Bashforth por Runge-Kutta ( ordem = "+ ordem+ " )\n")
	adam_bashforth(entrada_adam_bashforth, False)
	return

# Adam multon resolvida com solução implicita
def adam_multon_6(y0, t0, h, qntSteps, func):
	expr = sympify(func)
	
	ctes = [19087/60480, 2713/2520, -15487/20160, 586/945, -6737/20160, -95/288]
	ctes = [95/288, 1427/1440, -133/240, 241/720, -173/1440, 3/160]

	y__4 = float(y0[0])
	y__3 = float(y0[1])
	y__2 = float(y0[2])
	y__1 = float(y0[3])
	y =  float(y0[4])

	f_out.write("y(" + str(t0) + ") = " + str(y__4) + "\n")
	f_out.write("h = " + str(h) + "\n")
	f_out.write("0 " + str(y__4) + "\n")
	f_out.write("1 " + str(y__3) + "\n")
	f_out.write("2 " + str(y__2) + "\n")
	f_out.write("3 " + str(y__1) + "\n")
	f_out.write("4 " + str(y) + "\n")

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
		y = y + h*(				ctes[1] * f + 
											ctes[2] * f__1 +
											ctes[3] * f__2 +
											ctes[4] * f__3 +
											ctes[5] * f__4)
		ySymbol = Symbol('y')
		print((expr * h * ctes[0] - ySymbol).subs("t", t0 + 5 * h))
		print(solve((expr * h * ctes[0] - ySymbol).subs("t", t0 + 5 * h), ySymbol))
		y = solve((y + expr * h * ctes[0] -ySymbol).subs("t", t0 + 5 * h), ySymbol)[0]
		f_out.write(str(step) + " " + str(y) + "\n")
		t0 += h
	f_out.write("\n")
	return

def adam_multon_7(y0, t0, h, qntSteps, func):
	expr = sympify(func)
	
	ctes = [19087/60480, 2713/2520, -15487/20160, 586/945, -6737/20160, -95/288]

	y__5 = float(y0[0])
	y__4 = float(y0[1])
	y__3 = float(y0[2])
	y__2 = float(y0[3])
	y__1 = float(y0[4])
	y =  float(y0[5])

	f_out.write("y(" + str(t0) + ") = " + str(y__5) + "\n")
	f_out.write("h = " + str(h) + "\n")
	f_out.write("0 " + str(y__5) + "\n")
	f_out.write("1 " + str(y__4) + "\n")
	f_out.write("2 " + str(y__3) + "\n")
	f_out.write("3 " + str(y__2) + "\n")
	f_out.write("4 " + str(y__1) + "\n")
	f_out.write("5 " + str(y) + "\n")

	for step in range (6, qntSteps + 1):
		
		f = expr.subs([("t", t0 + 5 * h), ("y", y)])
		f__1 = expr.subs([("t", t0 + 4 * h), ("y", y__1)])
		f__2 = expr.subs([("t", t0 + 3 *  h), ("y", y__2)])
		f__3 = expr.subs([("t", t0 + 2 * h), ("y", y__3)])
		f__4 = expr.subs([("t", t0 + 1 * h), ("y", y__4)])
		f__5 = expr.subs([("t", t0 ), ("y", y__5)])

		y__5 = y__4
		y__4 = y__3
		y__3 = y__2
		y__2 = y__1
		y__1 = y
		y = y + h*(				ctes[1] * f + 
											ctes[2] * f__1 +
											ctes[3] * f__2 +
											ctes[4] * f__3 +
											ctes[5] * f__4 +
											ctes[6] * f__5)
		ySymbol = Symbol('y')
		y = solve((y + expr * h * ctes[0] -ySymbol).subs("t", t0 + 6 * h), ySymbol)[0]
		f_out.write(str(step) + " " + str(y) + "\n")
		t0 += h
	f_out.write("\n")
	return



# Função que chama o metodo de adam bashforth a depender do grau
def adam_multon(input, printa):
  
	if(printa == True):
		f_out.write("Metodo Adan-Multon \n")
	ordem = input[len(input) - 1] 
	if(ordem == "2"):
		adam_multon_2(input[0:1], float(input[1]), float(input[2]), int(input[3]), input[4])
	elif(ordem == "3"):
		adam_multon_3(input[0:2], float(input[2]), float(input[3]), int(input[4]), input[5])
	elif(ordem == "4"):
		adam_multon_4(input[0:3], float(input[3]), float(input[4]), int(input[5]), input[6])
	elif(ordem == "5"):
		adam_multon_5(input[0:4], float(input[4]), float(input[5]), int(input[6]), input[7])
	elif(ordem == "6"):
		adam_multon_6(input[0:5], float(input[5]), float(input[6]), int(input[7]), input[8])
	elif(ordem == "7"):
		adam_multon_7(input[0:6], float(input[6]), float(input[7]), int(input[8]), input[9])
	elif(ordem == "8"):
		adam_multon_8(input[0:7], float(input[7]), float(input[8]), int(input[9]), input[10])
	else:
		f_out.write("Out of range\n")
	
def main():
	readFile('entradas.txt')

def readFile(path):
  		
	with open(path) as f:
		for line in f:
			inputs = line.split()
			if(inputs[0] == 'euler'):
				euler(float(inputs[1]), float(inputs[2]), float(inputs[3]), int(inputs[4]), inputs[5], -1)
			elif(inputs[0] == 'euler_inverso'):
				euler_inverso(float(inputs[1]), float(inputs[2]), float(inputs[3]), int(inputs[4]), inputs[5], -1)
			elif(inputs[0] == 'euler_aprimorado'):
				euler_aprimorado(float(inputs[1]), float(inputs[2]), float(inputs[3]), int(inputs[4]), inputs[5], -1)
			elif(inputs[0] == 'runge_kutta'):
				runge_kutta(float(inputs[1]), float(inputs[2]), float(inputs[3]), int(inputs[4]), inputs[5], -1)
			elif(inputs[0] == 'adam_bashforth'):
				adam_bashforth(inputs[1:], True)
			elif(inputs[0] == 'adam_bashforth_by_euler'):
				adam_bashforth_by_euler(float(inputs[1]), float(inputs[2]), float(inputs[3]), int(inputs[4]), inputs[5], inputs[6])
			elif(inputs[0] == 'adam_bashforth_by_euler_inverso'):
				adam_bashforth_by_euler_inverso(float(inputs[1]), float(inputs[2]), float(inputs[3]), int(inputs[4]), inputs[5], inputs[6])
			elif(inputs[0] == 'adam_bashforth_by_euler_aprimorado'):
				adam_bashforth_by_euler_aprimorado(float(inputs[1]), float(inputs[2]), float(inputs[3]), int(inputs[4]), inputs[5], inputs[6])
			elif(inputs[0] == 'adam_bashforth_by_runge_kutta'):
				adam_bashforth_by_runge_kutta(float(inputs[1]), float(inputs[2]), float(inputs[3]), int(inputs[4]), inputs[5], inputs[6])
			elif(inputs[0] == 'adam_multon'):
				adam_multon(inputs[1:], True)
	f_out.close()
main()