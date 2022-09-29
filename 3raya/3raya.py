#para ejecutar: python E:\PythonLearning\3rayas.py
import time
import os

def clear():
	os.system("cls")
def main():
	clear()
	print ("Bienvenido al juego que no puedes ganar.")
	asdadadadsafdkjfkljflk = input (" ")
	
	clear()
	print("¿O sí?")
	asddsajkdjhaslkdjhasls = input (" ")

	clear()
	print("Funcionamiento:")
	print("Cuándo te lo indique el juego, escoge la casilla a llenar escribiendo el número de fila seguido del número de columna sin ningún tipo de separación entre ellos y pulsa enter.")
	print("")
	print("Ejemplo:")
	print("Para marcar la esquina superior derecha (fila 1, columna 3) escribiría 13 y pulsaría enter.")
	asddsajkdjhaslkdjhasls = input (" ")

	clear()
	x11 = " "
	x12 = " "
	x13 = " "
	x21 = " "
	x22 = " "
	x23 = " "
	x31 = " "
	x32 = " "
	x33 = " "
	zero_line = ["    1    2    3 "]
	first_line 	= [1,(x11,x12,x13)]
	second_line = [2,(x21,x22,x23)]
	third_line 	= [3,(x31,x32,x33)]
	print(zero_line)
	print(first_line)
	print(second_line)
	print(third_line)
	time.sleep(1)

	clear()
	x31 = "x"
	zero_line = ["    1    2    3 "]
	first_line 	= [1,(x11,x12,x13)]
	second_line = [2,(x21,x22,x23)]
	third_line 	= [3,(x31,x32,x33)]
	print(zero_line)
	print(first_line)
	print(second_line)
	print(third_line)
	respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
	
	while respuesta:
		if respuesta == 11:
			if x11 == " ":
				x11 = "o"
				break
			else:
				print ("Casilla ocupada, prueba otra vez")
		if respuesta == 12:
			if x12 == " ":
				x12 = "o"
				break
			else:
				print ("Casilla ocupada, prueba otra vez")
		if respuesta == 13:
			if x13 == " ":
				x13 = "o"
				break
			else:
				print ("Casilla ocupada, prueba otra vez")
		if respuesta == 21:
			if x21 == " ":
				x21 = "o"
				break
			else:
				print ("Casilla ocupada, prueba otra vez")
		if respuesta == 22:
			if x22 == " ":
				x22 = "o"
				break
			else:
				print ("Casilla ocupada, prueba otra vez")
		if respuesta == 23:
			if x23 == " ":
				x23 = "o"
				break
			else:
				print ("Casilla ocupada, prueba otra vez")
		if respuesta == 31:
			print ("Casilla ocupada, prueba otra vez")
		if respuesta == 32:
			if x32 == " ":
				x32 = "o"
				break
			else:
				print ("Casilla ocupada, prueba otra vez")
		if respuesta == 33:
			if x33 == " ":
				x33 = "o"
				break
			else:
				print ("Casilla ocupada, prueba otra vez")												
		respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))

	clear()
	zero_line = ["    1    2    3 "]
	first_line 	= [1,(x11,x12,x13)]
	second_line = [2,(x21,x22,x23)]
	third_line 	= [3,(x31,x32,x33)]
	print(zero_line)
	print(first_line)
	print(second_line)
	print(third_line)
	time.sleep(1)









































	if x22 == "o":
		x13 = "x"
		clear()
		zero_line = ["    1    2    3 "]
		first_line 	= [1,(x11,x12,x13)]
		second_line = [2,(x21,x22,x23)]
		third_line 	= [3,(x31,x32,x33)]
		print(zero_line)
		print(first_line)
		print(second_line)
		print(third_line)
		respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
		while respuesta:
			if respuesta == 11:
				if x11 == " ":
					x11 = "o"
					break
				else:
					print ("Casilla ocupada, prueba otra vez")
			if respuesta == 12:
				if x12 == " ":
					x12 = "o"
					break
				else:
					print ("Casilla ocupada, prueba otra vez")
			if respuesta == 13:
				if x13 == " ":
					x13 = "o"
					break
				else:
					print ("Casilla ocupada, prueba otra vez")
			if respuesta == 21:
				if x21 == " ":
					x21 = "o"
					break
				else:
					print ("Casilla ocupada, prueba otra vez")
			if respuesta == 22:
				if x22 == " ":
					x22 = "o"
					break
				else:
					print ("Casilla ocupada, prueba otra vez")
			if respuesta == 23:
				if x23 == " ":
					x23 = "o"
					break
				else:
					print ("Casilla ocupada, prueba otra vez")
			if respuesta == 31:
				print ("Casilla ocupada, prueba otra vez")
			if respuesta == 32:
				if x32 == " ":
					x32 = "o"
					break
				else:
					print ("Casilla ocupada, prueba otra vez")
			if respuesta == 33:
				if x33 == " ":
					x33 = "o"
					break
				else:
					print ("Casilla ocupada, prueba otra vez")												
			respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
		clear()
		zero_line = ["    1    2    3 "]
		first_line 	= [1,(x11,x12,x13)]
		second_line = [2,(x21,x22,x23)]
		third_line 	= [3,(x31,x32,x33)]
		print(zero_line)
		print(first_line)
		print(second_line)
		print(third_line)
		time.sleep(1)
		if x12 == "o":
			x32 = "x"
			clear()
			zero_line = ["    1    2    3 "]
			first_line 	= [1,(x11,x12,x13)]
			second_line = [2,(x21,x22,x23)]
			third_line 	= [3,(x31,x32,x33)]
			print(zero_line)
			print(first_line)
			print(second_line)
			print(third_line)
			respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
			while respuesta:
				if respuesta == 11:
					if x11 == " ":
						x11 = "o"
						break
					else:
						print ("Casilla ocupada, prueba otra vez")
				if respuesta == 12:
					if x12 == " ":
						x12 = "o"
						break
					else:
						print ("Casilla ocupada, prueba otra vez")
				if respuesta == 13:
					if x13 == " ":
						x13 = "o"
						break
					else:
						print ("Casilla ocupada, prueba otra vez")
				if respuesta == 21:
					if x21 == " ":
						x21 = "o"
						break
					else:
						print ("Casilla ocupada, prueba otra vez")
				if respuesta == 22:
					if x22 == " ":
						x22 = "o"
						break
					else:
						print ("Casilla ocupada, prueba otra vez")
				if respuesta == 23:
					if x23 == " ":
						x23 = "o"
						break
					else:
						print ("Casilla ocupada, prueba otra vez")
				if respuesta == 31:
					print ("Casilla ocupada, prueba otra vez")
				if respuesta == 32:
					if x32 == " ":
						x32 = "o"
						break
					else:
						print ("Casilla ocupada, prueba otra vez")
				if respuesta == 33:
					if x33 == " ":
						x33 = "o"
						break
					else:
						print ("Casilla ocupada, prueba otra vez")												
				respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
			clear()
			zero_line = ["    1    2    3 "]
			first_line 	= [1,(x11,x12,x13)]
			second_line = [2,(x21,x22,x23)]
			third_line 	= [3,(x31,x32,x33)]
			print(zero_line)
			print(first_line)
			print(second_line)
			print(third_line)
			time.sleep(1)
			if x33 == " ":
				x33 = "x"
				clear()
				zero_line = ["    1    2    3 "]
				first_line 	= [1,(x11,x12,x13)]
				second_line = [2,(x21,x22,x23)]
				third_line 	= [3,(x31,x32,x33)]
				print(zero_line)
				print(first_line)
				print(second_line)
				print(third_line)
				print("¡Has perdido!\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a")
				dksajldkajsda = input(" ")
								
			else:
				x11 = "x"
				clear()
				zero_line = ["    1    2    3 "]
				first_line 	= [1,(x11,x12,x13)]
				second_line = [2,(x21,x22,x23)]
				third_line 	= [3,(x31,x32,x33)]
				print(zero_line)
				print(first_line)
				print(second_line)
				print(third_line)
				respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
				while respuesta:
					if respuesta == 11:
						if x11 == " ":
							x11 = "o"
							break
						else:
							print ("Casilla ocupada, prueba otra vez")
					if respuesta == 12:
						if x12 == " ":
							x12 = "o"
							break
						else:
							print ("Casilla ocupada, prueba otra vez")
					if respuesta == 13:
						if x13 == " ":
							x13 = "o"
							break
						else:
							print ("Casilla ocupada, prueba otra vez")
					if respuesta == 21:
						if x21 == " ":
							x21 = "o"
							break
						else:
							print ("Casilla ocupada, prueba otra vez")
					if respuesta == 22:
						if x22 == " ":
							x22 = "o"
							break
						else:
							print ("Casilla ocupada, prueba otra vez")
					if respuesta == 23:
						if x23 == " ":
							x23 = "o"
							break
						else:
							print ("Casilla ocupada, prueba otra vez")
					if respuesta == 31:
						print ("Casilla ocupada, prueba otra vez")
					if respuesta == 32:
						if x32 == " ":
							x32 = "o"
							break
						else:
							print ("Casilla ocupada, prueba otra vez")
					if respuesta == 33:
						if x33 == " ":
							x33 = "o"
							break
						else:
							print ("Casilla ocupada, prueba otra vez")												
					respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
				clear()
				zero_line = ["    1    2    3 "]
				first_line 	= [1,(x11,x12,x13)]
				second_line = [2,(x21,x22,x23)]
				third_line 	= [3,(x31,x32,x33)]
				print(zero_line)
				print(first_line)
				print(second_line)
				print(third_line)
				time.sleep(1)
				if x21 == " ":
					x21 = "x"
					clear()
					zero_line = ["    1    2    3 "]
					first_line 	= [1,(x11,x12,x13)]
					second_line = [2,(x21,x22,x23)]
					third_line 	= [3,(x31,x32,x33)]
					print(zero_line)
					print(first_line)
					print(second_line)
					print(third_line)
					print("¡Has perdido!\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a")
					dksajldkajsda = input(" ")

									
				else:
					x23 = "x"
					clear()
					zero_line = ["    1    2    3 "]
					first_line 	= [1,(x11,x12,x13)]
					second_line = [2,(x21,x22,x23)]
					third_line 	= [3,(x31,x32,x33)]
					print(zero_line)
					print(first_line)
					print(second_line)
					print(third_line)
					print("¡Empate, vuelve a intentarlo!")
					dksajldkajsda = input(" ")

		else:
			if x21 == "o":
				x23 = "x"
				clear()
				zero_line = ["    1    2    3 "]
				first_line 	= [1,(x11,x12,x13)]
				second_line = [2,(x21,x22,x23)]
				third_line 	= [3,(x31,x32,x33)]
				print(zero_line)
				print(first_line)
				print(second_line)
				print(third_line)
				respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
				while respuesta:
					if respuesta == 11:
						if x11 == " ":
							x11 = "o"
							break
						else:
							print ("Casilla ocupada, prueba otra vez")
					if respuesta == 12:
						if x12 == " ":
							x12 = "o"
							break
						else:
							print ("Casilla ocupada, prueba otra vez")
					if respuesta == 13:
						if x13 == " ":
							x13 = "o"
							break
						else:
							print ("Casilla ocupada, prueba otra vez")
					if respuesta == 21:
						if x21 == " ":
							x21 = "o"
							break
						else:
							print ("Casilla ocupada, prueba otra vez")
					if respuesta == 22:
						if x22 == " ":
							x22 = "o"
							break
						else:
							print ("Casilla ocupada, prueba otra vez")
					if respuesta == 23:
						if x23 == " ":
							x23 = "o"
							break
						else:
							print ("Casilla ocupada, prueba otra vez")
					if respuesta == 31:
						print ("Casilla ocupada, prueba otra vez")
					if respuesta == 32:
						if x32 == " ":
							x32 = "o"
							break
						else:
							print ("Casilla ocupada, prueba otra vez")
					if respuesta == 33:
						if x33 == " ":
							x33 = "o"
							break
						else:
							print ("Casilla ocupada, prueba otra vez")												
					respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
				clear()
				zero_line = ["    1    2    3 "]
				first_line 	= [1,(x11,x12,x13)]
				second_line = [2,(x21,x22,x23)]
				third_line 	= [3,(x31,x32,x33)]
				print(zero_line)
				print(first_line)
				print(second_line)
				print(third_line)
				time.sleep(1)
				if x33 == " ":
					x33 = "x"
					clear()
					zero_line = ["    1    2    3 "]
					first_line 	= [1,(x11,x12,x13)]
					second_line = [2,(x21,x22,x23)]
					third_line 	= [3,(x31,x32,x33)]
					print(zero_line)
					print(first_line)
					print(second_line)
					print(third_line)
					print("¡Has perdido!\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a")
					dksajldkajsda = input(" ")
									
				else:
					x11 = "x"
					clear()
					zero_line = ["    1    2    3 "]
					first_line 	= [1,(x11,x12,x13)]
					second_line = [2,(x21,x22,x23)]
					third_line 	= [3,(x31,x32,x33)]
					print(zero_line)
					print(first_line)
					print(second_line)
					print(third_line)
					respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
					while respuesta:
						if respuesta == 11:
							if x11 == " ":
								x11 = "o"
								break
							else:
								print ("Casilla ocupada, prueba otra vez")
						if respuesta == 12:
							if x12 == " ":
								x12 = "o"
								break
							else:
								print ("Casilla ocupada, prueba otra vez")
						if respuesta == 13:
							if x13 == " ":
								x13 = "o"
								break
							else:
								print ("Casilla ocupada, prueba otra vez")
						if respuesta == 21:
							if x21 == " ":
								x21 = "o"
								break
							else:
								print ("Casilla ocupada, prueba otra vez")
						if respuesta == 22:
							if x22 == " ":
								x22 = "o"
								break
							else:
								print ("Casilla ocupada, prueba otra vez")
						if respuesta == 23:
							if x23 == " ":
								x23 = "o"
								break
							else:
								print ("Casilla ocupada, prueba otra vez")
						if respuesta == 31:
							print ("Casilla ocupada, prueba otra vez")
						if respuesta == 32:
							if x32 == " ":
								x32 = "o"
								break
							else:
								print ("Casilla ocupada, prueba otra vez")
						if respuesta == 33:
							if x33 == " ":
								x33 = "o"
								break
							else:
								print ("Casilla ocupada, prueba otra vez")												
						respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
					clear()
					zero_line = ["    1    2    3 "]
					first_line 	= [1,(x11,x12,x13)]
					second_line = [2,(x21,x22,x23)]
					third_line 	= [3,(x31,x32,x33)]
					print(zero_line)
					print(first_line)
					print(second_line)
					print(third_line)
					time.sleep(1)
					if x12 == " ":
						x12 = "x"
						clear()
						zero_line = ["    1    2    3 "]
						first_line 	= [1,(x11,x12,x13)]
						second_line = [2,(x21,x22,x23)]
						third_line 	= [3,(x31,x32,x33)]
						print(zero_line)
						print(first_line)
						print(second_line)
						print(third_line)
						print("¡Has perdido!\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a")
						dksajldkajsda = input(" ")

										
					else:
						x32 = "x"
						clear()
						zero_line = ["    1    2    3 "]
						first_line 	= [1,(x11,x12,x13)]
						second_line = [2,(x21,x22,x23)]
						third_line 	= [3,(x31,x32,x33)]
						print(zero_line)
						print(first_line)
						print(second_line)
						print(third_line)
						print("¡Empate, vuelve a intentarlo!")
						dksajldkajsda = input(" ")
			else:
				if x23 == "o":
					x21 = "x"
					clear()
					zero_line = ["    1    2    3 "]
					first_line 	= [1,(x11,x12,x13)]
					second_line = [2,(x21,x22,x23)]
					third_line 	= [3,(x31,x32,x33)]
					print(zero_line)
					print(first_line)
					print(second_line)
					print(third_line)
					respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
					while respuesta:
						if respuesta == 11:
							if x11 == " ":
								x11 = "o"
								break
							else:
								print ("Casilla ocupada, prueba otra vez")
						if respuesta == 12:
							if x12 == " ":
								x12 = "o"
								break
							else:
								print ("Casilla ocupada, prueba otra vez")
						if respuesta == 13:
							if x13 == " ":
								x13 = "o"
								break
							else:
								print ("Casilla ocupada, prueba otra vez")
						if respuesta == 21:
							if x21 == " ":
								x21 = "o"
								break
							else:
								print ("Casilla ocupada, prueba otra vez")
						if respuesta == 22:
							if x22 == " ":
								x22 = "o"
								break
							else:
								print ("Casilla ocupada, prueba otra vez")
						if respuesta == 23:
							if x23 == " ":
								x23 = "o"
								break
							else:
								print ("Casilla ocupada, prueba otra vez")
						if respuesta == 31:
							print ("Casilla ocupada, prueba otra vez")
						if respuesta == 32:
							if x32 == " ":
								x32 = "o"
								break
							else:
								print ("Casilla ocupada, prueba otra vez")
						if respuesta == 33:
							if x33 == " ":
								x33 = "o"
								break
							else:
								print ("Casilla ocupada, prueba otra vez")												
						respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
					clear()
					zero_line = ["    1    2    3 "]
					first_line 	= [1,(x11,x12,x13)]
					second_line = [2,(x21,x22,x23)]
					third_line 	= [3,(x31,x32,x33)]
					print(zero_line)
					print(first_line)
					print(second_line)
					print(third_line)
					time.sleep(1)
					if x11 == " ":
						x11 = "x"
						clear()
						zero_line = ["    1    2    3 "]
						first_line 	= [1,(x11,x12,x13)]
						second_line = [2,(x21,x22,x23)]
						third_line 	= [3,(x31,x32,x33)]
						print(zero_line)
						print(first_line)
						print(second_line)
						print(third_line)
						print("¡Has perdido!\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a")
						dksajldkajsda = input(" ")
										
					else:
						x33 = "x"
						clear()
						zero_line = ["    1    2    3 "]
						first_line 	= [1,(x11,x12,x13)]
						second_line = [2,(x21,x22,x23)]
						third_line 	= [3,(x31,x32,x33)]
						print(zero_line)
						print(first_line)
						print(second_line)
						print(third_line)
						respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
						while respuesta:
							if respuesta == 11:
								if x11 == " ":
									x11 = "o"
									break
								else:
									print ("Casilla ocupada, prueba otra vez")
							if respuesta == 12:
								if x12 == " ":
									x12 = "o"
									break
								else:
									print ("Casilla ocupada, prueba otra vez")
							if respuesta == 13:
								if x13 == " ":
									x13 = "o"
									break
								else:
									print ("Casilla ocupada, prueba otra vez")
							if respuesta == 21:
								if x21 == " ":
									x21 = "o"
									break
								else:
									print ("Casilla ocupada, prueba otra vez")
							if respuesta == 22:
								if x22 == " ":
									x22 = "o"
									break
								else:
									print ("Casilla ocupada, prueba otra vez")
							if respuesta == 23:
								if x23 == " ":
									x23 = "o"
									break
								else:
									print ("Casilla ocupada, prueba otra vez")
							if respuesta == 31:
								print ("Casilla ocupada, prueba otra vez")
							if respuesta == 32:
								if x32 == " ":
									x32 = "o"
									break
								else:
									print ("Casilla ocupada, prueba otra vez")
							if respuesta == 33:
								if x33 == " ":
									x33 = "o"
									break
								else:
									print ("Casilla ocupada, prueba otra vez")												
							respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
						clear()
						zero_line = ["    1    2    3 "]
						first_line 	= [1,(x11,x12,x13)]
						second_line = [2,(x21,x22,x23)]
						third_line 	= [3,(x31,x32,x33)]
						print(zero_line)
						print(first_line)
						print(second_line)
						print(third_line)
						time.sleep(1)
						if x32 == " ":
							x32 = "x"
							clear()
							zero_line = ["    1    2    3 "]
							first_line 	= [1,(x11,x12,x13)]
							second_line = [2,(x21,x22,x23)]
							third_line 	= [3,(x31,x32,x33)]
							print(zero_line)
							print(first_line)
							print(second_line)
							print(third_line)
							print("¡Has perdido!\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a")
							dksajldkajsda = input(" ")

											
						else:
							x12 = "x"
							clear()
							zero_line = ["    1    2    3 "]
							first_line 	= [1,(x11,x12,x13)]
							second_line = [2,(x21,x22,x23)]
							third_line 	= [3,(x31,x32,x33)]
							print(zero_line)
							print(first_line)
							print(second_line)
							print(third_line)
							print("¡Empate, vuelve a intentarlo!")
							dksajldkajsda = input(" ")
				else:
					if x32 == "o":
						x12 = "x"
						clear()
						zero_line = ["    1    2    3 "]
						first_line 	= [1,(x11,x12,x13)]
						second_line = [2,(x21,x22,x23)]
						third_line 	= [3,(x31,x32,x33)]
						print(zero_line)
						print(first_line)
						print(second_line)
						print(third_line)
						respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
						while respuesta:
							if respuesta == 11:
								if x11 == " ":
									x11 = "o"
									break
								else:
									print ("Casilla ocupada, prueba otra vez")
							if respuesta == 12:
								if x12 == " ":
									x12 = "o"
									break
								else:
									print ("Casilla ocupada, prueba otra vez")
							if respuesta == 13:
								if x13 == " ":
									x13 = "o"
									break
								else:
									print ("Casilla ocupada, prueba otra vez")
							if respuesta == 21:
								if x21 == " ":
									x21 = "o"
									break
								else:
									print ("Casilla ocupada, prueba otra vez")
							if respuesta == 22:
								if x22 == " ":
									x22 = "o"
									break
								else:
									print ("Casilla ocupada, prueba otra vez")
							if respuesta == 23:
								if x23 == " ":
									x23 = "o"
									break
								else:
									print ("Casilla ocupada, prueba otra vez")
							if respuesta == 31:
								print ("Casilla ocupada, prueba otra vez")
							if respuesta == 32:
								if x32 == " ":
									x32 = "o"
									break
								else:
									print ("Casilla ocupada, prueba otra vez")
							if respuesta == 33:
								if x33 == " ":
									x33 = "o"
									break
								else:
									print ("Casilla ocupada, prueba otra vez")												
							respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
						clear()
						zero_line = ["    1    2    3 "]
						first_line 	= [1,(x11,x12,x13)]
						second_line = [2,(x21,x22,x23)]
						third_line 	= [3,(x31,x32,x33)]
						print(zero_line)
						print(first_line)
						print(second_line)
						print(third_line)
						time.sleep(1)
						if x11 == " ":
							x11 = "x"
							clear()
							zero_line = ["    1    2    3 "]
							first_line 	= [1,(x11,x12,x13)]
							second_line = [2,(x21,x22,x23)]
							third_line 	= [3,(x31,x32,x33)]
							print(zero_line)
							print(first_line)
							print(second_line)
							print(third_line)
							print("¡Has perdido!\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a")
							dksajldkajsda = input(" ")
											
						else:
							x33 = "x"
							clear()
							zero_line = ["    1    2    3 "]
							first_line 	= [1,(x11,x12,x13)]
							second_line = [2,(x21,x22,x23)]
							third_line 	= [3,(x31,x32,x33)]
							print(zero_line)
							print(first_line)
							print(second_line)
							print(third_line)
							respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
							while respuesta:
								if respuesta == 11:
									if x11 == " ":
										x11 = "o"
										break
									else:
										print ("Casilla ocupada, prueba otra vez")
								if respuesta == 12:
									if x12 == " ":
										x12 = "o"
										break
									else:
										print ("Casilla ocupada, prueba otra vez")
								if respuesta == 13:
									if x13 == " ":
										x13 = "o"
										break
									else:
										print ("Casilla ocupada, prueba otra vez")
								if respuesta == 21:
									if x21 == " ":
										x21 = "o"
										break
									else:
										print ("Casilla ocupada, prueba otra vez")
								if respuesta == 22:
									if x22 == " ":
										x22 = "o"
										break
									else:
										print ("Casilla ocupada, prueba otra vez")
								if respuesta == 23:
									if x23 == " ":
										x23 = "o"
										break
									else:
										print ("Casilla ocupada, prueba otra vez")
								if respuesta == 31:
									print ("Casilla ocupada, prueba otra vez")
								if respuesta == 32:
									if x32 == " ":
										x32 = "o"
										break
									else:
										print ("Casilla ocupada, prueba otra vez")
								if respuesta == 33:
									if x33 == " ":
										x33 = "o"
										break
									else:
										print ("Casilla ocupada, prueba otra vez")												
								respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
							clear()
							zero_line = ["    1    2    3 "]
							first_line 	= [1,(x11,x12,x13)]
							second_line = [2,(x21,x22,x23)]
							third_line 	= [3,(x31,x32,x33)]
							print(zero_line)
							print(first_line)
							print(second_line)
							print(third_line)
							time.sleep(1)
							if x23 == " ":
								x23 = "x"
								clear()
								zero_line = ["    1    2    3 "]
								first_line 	= [1,(x11,x12,x13)]
								second_line = [2,(x21,x22,x23)]
								third_line 	= [3,(x31,x32,x33)]
								print(zero_line)
								print(first_line)
								print(second_line)
								print(third_line)
								print("¡Has perdido!\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a")
								dksajldkajsda = input(" ")

												
							else:
								x21 = "x"
								clear()
								zero_line = ["    1    2    3 "]
								first_line 	= [1,(x11,x12,x13)]
								second_line = [2,(x21,x22,x23)]
								third_line 	= [3,(x31,x32,x33)]
								print(zero_line)
								print(first_line)
								print(second_line)
								print(third_line)
								print("¡Empate, vuelve a intentarlo!")
								dksajldkajsda = input(" ")
					else:
						if x11 == "o":
							x33 = "x"
							clear()
							zero_line = ["    1    2    3 "]
							first_line 	= [1,(x11,x12,x13)]
							second_line = [2,(x21,x22,x23)]
							third_line 	= [3,(x31,x32,x33)]
							print(zero_line)
							print(first_line)
							print(second_line)
							print(third_line)
							respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
							while respuesta:
								if respuesta == 11:
									if x11 == " ":
										x11 = "o"
										break
									else:
										print ("Casilla ocupada, prueba otra vez")
								if respuesta == 12:
									if x12 == " ":
										x12 = "o"
										break
									else:
										print ("Casilla ocupada, prueba otra vez")
								if respuesta == 13:
									if x13 == " ":
										x13 = "o"
										break
									else:
										print ("Casilla ocupada, prueba otra vez")
								if respuesta == 21:
									if x21 == " ":
										x21 = "o"
										break
									else:
										print ("Casilla ocupada, prueba otra vez")
								if respuesta == 22:
									if x22 == " ":
										x22 = "o"
										break
									else:
										print ("Casilla ocupada, prueba otra vez")
								if respuesta == 23:
									if x23 == " ":
										x23 = "o"
										break
									else:
										print ("Casilla ocupada, prueba otra vez")
								if respuesta == 31:
									print ("Casilla ocupada, prueba otra vez")
								if respuesta == 32:
									if x32 == " ":
										x32 = "o"
										break
									else:
										print ("Casilla ocupada, prueba otra vez")
								if respuesta == 33:
									if x33 == " ":
										x33 = "o"
										break
									else:
										print ("Casilla ocupada, prueba otra vez")												
								respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
							clear()
							zero_line = ["    1    2    3 "]
							first_line 	= [1,(x11,x12,x13)]
							second_line = [2,(x21,x22,x23)]
							third_line 	= [3,(x31,x32,x33)]
							print(zero_line)
							print(first_line)
							print(second_line)
							print(third_line)
							time.sleep(1)
							if x23 == " ":
									x23 = "x"
									time.sleep(1)
									clear()
									zero_line = ["    1    2    3 "]
									first_line 	= [1,(x11,x12,x13)]
									second_line = [2,(x21,x22,x23)]
									third_line 	= [3,(x31,x32,x33)]
									print(zero_line)
									print(first_line)
									print(second_line)
									print(third_line)
									
									
							else:
								x32 = "x"
								time.sleep(1)
								clear()
								zero_line = ["    1    2    3 "]
								first_line 	= [1,(x11,x12,x13)]
								second_line = [2,(x21,x22,x23)]
								third_line 	= [3,(x31,x32,x33)]
								print(zero_line)
								print(first_line)
								print(second_line)
								print(third_line)
						
						else:
							if x33 == "o":
								x11 = "x"
								clear()
								zero_line = ["    1    2    3 "]
								first_line 	= [1,(x11,x12,x13)]
								second_line = [2,(x21,x22,x23)]
								third_line 	= [3,(x31,x32,x33)]
								print(zero_line)
								print(first_line)
								print(second_line)
								print(third_line)
								respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
								while respuesta:
									if respuesta == 11:
										if x11 == " ":
											x11 = "o"
											break
										else:
											print ("Casilla ocupada, prueba otra vez")
									if respuesta == 12:
										if x12 == " ":
											x12 = "o"
											break
										else:
											print ("Casilla ocupada, prueba otra vez")
									if respuesta == 13:
										if x13 == " ":
											x13 = "o"
											break
										else:
											print ("Casilla ocupada, prueba otra vez")
									if respuesta == 21:
										if x21 == " ":
											x21 = "o"
											break
										else:
											print ("Casilla ocupada, prueba otra vez")
									if respuesta == 22:
										if x22 == " ":
											x22 = "o"
											break
										else:
											print ("Casilla ocupada, prueba otra vez")
									if respuesta == 23:
										if x23 == " ":
											x23 = "o"
											break
										else:
											print ("Casilla ocupada, prueba otra vez")
									if respuesta == 31:
										print ("Casilla ocupada, prueba otra vez")
									if respuesta == 32:
										if x32 == " ":
											x32 = "o"
											break
										else:
											print ("Casilla ocupada, prueba otra vez")
									if respuesta == 33:
										if x33 == " ":
											x33 = "o"
											break
										else:
											print ("Casilla ocupada, prueba otra vez")												
									respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
								clear()
								zero_line = ["    1    2    3 "]
								first_line 	= [1,(x11,x12,x13)]
								second_line = [2,(x21,x22,x23)]
								third_line 	= [3,(x31,x32,x33)]
								print(zero_line)
								print(first_line)
								print(second_line)
								print(third_line)
								time.sleep(1)
								if x21 == " ":
										x21 = "x"
										time.sleep(1)
										clear()
										zero_line = ["    1    2    3 "]
										first_line 	= [1,(x11,x12,x13)]
										second_line = [2,(x21,x22,x23)]
										third_line 	= [3,(x31,x32,x33)]
										print(zero_line)
										print(first_line)
										print(second_line)
										print(third_line)
										
										
								else:
									x12 = "x"
									time.sleep(1)
									clear()
									zero_line = ["    1    2    3 "]
									first_line 	= [1,(x11,x12,x13)]
									second_line = [2,(x21,x22,x23)]
									third_line 	= [3,(x31,x32,x33)]
									print(zero_line)
									print(first_line)
									print(second_line)
									print(third_line)
						print("¡Has perdido!\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a")
						dksajldkajsda = input(" ")


			
				
				

	
















































	else:
		if x11 == "o":
			x33 = "x"
			clear()
			zero_line = ["    1    2    3 "]
			first_line 	= [1,(x11,x12,x13)]
			second_line = [2,(x21,x22,x23)]
			third_line 	= [3,(x31,x32,x33)]
			print(zero_line)
			print(first_line)
			print(second_line)
			print(third_line)
			respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
			while respuesta:
				if respuesta == 11:
					if x11 == " ":
						x11 = "o"
						break
					else:
						print ("Casilla ocupada, prueba otra vez")
				if respuesta == 12:
					if x12 == " ":
						x12 = "o"
						break
					else:
						print ("Casilla ocupada, prueba otra vez")
				if respuesta == 13:
					if x13 == " ":
						x13 = "o"
						break
					else:
						print ("Casilla ocupada, prueba otra vez")
				if respuesta == 21:
					if x21 == " ":
						x21 = "o"
						break
					else:
						print ("Casilla ocupada, prueba otra vez")
				if respuesta == 22:
					if x22 == " ":
						x22 = "o"
						break
					else:
						print ("Casilla ocupada, prueba otra vez")
				if respuesta == 23:
					if x23 == " ":
						x23 = "o"
						break
					else:
						print ("Casilla ocupada, prueba otra vez")
				if respuesta == 31:
					print ("Casilla ocupada, prueba otra vez")
				if respuesta == 32:
					if x32 == " ":
						x32 = "o"
						break
					else:
						print ("Casilla ocupada, prueba otra vez")
				if respuesta == 33:
					if x33 == " ":
						x33 = "o"
						break
					else:
						print ("Casilla ocupada, prueba otra vez")												
				respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
			clear()
			zero_line = ["    1    2    3 "]
			first_line 	= [1,(x11,x12,x13)]
			second_line = [2,(x21,x22,x23)]
			third_line 	= [3,(x31,x32,x33)]
			print(zero_line)
			print(first_line)
			print(second_line)
			print(third_line)
			time.sleep(1)
			if x32 == " ":
				x32 = "x"
				clear()
				zero_line = ["    1    2    3 "]
				first_line 	= [1,(x11,x12,x13)]
				second_line = [2,(x21,x22,x23)]
				third_line 	= [3,(x31,x32,x33)]
				print(zero_line)
				print(first_line)
				print(second_line)
				print(third_line)
				
				
			else:
				x13 = "x"
				clear()
				zero_line = ["    1    2    3 "]
				first_line 	= [1,(x11,x12,x13)]
				second_line = [2,(x21,x22,x23)]
				third_line 	= [3,(x31,x32,x33)]
				print(zero_line)
				print(first_line)
				print(second_line)
				print(third_line)
				respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
				while respuesta:
					if respuesta == 11:
						if x11 == " ":
							x11 = "o"
							break
						else:
							print ("Casilla ocupada, prueba otra vez")
					if respuesta == 12:
						if x12 == " ":
							x12 = "o"
							break
						else:
							print ("Casilla ocupada, prueba otra vez")
					if respuesta == 13:
						if x13 == " ":
							x13 = "o"
							break
						else:
							print ("Casilla ocupada, prueba otra vez")
					if respuesta == 21:
						if x21 == " ":
							x21 = "o"
							break
						else:
							print ("Casilla ocupada, prueba otra vez")
					if respuesta == 22:
						if x22 == " ":
							x22 = "o"
							break
						else:
							print ("Casilla ocupada, prueba otra vez")
					if respuesta == 23:
						if x23 == " ":
							x23 = "o"
							break
						else:
							print ("Casilla ocupada, prueba otra vez")
					if respuesta == 31:
						print ("Casilla ocupada, prueba otra vez")
					if respuesta == 32:
						if x32 == " ":
							x32 = "o"
							break
						else:
							print ("Casilla ocupada, prueba otra vez")
					if respuesta == 33:
						if x33 == " ":
							x33 = "o"
							break
						else:
							print ("Casilla ocupada, prueba otra vez")												
					respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
				clear()
				zero_line = ["    1    2    3 "]
				first_line 	= [1,(x11,x12,x13)]
				second_line = [2,(x21,x22,x23)]
				third_line 	= [3,(x31,x32,x33)]
				print(zero_line)
				print(first_line)
				print(second_line)
				print(third_line)

				if x22 == " ":
					x22 = "x"
					time.sleep(1)
					clear()
					zero_line = ["    1    2    3 "]
					first_line 	= [1,(x11,x12,x13)]
					second_line = [2,(x21,x22,x23)]
					third_line 	= [3,(x31,x32,x33)]
					print(zero_line)
					print(first_line)
					print(second_line)
					print(third_line)
					
					
				else:
					x23 = "x"
					time.sleep(1)
					clear()
					zero_line = ["    1    2    3 "]
					first_line 	= [1,(x11,x12,x13)]
					second_line = [2,(x21,x22,x23)]
					third_line 	= [3,(x31,x32,x33)]
					print(zero_line)
					print(first_line)
					print(second_line)
					print(third_line)
					
		




























































		else:
			if x12 == "o":
				x33 = "x"
				clear()
				zero_line = ["    1    2    3 "]
				first_line 	= [1,(x11,x12,x13)]
				second_line = [2,(x21,x22,x23)]
				third_line 	= [3,(x31,x32,x33)]
				print(zero_line)
				print(first_line)
				print(second_line)
				print(third_line)
				respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
				while respuesta:
					if respuesta == 11:
						if x11 == " ":
							x11 = "o"
							break
						else:
							print ("Casilla ocupada, prueba otra vez")
					if respuesta == 12:
						if x12 == " ":
							x12 = "o"
							break
						else:
							print ("Casilla ocupada, prueba otra vez")
					if respuesta == 13:
						if x13 == " ":
							x13 = "o"
							break
						else:
							print ("Casilla ocupada, prueba otra vez")
					if respuesta == 21:
						if x21 == " ":
							x21 = "o"
							break
						else:
							print ("Casilla ocupada, prueba otra vez")
					if respuesta == 22:
						if x22 == " ":
							x22 = "o"
							break
						else:
							print ("Casilla ocupada, prueba otra vez")
					if respuesta == 23:
						if x23 == " ":
							x23 = "o"
							break
						else:
							print ("Casilla ocupada, prueba otra vez")
					if respuesta == 31:
						print ("Casilla ocupada, prueba otra vez")
					if respuesta == 32:
						if x32 == " ":
							x32 = "o"
							break
						else:
							print ("Casilla ocupada, prueba otra vez")
					if respuesta == 33:
						if x33 == " ":
							x33 = "o"
							break
						else:
							print ("Casilla ocupada, prueba otra vez")												
					respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))	
				clear()
				zero_line = ["    1    2    3 "]
				first_line 	= [1,(x11,x12,x13)]
				second_line = [2,(x21,x22,x23)]
				third_line 	= [3,(x31,x32,x33)]
				print(zero_line)
				print(first_line)
				print(second_line)
				print(third_line)
				if x32 == " ":
					x32 = "x"
					clear()
					zero_line = ["    1    2    3 "]
					first_line 	= [1,(x11,x12,x13)]
					second_line = [2,(x21,x22,x23)]
					third_line 	= [3,(x31,x32,x33)]
					print(zero_line)
					print(first_line)
					print(second_line)
					print(third_line)
					
					
				else:
					x22 = "x"
					clear()
					zero_line = ["    1    2    3 "]
					first_line 	= [1,(x11,x12,x13)]
					second_line = [2,(x21,x22,x23)]
					third_line 	= [3,(x31,x32,x33)]
					print(zero_line)
					print(first_line)
					print(second_line)
					print(third_line)
					respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
					while respuesta:
						if respuesta == 11:
							if x11 == " ":
								x11 = "o"
								break
							else:
								print ("Casilla ocupada, prueba otra vez")
						if respuesta == 12:
							if x12 == " ":
								x12 = "o"
								break
							else:
								print ("Casilla ocupada, prueba otra vez")
						if respuesta == 13:
							if x13 == " ":
								x13 = "o"
								break
							else:
								print ("Casilla ocupada, prueba otra vez")
						if respuesta == 21:
							if x21 == " ":
								x21 = "o"
								break
							else:
								print ("Casilla ocupada, prueba otra vez")
						if respuesta == 22:
							if x22 == " ":
								x22 = "o"
								break
							else:
								print ("Casilla ocupada, prueba otra vez")
						if respuesta == 23:
							if x23 == " ":
								x23 = "o"
								break
							else:
								print ("Casilla ocupada, prueba otra vez")
						if respuesta == 31:
							print ("Casilla ocupada, prueba otra vez")
						if respuesta == 32:
							if x32 == " ":
								x32 = "o"
								break
							else:
								print ("Casilla ocupada, prueba otra vez")
						if respuesta == 33:
							if x33 == " ":
								x33 = "o"
								break
							else:
								print ("Casilla ocupada, prueba otra vez")												
						respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
					clear()
					zero_line = ["    1    2    3 "]
					first_line 	= [1,(x11,x12,x13)]
					second_line = [2,(x21,x22,x23)]
					third_line 	= [3,(x31,x32,x33)]
					print(zero_line)
					print(first_line)
					print(second_line)
					print(third_line)
					

					if x11 == " ":
						x11 = "x"
						time.sleep(1)
						clear()
						zero_line = ["    1    2    3 "]
						first_line 	= [1,(x11,x12,x13)]
						second_line = [2,(x21,x22,x23)]
						third_line 	= [3,(x31,x32,x33)]
						print(zero_line)
						print(first_line)
						print(second_line)
						print(third_line)
						
						
					else:
						x13 = "x"
						time.sleep(1)
						clear()
						zero_line = ["    1    2    3 "]
						first_line 	= [1,(x11,x12,x13)]
						second_line = [2,(x21,x22,x23)]
						third_line 	= [3,(x31,x32,x33)]
						print(zero_line)
						print(first_line)
						print(second_line)
						print(third_line)
						
















































			else:

				if x13 == "o":
					x33 = "x"
					clear()
					zero_line = ["    1    2    3 "]
					first_line 	= [1,(x11,x12,x13)]
					second_line = [2,(x21,x22,x23)]
					third_line 	= [3,(x31,x32,x33)]
					print(zero_line)
					print(first_line)
					print(second_line)
					print(third_line)
					respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
					while respuesta:
						if respuesta == 11:
							if x11 == " ":
								x11 = "o"
								break
							else:
								print ("Casilla ocupada, prueba otra vez")
						if respuesta == 12:
							if x12 == " ":
								x12 = "o"
								break
							else:
								print ("Casilla ocupada, prueba otra vez")
						if respuesta == 13:
							if x13 == " ":
								x13 = "o"
								break
							else:
								print ("Casilla ocupada, prueba otra vez")
						if respuesta == 21:
							if x21 == " ":
								x21 = "o"
								break
							else:
								print ("Casilla ocupada, prueba otra vez")
						if respuesta == 22:
							if x22 == " ":
								x22 = "o"
								break
							else:
								print ("Casilla ocupada, prueba otra vez")
						if respuesta == 23:
							if x23 == " ":
								x23 = "o"
								break
							else:
								print ("Casilla ocupada, prueba otra vez")
						if respuesta == 31:
							print ("Casilla ocupada, prueba otra vez")
						if respuesta == 32:
							if x32 == " ":
								x32 = "o"
								break
							else:
								print ("Casilla ocupada, prueba otra vez")
						if respuesta == 33:
							if x33 == " ":
								x33 = "o"
								break
							else:
								print ("Casilla ocupada, prueba otra vez")												
						respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
					clear()
					zero_line = ["    1    2    3 "]
					first_line 	= [1,(x11,x12,x13)]
					second_line = [2,(x21,x22,x23)]
					third_line 	= [3,(x31,x32,x33)]
					print(zero_line)
					print(first_line)
					print(second_line)
					print(third_line)
					time.sleep(1)
					if x32 == " ":
						x32 = "x"
						clear()
						zero_line = ["    1    2    3 "]
						first_line 	= [1,(x11,x12,x13)]
						second_line = [2,(x21,x22,x23)]
						third_line 	= [3,(x31,x32,x33)]
						print(zero_line)
						print(first_line)
						print(second_line)
						print(third_line)
						
						
					else:
						x11 = "x"
						clear()
						zero_line = ["    1    2    3 "]
						first_line 	= [1,(x11,x12,x13)]
						second_line = [2,(x21,x22,x23)]
						third_line 	= [3,(x31,x32,x33)]
						print(zero_line)
						print(first_line)
						print(second_line)
						print(third_line)
						respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
						while respuesta:
							if respuesta == 11:
								if x11 == " ":
									x11 = "o"
									break
								else:
									print ("Casilla ocupada, prueba otra vez")
							if respuesta == 12:
								if x12 == " ":
									x12 = "o"
									break
								else:
									print ("Casilla ocupada, prueba otra vez")
							if respuesta == 13:
								if x13 == " ":
									x13 = "o"
									break
								else:
									print ("Casilla ocupada, prueba otra vez")
							if respuesta == 21:
								if x21 == " ":
									x21 = "o"
									break
								else:
									print ("Casilla ocupada, prueba otra vez")
							if respuesta == 22:
								if x22 == " ":
									x22 = "o"
									break
								else:
									print ("Casilla ocupada, prueba otra vez")
							if respuesta == 23:
								if x23 == " ":
									x23 = "o"
									break
								else:
									print ("Casilla ocupada, prueba otra vez")
							if respuesta == 31:
								print ("Casilla ocupada, prueba otra vez")
							if respuesta == 32:
								if x32 == " ":
									x32 = "o"
									break
								else:
									print ("Casilla ocupada, prueba otra vez")
							if respuesta == 33:
								if x33 == " ":
									x33 = "o"
									break
								else:
									print ("Casilla ocupada, prueba otra vez")												
							respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
						clear()
						zero_line = ["    1    2    3 "]
						first_line 	= [1,(x11,x12,x13)]
						second_line = [2,(x21,x22,x23)]
						third_line 	= [3,(x31,x32,x33)]
						print(zero_line)
						print(first_line)
						print(second_line)
						print(third_line)
					


						if x22 == " ":
							x22 = "x"
							time.sleep(1)
							clear()
							zero_line = ["    1    2    3 "]
							first_line 	= [1,(x11,x12,x13)]
							second_line = [2,(x21,x22,x23)]
							third_line 	= [3,(x31,x32,x33)]
							print(zero_line)
							print(first_line)
							print(second_line)
							print(third_line)
							
							
						else:
							x21 = "x"
							time.sleep(1)
							clear()
							zero_line = ["    1    2    3 "]
							first_line 	= [1,(x11,x12,x13)]
							second_line = [2,(x21,x22,x23)]
							third_line 	= [3,(x31,x32,x33)]
							print(zero_line)
							print(first_line)
							print(second_line)
							print(third_line)
							
							


























































				else:
					if x21 == "o":
						x33 = "x"
						clear()
						zero_line = ["    1    2    3 "]
						first_line 	= [1,(x11,x12,x13)]
						second_line = [2,(x21,x22,x23)]
						third_line 	= [3,(x31,x32,x33)]
						print(zero_line)
						print(first_line)
						print(second_line)
						print(third_line)	
						respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
						while respuesta:
							if respuesta == 11:
								if x11 == " ":
									x11 = "o"
									break
								else:
									print ("Casilla ocupada, prueba otra vez")
							if respuesta == 12:
								if x12 == " ":
									x12 = "o"
									break
								else:
									print ("Casilla ocupada, prueba otra vez")
							if respuesta == 13:
								if x13 == " ":
									x13 = "o"
									break
								else:
									print ("Casilla ocupada, prueba otra vez")
							if respuesta == 21:
								if x21 == " ":
									x21 = "o"
									break
								else:
									print ("Casilla ocupada, prueba otra vez")
							if respuesta == 22:
								if x22 == " ":
									x22 = "o"
									break
								else:
									print ("Casilla ocupada, prueba otra vez")
							if respuesta == 23:
								if x23 == " ":
									x23 = "o"
									break
								else:
									print ("Casilla ocupada, prueba otra vez")
							if respuesta == 31:
								print ("Casilla ocupada, prueba otra vez")
							if respuesta == 32:
								if x32 == " ":
									x32 = "o"
									break
								else:
									print ("Casilla ocupada, prueba otra vez")
							if respuesta == 33:
								if x33 == " ":
									x33 = "o"
									break
								else:
									print ("Casilla ocupada, prueba otra vez")												
							respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))	
						clear()
						zero_line = ["    1    2    3 "]
						first_line 	= [1,(x11,x12,x13)]
						second_line = [2,(x21,x22,x23)]
						third_line 	= [3,(x31,x32,x33)]
						print(zero_line)
						print(first_line)
						print(second_line)
						print(third_line)
						time.sleep(1)
						if x32 == " ":
							x32 = "x"
							clear()
							zero_line = ["    1    2    3 "]
							first_line 	= [1,(x11,x12,x13)]
							second_line = [2,(x21,x22,x23)]
							third_line 	= [3,(x31,x32,x33)]
							print(zero_line)
							print(first_line)
							print(second_line)
							print(third_line)
							
							
						else:
							x13 = "x"
							clear()
							zero_line = ["    1    2    3 "]
							first_line 	= [1,(x11,x12,x13)]
							second_line = [2,(x21,x22,x23)]
							third_line 	= [3,(x31,x32,x33)]
							print(zero_line)
							print(first_line)
							print(second_line)
							print(third_line)
							respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
							while respuesta:
								if respuesta == 11:
									if x11 == " ":
										x11 = "o"
										break
									else:
										print ("Casilla ocupada, prueba otra vez")
								if respuesta == 12:
									if x12 == " ":
										x12 = "o"
										break
									else:
										print ("Casilla ocupada, prueba otra vez")
								if respuesta == 13:
									if x13 == " ":
										x13 = "o"
										break
									else:
										print ("Casilla ocupada, prueba otra vez")
								if respuesta == 21:
									if x21 == " ":
										x21 = "o"
										break
									else:
										print ("Casilla ocupada, prueba otra vez")
								if respuesta == 22:
									if x22 == " ":
										x22 = "o"
										break
									else:
										print ("Casilla ocupada, prueba otra vez")
								if respuesta == 23:
									if x23 == " ":
										x23 = "o"
										break
									else:
										print ("Casilla ocupada, prueba otra vez")
								if respuesta == 31:
									print ("Casilla ocupada, prueba otra vez")
								if respuesta == 32:
									if x32 == " ":
										x32 = "o"
										break
									else:
										print ("Casilla ocupada, prueba otra vez")
								if respuesta == 33:
									if x33 == " ":
										x33 = "o"
										break
									else:
										print ("Casilla ocupada, prueba otra vez")												
								respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
							clear()
							zero_line = ["    1    2    3 "]
							first_line 	= [1,(x11,x12,x13)]
							second_line = [2,(x21,x22,x23)]
							third_line 	= [3,(x31,x32,x33)]
							print(zero_line)
							print(first_line)
							print(second_line)
							print(third_line)
					

							if x22 == " ":
								x22 = "x"
								time.sleep(1)
								clear()
								zero_line = ["    1    2    3 "]
								first_line 	= [1,(x11,x12,x13)]
								second_line = [2,(x21,x22,x23)]
								third_line 	= [3,(x31,x32,x33)]
								print(zero_line)
								print(first_line)
								print(second_line)
								print(third_line)
								
								
							else:
								x23 = "x"
								time.sleep(1)
								clear()
								zero_line = ["    1    2    3 "]
								first_line 	= [1,(x11,x12,x13)]
								second_line = [2,(x21,x22,x23)]
								third_line 	= [3,(x31,x32,x33)]
								print(zero_line)
								print(first_line)
								print(second_line)
								print(third_line)
								
								

























































					else:
						if x23 == "o":
							x33 = "x"
							clear()
							zero_line = ["    1    2    3 "]
							first_line 	= [1,(x11,x12,x13)]
							second_line = [2,(x21,x22,x23)]
							third_line 	= [3,(x31,x32,x33)]
							print(zero_line)
							print(first_line)
							print(second_line)
							print(third_line)
							respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
							while respuesta:
								if respuesta == 11:
									if x11 == " ":
										x11 = "o"
										break
									else:
										print ("Casilla ocupada, prueba otra vez")
								if respuesta == 12:
									if x12 == " ":
										x12 = "o"
										break
									else:
										print ("Casilla ocupada, prueba otra vez")
								if respuesta == 13:
									if x13 == " ":
										x13 = "o"
										break
									else:
										print ("Casilla ocupada, prueba otra vez")
								if respuesta == 21:
									if x21 == " ":
										x21 = "o"
										break
									else:
										print ("Casilla ocupada, prueba otra vez")
								if respuesta == 22:
									if x22 == " ":
										x22 = "o"
										break
									else:
										print ("Casilla ocupada, prueba otra vez")
								if respuesta == 23:
									if x23 == " ":
										x23 = "o"
										break
									else:
										print ("Casilla ocupada, prueba otra vez")
								if respuesta == 31:
									print ("Casilla ocupada, prueba otra vez")
								if respuesta == 32:
									if x32 == " ":
										x32 = "o"
										break
									else:
										print ("Casilla ocupada, prueba otra vez")
								if respuesta == 33:
									if x33 == " ":
										x33 = "o"
										break
									else:
										print ("Casilla ocupada, prueba otra vez")												
								respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
							clear()
							zero_line = ["    1    2    3 "]
							first_line 	= [1,(x11,x12,x13)]
							second_line = [2,(x21,x22,x23)]
							third_line 	= [3,(x31,x32,x33)]
							print(zero_line)
							print(first_line)
							print(second_line)
							print(third_line)
							time.sleep(1)
							if x32 == " ":
								x32 = "x"
								clear()
								first_line 	= [(x11,x12,x13)]
								second_line = [(x21,x22,x23)]
								third_line 	= [(x31,x32,x33)]
								print(first_line)
								print(second_line)
								print(third_line)
								
								

							else:
								x11 = "x"
								clear()
								zero_line = ["    1    2    3 "]
								first_line 	= [1,(x11,x12,x13)]
								second_line = [2,(x21,x22,x23)]
								third_line 	= [3,(x31,x32,x33)]
								print(zero_line)
								print(first_line)
								print(second_line)
								print(third_line)
								respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
								while respuesta:
									if respuesta == 11:
										if x11 == " ":
											x11 = "o"
											break
										else:
											print ("Casilla ocupada, prueba otra vez")
									if respuesta == 12:
										if x12 == " ":
											x12 = "o"
											break
										else:
											print ("Casilla ocupada, prueba otra vez")
									if respuesta == 13:
										if x13 == " ":
											x13 = "o"
											break
										else:
											print ("Casilla ocupada, prueba otra vez")
									if respuesta == 21:
										if x21 == " ":
											x21 = "o"
											break
										else:
											print ("Casilla ocupada, prueba otra vez")
									if respuesta == 22:
										if x22 == " ":
											x22 = "o"
											break
										else:
											print ("Casilla ocupada, prueba otra vez")
									if respuesta == 23:
										if x23 == " ":
											x23 = "o"
											break
										else:
											print ("Casilla ocupada, prueba otra vez")
									if respuesta == 31:
										print ("Casilla ocupada, prueba otra vez")
									if respuesta == 32:
										if x32 == " ":
											x32 = "o"
											break
										else:
											print ("Casilla ocupada, prueba otra vez")
									if respuesta == 33:
										if x33 == " ":
											x33 = "o"
											break
										else:
											print ("Casilla ocupada, prueba otra vez")												
									respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
								clear()
								zero_line = ["    1    2    3 "]
								first_line 	= [1,(x11,x12,x13)]
								second_line = [2,(x21,x22,x23)]
								third_line 	= [3,(x31,x32,x33)]
								print(zero_line)
								print(first_line)
								print(second_line)
								print(third_line)
					

								if x22 == " ":
									x22 = "x"
									time.sleep(1)
									clear()
									zero_line = ["    1    2    3 "]
									first_line 	= [1,(x11,x12,x13)]
									second_line = [2,(x21,x22,x23)]
									third_line 	= [3,(x31,x32,x33)]
									print(zero_line)
									print(first_line)
									print(second_line)
									print(third_line)
									
									

								else:
									x21 = "x"
									time.sleep(1)
									clear()
									zero_line = ["    1    2    3 "]
									first_line 	= [1,(x11,x12,x13)]
									second_line = [2,(x21,x22,x23)]
									third_line 	= [3,(x31,x32,x33)]
									print(zero_line)
									print(first_line)
									print(second_line)
									print(third_line)
									
							





















































						else:
							if x32 == "o":
								x11 = "x"
								clear()
								zero_line = ["    1    2    3 "]
								first_line 	= [1,(x11,x12,x13)]
								second_line = [2,(x21,x22,x23)]
								third_line 	= [3,(x31,x32,x33)]
								print(zero_line)
								print(first_line)
								print(second_line)
								print(third_line)
								respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
								while respuesta:
									if respuesta == 11:
										if x11 == " ":
											x11 = "o"
											break
										else:
											print ("Casilla ocupada, prueba otra vez")
									if respuesta == 12:
										if x12 == " ":
											x12 = "o"
											break
										else:
											print ("Casilla ocupada, prueba otra vez")
									if respuesta == 13:
										if x13 == " ":
											x13 = "o"
											break
										else:
											print ("Casilla ocupada, prueba otra vez")
									if respuesta == 21:
										if x21 == " ":
											x21 = "o"
											break
										else:
											print ("Casilla ocupada, prueba otra vez")
									if respuesta == 22:
										if x22 == " ":
											x22 = "o"
											break
										else:
											print ("Casilla ocupada, prueba otra vez")
									if respuesta == 23:
										if x23 == " ":
											x23 = "o"
											break
										else:
											print ("Casilla ocupada, prueba otra vez")
									if respuesta == 31:
										print ("Casilla ocupada, prueba otra vez")
									if respuesta == 32:
										if x32 == " ":
											x32 = "o"
											break
										else:
											print ("Casilla ocupada, prueba otra vez")
									if respuesta == 33:
										if x33 == " ":
											x33 = "o"
											break
										else:
											print ("Casilla ocupada, prueba otra vez")												
									respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
								clear()
								zero_line = ["    1    2    3 "]
								first_line 	= [1,(x11,x12,x13)]
								second_line = [2,(x21,x22,x23)]
								third_line 	= [3,(x31,x32,x33)]
								print(zero_line)
								print(first_line)
								print(second_line)
								print(third_line)
								time.sleep(1)
								if x21 == " ":
									x21 = "x"
									clear()
									first_line 	= [(x11,x12,x13)]
									second_line = [(x21,x22,x23)]
									third_line 	= [(x31,x32,x33)]
									print(first_line)
									print(second_line)
									print(third_line)
									
									
								else:
									x13 = "x"
									clear()
									zero_line = ["    1    2    3 "]
									first_line 	= [1,(x11,x12,x13)]
									second_line = [2,(x21,x22,x23)]
									third_line 	= [3,(x31,x32,x33)]
									print(zero_line)
									print(first_line)
									print(second_line)
									print(third_line)
									respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
									while respuesta:
										if respuesta == 11:
											if x11 == " ":
												x11 = "o"
												break
											else:
												print ("Casilla ocupada, prueba otra vez")
										if respuesta == 12:
											if x12 == " ":
												x12 = "o"
												break
											else:
												print ("Casilla ocupada, prueba otra vez")
										if respuesta == 13:
											if x13 == " ":
												x13 = "o"
												break
											else:
												print ("Casilla ocupada, prueba otra vez")
										if respuesta == 21:
											if x21 == " ":
												x21 = "o"
												break
											else:
												print ("Casilla ocupada, prueba otra vez")
										if respuesta == 22:
											if x22 == " ":
												x22 = "o"
												break
											else:
												print ("Casilla ocupada, prueba otra vez")
										if respuesta == 23:
											if x23 == " ":
												x23 = "o"
												break
											else:
												print ("Casilla ocupada, prueba otra vez")
										if respuesta == 31:
											print ("Casilla ocupada, prueba otra vez")
										if respuesta == 32:
											if x32 == " ":
												x32 = "o"
												break
											else:
												print ("Casilla ocupada, prueba otra vez")
										if respuesta == 33:
											if x33 == " ":
												x33 = "o"
												break
											else:
												print ("Casilla ocupada, prueba otra vez")												
										respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
									clear()
									zero_line = ["    1    2    3 "]
									first_line 	= [1,(x11,x12,x13)]
									second_line = [2,(x21,x22,x23)]
									third_line 	= [3,(x31,x32,x33)]
									print(zero_line)
									print(first_line)
									print(second_line)
									print(third_line)
									


									if x22 == " ":
										x22 = "x"
										time.sleep(1)
										clear()
										zero_line = ["    1    2    3 "]
										first_line 	= [1,(x11,x12,x13)]
										second_line = [2,(x21,x22,x23)]
										third_line 	= [3,(x31,x32,x33)]
										print(zero_line)
										print(first_line)
										print(second_line)
										print(third_line)
										
									else:
										x12 = "x"
										time.sleep(1)
										clear()
										zero_line = ["    1    2    3 "]
										first_line 	= [1,(x11,x12,x13)]
										second_line = [2,(x21,x22,x23)]
										third_line 	= [3,(x31,x32,x33)]
										print(zero_line)
										print(first_line)
										print(second_line)
										print(third_line)
										
								




















































							else:
								if x33 == "o":
									x11 = "x"
									clear()
									zero_line = ["    1    2    3 "]
									first_line 	= [1,(x11,x12,x13)]
									second_line = [2,(x21,x22,x23)]
									third_line 	= [3,(x31,x32,x33)]
									print(zero_line)
									print(first_line)
									print(second_line)
									print(third_line)
									respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
									while respuesta:
										if respuesta == 11:
											if x11 == " ":
												x11 = "o"
												break
											else:
												print ("Casilla ocupada, prueba otra vez")
										if respuesta == 12:
											if x12 == " ":
												x12 = "o"
												break
											else:
												print ("Casilla ocupada, prueba otra vez")
										if respuesta == 13:
											if x13 == " ":
												x13 = "o"
												break
											else:
												print ("Casilla ocupada, prueba otra vez")
										if respuesta == 21:
											if x21 == " ":
												x21 = "o"
												break
											else:
												print ("Casilla ocupada, prueba otra vez")
										if respuesta == 22:
											if x22 == " ":
												x22 = "o"
												break
											else:
												print ("Casilla ocupada, prueba otra vez")
										if respuesta == 23:
											if x23 == " ":
												x23 = "o"
												break
											else:
												print ("Casilla ocupada, prueba otra vez")
										if respuesta == 31:
											print ("Casilla ocupada, prueba otra vez")
										if respuesta == 32:
											if x32 == " ":
												x32 = "o"
												break
											else:
												print ("Casilla ocupada, prueba otra vez")
										if respuesta == 33:
											if x33 == " ":
												x33 = "o"
												break
											else:
												print ("Casilla ocupada, prueba otra vez")												
										respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
									clear()
									zero_line = ["    1    2    3 "]
									first_line 	= [1,(x11,x12,x13)]
									second_line = [2,(x21,x22,x23)]
									third_line 	= [3,(x31,x32,x33)]
									print(zero_line)
									print(first_line)
									print(second_line)
									print(third_line)
									time.sleep(1)
									if x21 == " ":
										x21 = "x"
										clear()
										zero_line = ["    1    2    3 "]
										first_line 	= [1,(x11,x12,x13)]
										second_line = [2,(x21,x22,x23)]
										third_line 	= [3,(x31,x32,x33)]
										print(zero_line)
										print(first_line)
										print(second_line)
										print(third_line)
										
										
									else:
										x13 = "x"
										clear()
										zero_line = ["    1    2    3 "]
										first_line 	= [1,(x11,x12,x13)]
										second_line = [2,(x21,x22,x23)]
										third_line 	= [3,(x31,x32,x33)]
										print(zero_line)
										print(first_line)
										print(second_line)
										print(third_line)
										respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
										while respuesta:
											if respuesta == 11:
												if x11 == " ":
													x11 = "o"
													break
												else:
													print ("Casilla ocupada, prueba otra vez")
											if respuesta == 12:
												if x12 == " ":
													x12 = "o"
													break
												else:
													print ("Casilla ocupada, prueba otra vez")
											if respuesta == 13:
												if x13 == " ":
													x13 = "o"
													break
												else:
													print ("Casilla ocupada, prueba otra vez")
											if respuesta == 21:
												if x21 == " ":
													x21 = "o"
													break
												else:
													print ("Casilla ocupada, prueba otra vez")
											if respuesta == 22:
												if x22 == " ":
													x22 = "o"
													break
												else:
													print ("Casilla ocupada, prueba otra vez")
											if respuesta == 23:
												if x23 == " ":
													x23 = "o"
													break
												else:
													print ("Casilla ocupada, prueba otra vez")
											if respuesta == 31:
												print ("Casilla ocupada, prueba otra vez")
											if respuesta == 32:
												if x32 == " ":
													x32 = "o"
													break
												else:
													print ("Casilla ocupada, prueba otra vez")
											if respuesta == 33:
												if x33 == " ":
													x33 = "o"
													break
												else:
													print ("Casilla ocupada, prueba otra vez")												
											respuesta = eval(input ("¿En que casilla quieres colocar tu pieza? (filacolumna)"))
										clear()
										zero_line = ["    1    2    3 "]
										first_line 	= [1,(x11,x12,x13)]
										second_line = [2,(x21,x22,x23)]
										third_line 	= [3,(x31,x32,x33)]
										print(zero_line)
										print(first_line)
										print(second_line)
										print(third_line)
					


										if x22 == " ":
											x22 = "x"
											time.sleep(1)
											clear()
											zero_line = ["    1    2    3 "]
											first_line 	= [1,(x11,x12,x13)]
											second_line = [2,(x21,x22,x23)]
											third_line 	= [3,(x31,x32,x33)]
											print(zero_line)
											print(first_line)
											print(second_line)
											print(third_line)
											
											
										else:
											x12 = "x"
											time.sleep(1)
											clear()
											zero_line = ["    1    2    3 "]
											first_line 	= [1,(x11,x12,x13)]
											second_line = [2,(x21,x22,x23)]
											third_line 	= [3,(x31,x32,x33)]
											print(zero_line)
											print(first_line)
											print(second_line)
											print(third_line)
														
				
		print("¡Has perdido!\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a")
		dksajldkajsda = input(" ")


	

main()