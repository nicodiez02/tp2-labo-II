import pygame
from pygame.locals import *
import sys

from config import ANCHO_VENTANA, ALTO_VENTANA, COLOR_FONDO

class PantallaJuego:
    def __init__(self):
        self.fuente = pygame.font.Font(None, 36)

    def manejar_eventos(self, eventos):
        # Definimos algunas constantes
        ANCHO, ALTO = 700, 600
        FILAS, COLUMNAS = 6, 7
        TAMANO_CASILLA = 100
        COLOR_FONDO = (255, 255, 255)
        COLOR_NEGRO = (0, 0, 0)
        ROJO = (255, 0, 0)
        VERDE = (100, 255, 100)

        # Inicializamos Pygame
        pygame.init()

        # Configuramos la pantalla
        pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("4 en Línea")

        # Cargamos las imagenes
        tableroPath = "./tablero.png"
        tablero = pygame.image.load(tableroPath).convert_alpha()
        tableroExpandido = pygame.transform.scale(tablero, (701, 600))

        fichaRojaPath = "./fichaRoja.png"
        fichaRoja = pygame.image.load(fichaRojaPath).convert_alpha()

        fichaAmarillaPath = "./fichaAmarilla.png"
        fichaAmarilla = pygame.image.load(fichaAmarillaPath).convert_alpha()
        tamanoFicha = fichaAmarilla.get_size()

        def reiniciar_juego():
            tablero = [[0] * COLUMNAS for _ in range(FILAS)]
            jugador_actual = 1

            while True:
                for evento in pygame.event.get():
                    if evento.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    elif evento.type == MOUSEBUTTONDOWN:
                        clic_x = evento.pos[0]
                        columna = clic_x // TAMANO_CASILLA

                        dejar_caer_ficha_animada(tablero, columna, jugador_actual)

                        if verificar_ganador(tablero, jugador_actual):
                            return  # Sal del bucle para reiniciar

                        jugador_actual = 3 - jugador_actual

                pantalla.fill(COLOR_FONDO)
                dibujar_tablero(tablero)
                pygame.display.flip()

        def mostrar_cartel_ganador(jugador):
            cartel_font = pygame.font.Font(None, 36)
            cartel_texto = cartel_font.render(f"¡Jugador {jugador} ha ganado!", True, COLOR_NEGRO)
            cartel_rect = cartel_texto.get_rect(center=(ANCHO // 2, ALTO // 2))

            cerrar_boton = pygame.Rect(ANCHO // 2 - 120, ALTO // 2 + 40, 240, 40)
            volver_a_jugar_boton = pygame.Rect(ANCHO // 2 - 120, ALTO // 2 + 90, 240, 40)

            while True:
                for evento in pygame.event.get():
                    if evento.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    elif evento.type == MOUSEBUTTONDOWN:
                        if cerrar_boton.collidepoint(evento.pos):
                            pygame.quit()
                            sys.exit()
                        elif volver_a_jugar_boton.collidepoint(evento.pos):
                            return True

                pantalla.fill(COLOR_FONDO)
                # dibujar_tablero(tablero)

                # Dibuja el cartel y los botones
                pygame.draw.rect(pantalla, COLOR_FONDO, cartel_rect)
                pygame.draw.rect(pantalla, ROJO, cerrar_boton)
                pygame.draw.rect(pantalla, VERDE, volver_a_jugar_boton)

                # Texto en los botones
                texto_cerrar = cartel_font.render("Cerrar", True, COLOR_FONDO)
                pantalla.blit(texto_cerrar, (cerrar_boton.center[0] - texto_cerrar.get_width() // 2, cerrar_boton.center[1] - texto_cerrar.get_height() // 2))

                texto_volver_a_jugar = cartel_font.render("Volver a Jugar", True, COLOR_FONDO)
                pantalla.blit(texto_volver_a_jugar, (volver_a_jugar_boton.center[0] - texto_volver_a_jugar.get_width() // 2, volver_a_jugar_boton.center[1] - texto_volver_a_jugar.get_height() // 2))

                pantalla.blit(cartel_texto, cartel_rect.topleft)
                pygame.display.flip()

        # Función para dibujar el tablero
        def dibujar_tablero(tablero):
            for fila in range(FILAS):
                for columna in range(COLUMNAS):
                    if tablero[fila][columna] == 1:
                        pantalla.blit(fichaRoja, (columna * TAMANO_CASILLA + (TAMANO_CASILLA - tamanoFicha[0]) // 2 , fila * TAMANO_CASILLA + (TAMANO_CASILLA - tamanoFicha[1]) // 2))
                    elif tablero[fila][columna] == 2:
                        pantalla.blit(fichaAmarilla, (columna * TAMANO_CASILLA + (TAMANO_CASILLA - tamanoFicha[0]) // 2, fila * TAMANO_CASILLA + (TAMANO_CASILLA - tamanoFicha[1]) // 2))
            pantalla.blit(tableroExpandido, (-1, 0))

        # Función para dejar caer una ficha en la columna seleccionada
        def dejar_caer_ficha_animada(tablero, columna, jugador):
            fila_destino = 0

            # Encuentra la posición de destino para la ficha
            for fila in range(FILAS - 1, -1, -1):
                if tablero[fila][columna] == 0:
                    fila_destino = fila
                    break

            # Inicializa la posición de la ficha en la parte superior de la pantalla
            x = columna * TAMANO_CASILLA + (TAMANO_CASILLA - tamanoFicha[0]) // 2
            y = 0

            # Animación de caída
            while y < TAMANO_CASILLA * (fila_destino):  # Ajuste para centrar la ficha
                for evento in pygame.event.get():
                    if evento.type == QUIT:
                        pygame.quit()
                        sys.exit()

                pantalla.fill(COLOR_FONDO)
                # Dibuja la ficha en su posición actual
                if jugador == 1:
                    pantalla.blit(fichaRoja, (x , int(y)))
                else: 
                    pantalla.blit(fichaAmarilla, (x , int(y)))

                dibujar_tablero(tablero)

                pygame.display.flip()

                # Incrementa la posición y para simular la caída
                y += 20  # Ajusta la velocidad de la caída

                # Controla la velocidad de la animación
                pygame.time.delay(30)

            # Coloca la ficha en su posición final en el tablero
            tablero[fila_destino][columna] = jugador

            return True

        # Función para verificar si hay un ganador
        def verificar_ganador(tablero, jugador):
            # Verificar horizontal
            for fila in range(FILAS):
                for columna in range(COLUMNAS - 3):
                    if tablero[fila][columna] == jugador and tablero[fila][columna + 1] == jugador and tablero[fila][columna + 2] == jugador and tablero[fila][columna + 3] == jugador:
                        return True

            # Verificar vertical
            for fila in range(FILAS - 3):
                for columna in range(COLUMNAS):
                    if tablero[fila][columna] == jugador and tablero[fila + 1][columna] == jugador and tablero[fila + 2][columna] == jugador and tablero[fila + 3][columna] == jugador:
                        return True

            # Verificar diagonales
            for fila in range(FILAS - 3):
                for columna in range(COLUMNAS - 3):
                    if tablero[fila][columna] == jugador and tablero[fila + 1][columna + 1] == jugador and tablero[fila + 2][columna + 2] == jugador and tablero[fila + 3][columna + 3] == jugador:
                        return True
                    if tablero[fila + 3][columna] == jugador and tablero[fila + 2][columna + 1] == jugador and tablero[fila + 1][columna + 2] == jugador and tablero[fila][columna + 3] == jugador:
                        return True

            return False

        # Función principal
        def empezarJuego():
            tablero = [[0] * COLUMNAS for _ in range(FILAS)]
            jugador_actual = 1

            while True:
                reiniciar_juego()
                if mostrar_cartel_ganador(jugador_actual):
                    continue

                # Dibujar el tablero
                pantalla.fill(COLOR_FONDO)
                dibujar_tablero(tablero)
                pantalla.blit(tableroExpandido, (-1, 0))
                pygame.display.flip()
        empezarJuego()

    def actualizar(self):
        pass

    def dibujar(self, ventana):
        ventana.fill(COLOR_FONDO)
