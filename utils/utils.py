import pygame
from config import ANCHO_VENTANA, ALTO_VENTANA

class utils:
    def draw_button(x, y, width, height, text, click_handler, button_color, textColor):
        screen = pygame.display.set_mode((width, height))
        font = pygame.font.Font(None, 36)

        button_rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(screen, button_color, button_rect)

        text_surface = font.render(text, True, (0,0,0))
        text_rect = text_surface.get_rect(center=button_rect.center)
        screen.blit(text_surface, text_rect)

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        if button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (200, 200, 200), button_rect)

            if mouse_click[0]:  # Left mouse button clicked
                click_handler()

    def crear_degradado(color_inicio, color_fin):
        superficie = pygame.Surface((ANCHO_VENTANA, ALTO_VENTANA))
        degradado = pygame.Surface((1, ALTO_VENTANA))

        for y in range(ALTO_VENTANA):
            proporcion = y / ALTO_VENTANA
            color = (
                int(color_inicio[0] + (color_fin[0] - color_inicio[0]) * proporcion),
                int(color_inicio[1] + (color_fin[1] - color_inicio[1]) * proporcion),
                int(color_inicio[2] + (color_fin[2] - color_inicio[2]) * proporcion)
            )
            degradado.set_at((0, y), color)

        for x in range(ANCHO_VENTANA):
            superficie.blit(degradado, (x, 0))

        return superficie