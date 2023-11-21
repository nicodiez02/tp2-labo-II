import pygame
import sys

from utils.utils import utils
from config import ANCHO_VENTANA, ALTO_VENTANA, PRIMARY_TEXT,BUTTON_BACKGROUND


class PantallaInicio:
    def __init__(self):
        self.fuente = pygame.font.SysFont("courier10", 36)
        self.texto = self.fuente.render("BIENVENIDO AL 4 EN LINEA", True, PRIMARY_TEXT)
        self.boton_rect = pygame.Rect(200, ALTO_VENTANA // 2 - 25, 150, 50)
        self.boton_texto = self.fuente.render("Comenzar partida", True, (255,255,255))

        self.boton_rect = pygame.Rect(
            ANCHO_VENTANA // 2 - 230 // 2 - 10,  # Puedes ajustar este valor según tus necesidades
            ALTO_VENTANA // 2 - 25,
            230 + 20,  # Puedes ajustar este valor según tus necesidades
            50,
        )

    def manejar_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if self.boton_rect.collidepoint(evento.pos):
                    return "juego"
        return "inicio"

    def actualizar(self):
        pass

    def dibujar(self, ventana):
        color_inicio = pygame.Color("#d690cc")
        color_fin = pygame.Color("#f7ecf6")
        fondo = utils.crear_degradado(color_inicio, color_fin)
        ventana.blit(fondo, (0, 0))
        pygame.draw.rect(ventana, BUTTON_BACKGROUND, self.boton_rect)
        ventana.blit(self.texto, (ANCHO_VENTANA // 2 - self.texto.get_width() // 2, 100))
        ventana.blit(self.boton_texto, (self.boton_rect.x + 25, self.boton_rect.y + 15))

