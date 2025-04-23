## 🚛 Armado Óptimo de Vehículos de Transporte de Paquetes (Ramificación y Poda)

El armado eficiente de vehículos de reparto es un desafío logístico fundamental en operaciones de distribución. Estos vehículos deben ser cargados siguiendo un orden específico de entrega, pero los paquetes están almacenados en filas tipo "pila", lo que genera restricciones físicas al acceso. En este proyecto desarrollamos un algoritmo que, mediante **ramificación y poda**, encuentra la **forma óptima de cargar un vehículo** con el menor número de movimientos posibles, respetando dichas restricciones.

---

### 🧠 Descripción del problema

En un centro de distribución, los paquetes están almacenados en **varias filas apiladas**. Cada fila se comporta como una **pila** (estructura LIFO): solo se puede retirar el **paquete que está al frente**. Si el paquete que se desea cargar está más atrás, es necesario **mover temporalmente los paquetes que lo bloquean a otras filas** para poder acceder a él.

El objetivo es **cargar un vehículo en un orden específico**, correspondiente a la secuencia de entregas, **minimizando la cantidad total de movimientos necesarios**.

---

### ⚙️ Metodología

En este repositorio encontrarás el desarrollo de un algoritmo de **búsqueda inteligente con ramificación y poda**, que permite evaluar múltiples combinaciones sin caer en fuerza bruta. El proceso funciona de la siguiente forma:

- Cada estado representa una **configuración del patio** (con los paquetes aún disponibles), el **vehículo parcialmente cargado**, el **costo acumulado** (número de movimientos) y la **secuencia de acciones realizadas**.
- Se utiliza una **cola de prioridad** (`heapq`) para expandir **primero los caminos de menor costo**.
- Se aplican reglas de **poda** para descartar caminos:
  - Si el costo actual ya supera la mejor solución encontrada.
  - Si no hay suficientes paquetes restantes para completar el objetivo.
- Se define un límite de exploración (`max_depth`) para controlar la complejidad computacional.

---

### 🧲 Detalles del modelo

- `initial_yard`: Una lista de listas que representa las filas apiladas de paquetes.
- `goal`: Lista que define el **orden exacto** de los paquetes que deben cargarse al vehículo.
- El **costo** se incrementa en función de cuántos paquetes hay que mover para acceder a uno en particular.
- Se generan nuevos estados mediante la función `generate_children_verbose_generic`, que simula los posibles movimientos desde un estado actual.

---

### 📊 Resultados

En el caso base simulado:

```python
initial_yard = [
    ['C', 'B', 'A', 'B', 'C', 'A'],
    ['A', 'B', 'C', 'A', 'B', 'C'],
    ['B', 'C', 'A', 'C', 'A', 'B'],
    ['C', 'C', 'B', 'B', 'A', 'A'],
    ['B', 'A', 'C', 'B', 'C', 'A'],
    ['A', 'C', 'B', 'C', 'A', 'B']
]

goal = ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'C', 'C']
```

El algoritmo encontró una **solución óptima** que permite cargar el vehículo en el orden requerido, utilizando el menor número posible de movimientos. Además, devuelve una **secuencia detallada de pasos** para ejecutar dicha carga.

---

### 📌 Archivos principales

- `State`: Clase que representa un estado intermedio del proceso.
- `generate_children_verbose_generic`: Genera todos los movimientos posibles desde el estado actual.
- `branch_and_bound_limited`: Función principal que implementa la lógica de ramificación y poda.
- `create_yard`, `count_types_generic`: Funciones auxiliares para simular el patio y contar los paquetes disponibles.

---

### 🚧 Próximas etapas

- Visualización interactiva paso a paso del proceso de carga.
- Incorporación de pesos, tiempos o prioridades de entrega por tipo de paquete.
- Comparación contra heurísticas simples o algoritmos de búsqueda exhaustiva.

