import turtle as t
import numpy as np

def draw_agent_with_sensors():
    """
    Dibuja un agente estático con sus sensores para visualización.
    """
    # Configurar pantalla
    screen = t.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("lightblue")
    screen.title("Visualización del Agente y sus Sensores")
    
    # Crear el agente
    agent = t.Turtle()
    agent.shape("triangle")
    agent.color("yellow")
    agent.shapesize(stretch_wid=1, stretch_len=1)
    agent.penup()
    agent.goto(0, 0)
    
    # Crear sensores
    sensors = []
    sensor_colors = ["red", "orange", "green", "purple", "blue"]
    sensor_labels = [
        "Diagonal Superior Derecha",
        "Diagonal Inferior Derecha",
        "Superior",
        "Inferior",
        "Derecha"
    ]
    
    # Posiciones finales de los sensores (dirección y longitud)
    sensor_positions = [
        (150, 150),    # Diagonal superior derecha
        (150, -150),   # Diagonal inferior derecha
        (0, 150),      # Superior
        (0, -150),     # Inferior
        (150, 0)       # Derecha
    ]
    
    # Dibujar cada sensor
    for i in range(5):
        sensor = t.Turtle()
        sensor.hideturtle()
        sensor.penup()
        sensor.goto(0, 0)  # Posición del agente
        sensor.pendown()
        sensor.pensize(2)
        sensor.color(sensor_colors[i])
        sensor.goto(sensor_positions[i])
        
        # Añadir flecha al final del sensor
        sensor.stamp()
        
        # Añadir etiqueta
        sensor.penup()
        sensor.goto(sensor_positions[i][0] + 10, sensor_positions[i][1])
        sensor.write(sensor_labels[i], font=("Arial", 10, "normal"))
        
        sensors.append(sensor)
    
    # Añadir título explicativo
    title = t.Turtle()
    title.hideturtle()
    title.penup()
    title.goto(-300, 250)
    title.write("Agente con 5 Sensores Direccionales", font=("Arial", 16, "bold"))
    
    # Añadir leyenda
    legend = t.Turtle()
    legend.hideturtle()
    legend.penup()
    legend.goto(-300, 190)
    legend.write(
        "Los sensores detectan obstáculos a distancias de 20 a 250 píxeles.\n"
        "Cada sensor retorna un valor normalizado entre 0.2 y 2.5.\n"
        "Un valor de 2.5 indica que no hay obstáculo en esa dirección.",
        font=("Calibri", 12, "normal")
    )
    
    # Añadir una tubería de ejemplo (aparece completa inmediatamente)
    pipe = t.Turtle()
    pipe.hideturtle()  # Ocultar la tortuga después de dibujar
    pipe.shape("square")
    pipe.color("green")
    pipe.shapesize(stretch_wid=8, stretch_len=2)
    pipe.penup()
    pipe.goto(110, 80)  # Posición del medio de la tubería
    pipe.showturtle()  # Mostrar la tortuga para dibujar la tubería
    texto_tubo = t.Turtle()
    texto_tubo.hideturtle()
    texto_tubo.color("green")
    texto_tubo.penup()
    texto_tubo.goto(150, 80)
    texto_tubo.write("Tubería de ejemplo", font=("Calibri", 10, "normal"))
    
    # Mostrar la distancia detectada en cada sensor
    values_text = t.Turtle()
    values_text.hideturtle()
    values_text.penup()
    values_text.goto(-320, -100)
    
    # Calcular valores de ejemplo para los sensores basados en la tubería
    sensor_values = [1.0, 2.5, 2.5, 2.5, 1.0]  # Valores de ejemplo
    
    values_text.write(
        "Valores de los sensores con este obstáculo:\n" +
        "\n".join([f"Sensor {i+1} ({sensor_labels[i]}): {sensor_values[i]}" 
                  for i in range(5)]),
        font=("Calibri", 12, "normal")
    )
    
    screen.update()
    t.done()

# Ejecutar la función
if __name__ == "__main__":
    draw_agent_with_sensors()