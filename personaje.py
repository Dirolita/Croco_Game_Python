import pygame

# Forma y ubicacion
class Personaje():
    def __init__(self, x, y, image):
        self.image_original = image  # Guarda una copia de la imagen original
        self.image = self.image_original  # Imagen que se mostrará
        self.forma = pygame.Rect(0, 0, 20, 20)
        self.forma.center = (x, y)
        self.visible = True
        self.direccion = 'derecha'  # Puede ser 'derecha' o 'izquierda'

    def obtener_posicion_x(self):
        return self.forma.x

    def obtener_posicion_y(self):
        return self.forma.y

    def dibujar(self, interfaz):
        if self.visible:
            interfaz.blit(self.image, self.forma)

    def movimiento(self, delta_x, delta_y):
        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y

        # Si se está moviendo a la derecha, muestra la imagen normal
        if delta_x > 0:
            self.image = self.image_original
            self.direccion = 'derecha'
        # Si se está moviendo a la izquierda, voltear la imagen horizontalmente
        elif delta_x < 0:
            self.image = pygame.transform.flip(self.image_original, True, False)
            self.direccion = 'izquierda'
