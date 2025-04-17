# 🐤 Agente que aprende a jugar Flappy Bird usando algoritmos genéticos


---

## 🚀 Sobre el Proyecto

Este proyecto es una implementación del clásico juego Flappy Bird donde los agentes aprenden a jugar a través de algoritmos genéticos y redes neuronales. 
En lugar de programar explícitamente la lógica de juego, este proyecto permite que los agentes evolucionen naturalmente a través de generaciones, aprendiendo a navegar entre obstáculos de manera cada vez más eficiente.

---

## 📊 Características Principales

- **Algoritmos Genéticos**: Evolución natural de agentes mediante selección, cruce y mutación.
- **Redes Neuronales**: Toma de decisiones basada en redes neuronales que mejoran con cada generación.
- **Sensores Virtuales**: Los agentes detectan obstáculos mediante sensores en diferentes direcciones.
- **Simulación Visual**: Visualización en tiempo real de la evolución de los agentes.
- **Métrica de Fitness**: Sistema de evaluación que recompensa supervivencia y posicionamiento estratégico.

---

## 🛠️ Tecnologías Utilizadas

- Python: Lenguaje principal de programación.
- Turtle: Biblioteca para visualización gráfica.
- NumPy: Manipulación de matrices y operaciones matemáticas.
- Programación Orientada a Objetos: Arquitectura basada en clases y objetos.

---

## 🔧 Instalación y Ejecución

**Clona este repositorio:**

`git clone https://github.com/frantorres14/Flappy-Bird-Agent-Trained-Through-Genetic-Algorithms.git`

`cd FlappyGeneticAgents`

**Instala las dependencias:**



**Ejecuta el programa principal:**

`python Main.py`

---

## 📖 Cómo Funciona

### Arquitectura de Agentes

Cada agente (pájaro) utiliza:

- Una red neuronal para tomar decisiones de salto.
- Sensores que detectan obstáculos en 5 direcciones diferentes.
- Un valor de fitness que mide su desempeño.

### Algoritmo Genético

- **Inicialización**: Se crea una población inicial con genes aleatorios.
- **Simulación**: Los agentes juegan hasta que mueren o se alcanza un límite de tiempo.
- **Selección**: Los agentes con mejor desempeño tienen más probabilidad de ser seleccionados.
- **Cruce**: Los genes de los agentes seleccionados se combinan para crear nuevos agentes.
- **Mutación**: Pequeñas alteraciones aleatorias en los genes para mantener diversidad.
- **Repetición**: El proceso se repite por múltiples generaciones.

### Sistema de Fitness

Los agentes acumulan fitness por:

- Sobrevivir cada frame (+1 punto).
- Mantenerse cerca del centro de la pantalla (hasta +0.1 puntos por frame).

---

## 🎮 Controles e Interfaz

La simulación es completamente automática.

La ventana muestra:

- Agentes actuales (pájaros).
- Obstáculos (tubos).
- Número de generación.

---

## 📋 Estructura del Proyecto

- `main.py`: Punto de entrada y coordinación del programa.
- `mimulation.py`: Lógica de la simulación y visualización.
- `agente.py`: Implementación de los agentes (pájaros).
- `redneuronal.py`: Implementación de la red neuronal.
- `geneticalgo.py`: Implementación del algoritmo genético.
- `obstaculos.py`: Definición de los obstáculos (tubos).

---

## 🧠 Aspectos Técnicos

### Red Neuronal

Arquitectura de 3 capas:

- Capa de entrada: 5 neuronas (sensores).
- Capa oculta: 2 neuronas.
- Capa de salida: 1 neurona (decisión de saltar).

### Codificación Genética

Cada agente tiene 60 genes binarios que codifican los pesos de la red neuronal.

### Parámetros de la simulación

Estos parámetros se pueden cambiar en el archivo main.py
- Población: 40 agentes. (Se recomiendan más de 10)
- Generaciones: 100. (Se recomiendan más de 10)
Estos parámetros se pueden cambiar en el archivo geneticalgo.py
- Método de selección: Torneo. (Se puede cambiar por ruleta)
- Método de cruce: Dos puntos. (Se puede cambiar por un punto)
- Probabilidad de mutación: 0.01.

---

## 📝 Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo LICENSE para más detalles.

---

## 👨‍💻 Autor

Tu Nombre - Trabajo Inicial - [@frantorres14](https://github.com/frantorres14)

---


## ⭐️ De tu-usuario

¡Si te gusta el proyecto, no olvides dejar una estrella en GitHub!
También puedes seguirme en mis redes para tutoriales y videos sobre IA
TikTok: [@frantorresia](https://www.tiktok.com/@frantorresia)
YT: [@frantorresia](https://www.youtube.com/@frantorresia)
