import pygame
from windows.welcome import PantallaInicio 
from windows.game import PantallaJuego 
from config import ANCHO_VENTANA, ALTO_VENTANA

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("4 en Linea")

def main():
    pantalla_actual = PantallaInicio()

    while True:
        eventos = pygame.event.get()

        proximo_estado = pantalla_actual.manejar_eventos(eventos)

        if proximo_estado == "juego":
            pantalla_actual = PantallaJuego()

        pantalla_actual.actualizar()
        pantalla_actual.dibujar(ventana)

        pygame.display.flip()

        pygame.time.Clock().tick(30)

if __name__ == "__main__":
    main()
