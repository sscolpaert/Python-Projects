import turtle

def main():
    # Movimentando a tartaruga.
    set_up_turtle()

    for cont in range(4):
        turtle.forward(200)  # Anda para frente 200 pixels.
        turtle.right(90)  # Gira 90 graus para a direita.

    turtle.done()  # Fecha a janela da tartaruga.

def set_up_turtle():
    turtle.title("TARTARUGA TOUCHE!")  # Coloca o título na janela.
    turtle.bgcolor("lightyellow")  # Coloca a cor de fundo da janela em amarelo claro.
    turtle.pensize(4)  # Define a espessura do traço.
    turtle.color("blue")  # Define a cor da tartaruga e do traço.
    turtle.shape("turtle")  # Coloca o formato da tartaruga.
    turtle.delay(50)

if __name__ == "__main__":
    main()