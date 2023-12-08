import pygame
from personaje import Personaje 
from preguntas import mostrar_pregunta

pygame.init()

def cargar_imagen(nombre_archivo, ancho, alto):
    imagen = pygame.image.load(nombre_archivo)
    return pygame.transform.scale(imagen, (ancho, alto))

# Crear personajes con la función cargar_imagen
player = Personaje(95, 190, cargar_imagen("imgs/COCO.png", 140, 55))
sapo = Personaje(325, 200, cargar_imagen("imgs/sapo.png", 59, 42))
cazador = Personaje(538, 107, cargar_imagen("imgs/casador.png", 72, 120))
leon = Personaje(585, 255, cargar_imagen("imgs/leon.png", 177, 130))
hipo = Personaje(273, 315, cargar_imagen("imgs/HIPO2.png", 163, 110))
banano = Personaje(113, 263, cargar_imagen("imgs/banana.png", 113, 64))
roca = Personaje(11, 361, cargar_imagen("imgs/rock.png", 110, 100))


#Creacion de ventana 
WIDTH = 800
HEIGHT = 500
BKG = (0,0,20)
Window = pygame.display.set_mode((WIDTH,HEIGHT))
background_image = pygame.image.load('imgs/fondo.jpg').convert()
imagen_redimensionada = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

#Nombre de Juego
pygame.display.set_caption("Croco Python Game - Diana Serrano")

#Definir variables de movimiento
keys = {pygame.K_w: False, pygame.K_s: False, pygame.K_a: False, pygame.K_d: False}
#Velocidad movimiento
reloj = pygame.time.Clock()

#Declaracion de posiciones de opstaculos:
ListaPosOb1 = [195,160,188]
ListaPosOb2 = [407,160,188]
ListaPosOb3 = [460,520,230,320]
ListaPosOb4 = [30,70,240,290]
ListaPosOb5 = [135,220,315,360]

#Bienvenida
font = pygame.font.Font(None, 36)
font_text = pygame.font.Font(None, 24)
welcome_text = font.render("¡Bienvenido a Croco Python Game", True, (68, 155, 30))
reto_text = font_text.render("Ayuda a Croco a estar solo en su pantano,contestando bien las preguntas", True, (72, 184, 241))
instruction_text = font.render("Presiona 's' para comenzar a jugar", True, (68, 155, 30))
game_started = False

#Ciclo de continuidad 
running = True
while running:
    Window.blit(imagen_redimensionada, (0, 0))
    player.dibujar(Window)
    hipo.dibujar(Window) 
    cazador.dibujar(Window)
    roca.dibujar(Window)
    leon.dibujar(Window)
    sapo.dibujar(Window)
    banano.dibujar(Window)
    reloj.tick(60)

    #Llamada de Bienvenida
    if not game_started:
        Window.blit(welcome_text, (200, 80))
        Window.blit(reto_text,(80,130))
        Window.blit(instruction_text, (200, 145))
        
    
    #Instruccion
    keys = pygame.key.get_pressed()
    if not game_started and keys[pygame.K_s]:
        game_started = True  # Comienza el juego al presionar 's'

    #Logica para cerrar
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Manejar eventos de teclas presionadas
        if event.type == pygame.KEYDOWN:
            if event.key in keys:
                keys[event.key] = True
        if event.type == pygame.KEYUP:
            if event.key in keys:
                keys[event.key] = False
    # Calcular movimiento basado en el estado de las teclas
        delta_x = (keys[pygame.K_d] - keys[pygame.K_a]) * 2
        delta_y = (keys[pygame.K_s] - keys[pygame.K_w]) * 2
        player.movimiento(delta_x, delta_y)
    #Logica busqueda de objetos
    if player.obtener_posicion_x() == ListaPosOb1[0] and ListaPosOb1[1] <= player.obtener_posicion_y() <= ListaPosOb1[2]:
        ListaPosOb1 =[0,0,0]
        keys = {pygame.K_w: False, pygame.K_s: False, pygame.K_a: False, pygame.K_d: False}
        mostrar_pregunta(player,sapo, Window,0)
    
    elif player.obtener_posicion_x() == ListaPosOb2[0] and ListaPosOb2[1] <= player.obtener_posicion_y() <= ListaPosOb2[2]:
        ListaPosOb2 =[0,0,0]
        keys = {pygame.K_w: False, pygame.K_s: False, pygame.K_a: False, pygame.K_d: False}
        mostrar_pregunta(player,cazador, Window,1)
    
    elif ListaPosOb3[0] <= player.obtener_posicion_x() <= ListaPosOb3[1] and ListaPosOb3[2] <= player.obtener_posicion_y() <= ListaPosOb3[3]:
        ListaPosOb3 =[0,0,0,0]
        keys = {pygame.K_w: False, pygame.K_s: False, pygame.K_a: False, pygame.K_d: False}
        mostrar_pregunta(player,leon, Window,2)

    elif ListaPosOb4[0] <= player.obtener_posicion_x() <= ListaPosOb4[1] and ListaPosOb4[2] <= player.obtener_posicion_y() <= ListaPosOb4[3]:
        ListaPosOb4 =[0,0,0,0]
        keys = {pygame.K_w: False, pygame.K_s: False, pygame.K_a: False, pygame.K_d: False}
        mostrar_pregunta(player,banano, Window,3)
        
    elif ListaPosOb5[0] <= player.obtener_posicion_x() <= ListaPosOb5[1] and ListaPosOb4[2] <= player.obtener_posicion_y() <= ListaPosOb5[3]:
        ListaPosOb5 =[0,0,0,0]
        keys = {pygame.K_w: False, pygame.K_s: False, pygame.K_a: False, pygame.K_d: False}
        mostrar_pregunta(player,hipo, Window,4)
    
    if sum(ListaPosOb1) == 0 and sum(ListaPosOb2) == 0 and sum(ListaPosOb3) == 0 and sum(ListaPosOb4) == 0 and sum(ListaPosOb5) == 0:
        felicitaciones_texto = font.render("¡Felicidades!", True, (68, 155, 30))
        Window.blit(felicitaciones_texto, (300, 80))

    pygame.display.update()

pygame.quit()

