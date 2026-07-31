# Snake Game - Pygame

Un motor de Snake clásico desarrollado en Python con **Pygame**, implementado desde cero para dominar la lógica de videojuegos 2D, manipulación de coordenadas en cuadrícula, detección de colisiones y manejo de estados.

---

## Características del Juego

- **Movimiento de precisión por grilla:** La serpiente y la comida se alinean estrictamente a bloques de 20px.
- **Dificultad Progresiva:** La velocidad de juego (`FPS`) se incrementa suave y dinámicamente con cada manzana consumida.
- **Máquina de Estados Simple:** Transiciones claras entre el estado principal de juego (`PLAYING`) y la pantalla de fin de juego (`GAME OVER`).
- **Sistema de Game Over Detallado:** Congela la escena al morir y reporta la causa exacta de la colisión (muro o autocolisión).
- **Persistencia de Récord:** Almacena la puntuación máxima en un archivo local (`highscore.txt`).
- **Control Antirreversa:** Previene colisiones accidentales inmediatas al bloquear giros de 180°.

---

## Estado del Proyecto & Checklist

- [x] Configuración de ventana y Game Loop.
- [x] Movimiento en ángulos rectos.
- [x] Movimiento continuo con teclado (`get_pressed`).
- [x] Manejo de bordes con `pygame.Rect`.
- [x] Generación de comida aleatoria alineada a la cuadrícula.
- [x] Lógica de cuerpo de serpiente con listas (efecto oruga).
- [x] Colisión con paredes y autocolisión.
- [x] Candado para evitar la "muerte por reversa".
- [x] Crecimiento y aceleración progresiva por FPS.
- [x] Puntaje dinámico en pantalla.
- [x] Pantalla de Game Over con causa de muerte.
- [x] Reinicio de partida con tecla `ENTER`.
- [x] Alineación de grilla y sincronización de comida.
- [x] Récord (*High Score*) persistente.

---

## Controles

**Flechas Direccionales** | Mover la serpiente (Arriba, Abajo, Izquierda, Derecha)
**Enter** | Reiniciar partida cuando estás en pantalla de *Game Over*
**Escape (ESC)** | Salir del juego 

---

## Requisitos e Instalación

### Prerrequisitos
- **Python 3.x**
- **Pygame**

### Pasos para ejecutar

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/Alex040901/Snake-Game](https://github.com/Alex040901/Snake-Game)
   cd snake-pygame