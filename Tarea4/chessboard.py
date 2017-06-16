#importamos la libreria
import turtle


# Este codigo fue tomado para hacer pruebas y visualizar mejor el algoritmo de la reyna

#obtenemos las caracteristicas
wn=turtle.Screen()
#wn.bgcolor('lightblue')
wn.title('Chessboard')

#definimos la velocidad de la tortuga
turtle.speed(0)

'''
	IMPORTANTE LEER PARA MANIPULAR OJO EL TABLERO SOLO FUNCIONA CON NUMEROS DE 2^X EJEMPLO: 2^2 = 4, 2^4 = 16
Para poder mainpular el numero de filas y columnas que tendra nuestro tablero, es necesario cambiar los range en def square y def row a la mitad de lo que se busca, ejemplo
si se busca un tlabero de 12 X 12, en los range se colocara un 6, despues se colocara el numero total de cuadros por linea en el range de def chessboard, en nuestro 
ejemplo seria range(12), de igual manera lo haremos en nuestro turtle.bk(size*x) quedando en nuestro ejemplo de la siguiente manera: turtle.bk(size*12)
'''

'''En un tablero de ajedrez, para nuestro programa, abajo siempre sera reina blanca con las coordenadas (-125,25)'''
x=16
y=8


def reina(n):
	turtle.goto(-125,25)
	turtle.dot(20, "red")

#dibuja y rellena un cuadro
def square(size,alternate,color):
	turtle.color(color)
	turtle.begin_fill()
	for i in range(y):
		turtle.fd(size)
		turtle.lt(90)
	turtle.end_fill()
	turtle.fd(size)

#dibuja una fila de cuadros
def row(size,alternate,color1,color2):
	for i in range(y):
		if(alternate==True):
			square(size,alternate,color1)
			square(size,alternate,color2)
		else:
			square(size,alternate,color2)
			square(size,alternate,color1)

#Dibujamos el mapa entero
def chessboard(size,alternate,color1,color2):
	turtle.pu()
	turtle.goto(-(size*7),(size*7))
	for i in range(x):
		row(size,alternate,color1,color2)
		turtle.bk(size*x)
		turtle.rt(90)
		turtle.fd(size)
		turtle.lt(90)
		if(alternate==True):
			alternate=False
		else:
			alternate=True

chessboard(50,True,'black','white')
reina(8)

turtle.hideturtle()

turtle.done()

