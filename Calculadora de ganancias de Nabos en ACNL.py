import sys  #El "sys" me ayudo mucho jajajja, me puse como tonto a usar el "break" pensando que me ayudaria a terminar el programa
            #cuando uno eliga "no" en las preguntas y pues, que equivocado estaba. Pero esto me ayudo mucho! ya que no sabia de su existencia.
            
print("¡Hola!")                                                                                      

print("""Primo esto para es ver cuantos nabos estas comprando, ganando
o perdiendo. Espero te guste!""")                                                                      

print()

print("(Por favor, solo usar numeros de manera entera, sin comas ni puntos.)")

print() #No consigo que dejar lineas libres cuando ejecuto mi "programa" si asi le puedo llamar jajaja, pero asi lo logro

nabos=int(input("A cuanto estan los Nabos?:"))  #Para esto e intentando usar el comando "float" pero me da los numeros de una manera que no
                                                #me agradan la verdad...
print()

cantidad=int(input("Cuantos nabos quieres comprar?:"))

print()

print("""Entonces si un nabo cuesta""", nabos, """Pues multiplicandolo con los""", cantidad,
"""nabos deseados"""+""",""","""serian""", nabos*cantidad, """Bayas!""")
                                                                         #No tiene que ver con el codigo esto, bueno si. Pero no creei 
ganancia=nabos*cantidad                                                  #usar mis matematicas en vacaciones jajaja


print("Estas a gusto y estoy en lo cierto?")                             #Ahora hablado sobre mi codigo. En las primeras 22 lineas de codigo
si=str (input("dime:"))                                                  #uso las primeras cosas que aprendi sobre Python, como: "int" y "str"
                                                                         #Y aca lo que es: "if", "elif" y "else". ¡Ah! y las Variables ovbio.
print()                         
        
if si=="si":
	print("Me alegro de averte ayudado primo!")                          #Y tambien creo que se noto, no se como explicarlo. Pero lo de usar
                                                                         #("""Tres Comillas""") para que el codigo no se valla a la quinta mrd
                                                                         #y pues lo dejo asi entre lineas y sea mas comodo.
else:
	print("Bueno, perdon")
	sys.exit()

print("Ahora veamos")

print()

s=(input("""Si estas usando este programa sea un dia de la semana el cual 
no es domingo (ya que es el unico dia el cual no puedes vender nabos) 
quieres saber si es buena idea vender tus nabos hoy u otro dia?
(Responde "s" para aceptar y "n" para negar): """))


if s=="s":
	print("Bueno, entonces ¡Hagamoslo!")


else:
	print("Bueno, cuando si lo quieras me avisas!")
	sys.exit()


nabos_2=int (input("a cuanto estan los nabos Hoy?:"))


if nabos>nabos_2:
	print("""Vaya! El precio de los Nabos hoy ¡Es menor que el dia que los
compraste! No es recomendable venderlos hoy primo. A menos que no 
sientas que el precio subira mañana.""")


elif nabos<nabos_2:
	print("¡Genial! El precio es mas alto que el dia que los compraste!")

print()

S=str(input("Entonces dime, ¿Quieres saber cuanto estas ganando o perdiendo?:"))

print()

if S=="si":
	print("""Bueno! por lo visto tus ganancias serian""", nabos_2*cantidad,"""Bayas,"""
	"""pero restando las bayas que usaste para lograr esa cantidad serian:""", cantidad*nabos_2-ganancia)


else:
	print("Bueno, cuando si quieras saberlo, dimelo!")
	sys.exit()


resultado=cantidad*nabos_2-ganancia

print()

print("Ganaste", resultado, "Bayas, es una buena cantidad eh?" )
