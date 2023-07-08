import turtle

def quadrado(graus, tamanho):
    for cont in range(4):
        turtle.forward(tamanho)
        turtle.right(graus)

def triangulo(graus, tamanho):
    colors = ["red", "violet", "orange"]
    for i in range(3):
        turtle.color(colors[i])
        turtle.left(graus)
        turtle.forward(tamanho)

def touche():
    screen = turtle.Screen()
    screen.title("TARTARUGA TOUCHE!")  # Coloca o título na janela.
    screen.bgcolor("lightyellow")  # Coloca a cor de fundo da janela em amarelo claro.
    turtle_obj = turtle.Turtle()
    turtle_obj.pensize(4)  # Define a espessura do traço.
    turtle_obj.color("blue")  # Define a cor da tartaruga e do traço.
    turtle_obj.shape("turtle")  # Define o formato da tartaruga.
    turtle_obj.speed(1)  # Define a velocidade da tartaruga.
    quadrado(90, 200)
    triangulo(120, 150)

touche()  # Chama a função.
turtle.mainloop()  # Mantém a janela aberta.
