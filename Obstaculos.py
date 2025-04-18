import turtle

class Pipe:
    """
    Clase Pipe que representa un par de tubos en el juego Flappy Bird.
    Cada tubo tiene una posición y dimensiones específicas. Los tubos se mueven hacia la izquierda
    y se eliminan cuando salen de la pantalla. También se puede verificar si un punto está dentro de los tubos.
    Atributos:
    pipe1 (turtle.Turtle): Primer tubo.
    pipe2 (turtle.Turtle): Segundo tubo.
    punto_medio (float): Coordenada y del punto medio entre los dos tubos.
    Métodos:
    mover(): Mueve ambos tubos hacia la izquierda.
    is_out(): Verifica si los tubos han salido de la pantalla.
    is_in_area(x, y): Verifica si un punto (x, y) está dentro de los límites de los tubos.
    get_punto_medio(): Devuelve la coordenada y del punto medio entre los dos tubos.
    """

    def __init__(self, y):
        self.pipe1 = turtle.Turtle()
        self.pipe2 = turtle.Turtle()
        self.pipe1.shape("square")
        self.pipe2.shape("square")
        self.pipe1.color("green")
        self.pipe2.color("green")
        self.pipe1.alto = 400
        self.pipe1.ancho = 100
        self.pipe2.alto = 400
        self.pipe2.ancho = 100
        self.pipe1.shapesize(stretch_wid=self.pipe1.alto/20, stretch_len= self.pipe1.ancho/20)
        self.pipe2.shapesize(stretch_wid=self.pipe2.alto/20, stretch_len= self.pipe2.ancho/20)
        self.pipe1.penup()
        self.pipe2.penup()
        self.pipe1.speed(0)
        self.pipe2.speed(0)
        self.pipe1.setx(450)
        self.pipe2.setx(450)
        self.pipe1.sety(y + 270)
        self.pipe2.sety(y - 270)
        self._punto_medio = y
       

    def mover(self):
        """
        Mueve ambos tubos hacia la izquierda a una velocidad constante.
        """
        self.pipe1.setx(self.pipe1.xcor() - 4)
        self.pipe2.setx(self.pipe2.xcor() - 4)


    def is_out(self):
        """
        Verifica si los tubos han salido de la pantalla.
        Retorna:
            bool: True si los tubos han salido de la pantalla, False en caso contrario.
        """
        if self.pipe2.xcor() < -450:
            self.pipe1.clear()
            self.pipe2.clear()
            self.pipe1.hideturtle()
            self.pipe2.hideturtle()
            return True
        return False
        
    def is_in_area(self, x, y):
        """
        Verifica si el punto (x, y) está dentro de los límites de los tubos.
        Parametros:
            x (float): Coordenada x del punto.
            y (float): Coordenada y del punto.
        Retorna:
            bool: True si el punto está dentro de los tubos, False en caso contrario.
        """
        def dentro_de_tubo(pipe):
            return (
                pipe.xcor() - pipe.ancho / 2 < x < pipe.xcor() + pipe.ancho / 2 and
                pipe.ycor() - pipe.alto / 2 < y < pipe.ycor() + pipe.alto / 2
            )

        return dentro_de_tubo(self.pipe1) or dentro_de_tubo(self.pipe2)
        
    def get_punto_medio(self):
        """
        Devuelve la coordenada y del punto medio entre los dos tubos.
        Retorna:
            float: Coordenada y del punto medio entre los dos tubos.
        """
        return self._punto_medio