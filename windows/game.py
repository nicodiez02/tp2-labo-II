import pygame
import sys

from config import ANCHO_VENTANA, ALTO_VENTANA, COLOR_FONDO

class PantallaJuego:
    def __init__(self):
        self.fuente = pygame.font.Font(None, 36)
        self.texto = self.fuente.render("Pantalla del Juego", True, (0, 0, 0))

    def manejar_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        return "juego"

    def actualizar(self):
        pass

    def dibujar(self, ventana):
        ventana.fill(COLOR_FONDO)
        ventana.blit(self.texto, (ANCHO_VENTANA // 2 - self.texto.get_width() // 2, ALTO_VENTANA // 2 - self.texto.get_height() // 2 - 50))
