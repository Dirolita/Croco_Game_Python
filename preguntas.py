import pygame

preguntas = [
    {
        "pregunta": "¿Cuál es la forma correcta de comentar una línea en Python?",
        "opciones": ["# Esto es un comentario", "// Esto es un comentario", "Verde"],
        "respuesta": "# Esto es un comentario"
    },
    {
        "pregunta": "¿Cuál es la palabra clave para definir una función en Python?",
        "opciones": ["define", "function", "def"],
        "respuesta": "def"
    },
    {
        "pregunta": "¿Cuál es la función utilizada para obtener la longitud de una lista en Python?" ,
        "opciones": ["count()", "length()", "len()"],
        "respuesta": "len()"
    },
    {
        "pregunta": "¿Cuál de las siguientes estructuras de datos en Python es mutable?" ,
        "opciones": ["Tuple", "Set", "String"],
        "respuesta": "Set"
    },
    {
        "pregunta": "¿Cómo se realiza la concatenación de dos listas en Python?" ,
        "opciones": ["list_concat(lista1, lista2)", "lista1.join(lista2)", "lista1 + lista2"],
        "respuesta": "lista1 + lista2"
    }
]

def mostrar_pregunta(player, opstaculo, ventana,pregunta):
    font = pygame.font.Font(None, 32)
    pregunta_actual = preguntas[pregunta] 
    texto_pregunta = font.render(pregunta_actual["pregunta"], True, (255, 255, 255))
    opciones_texto = []
    for index, opcion in enumerate(pregunta_actual["opciones"]):
        opcion_texto = font.render(f"{index + 1}: {opcion}", True, (255, 255, 255))
        opciones_texto.append(opcion_texto)

    respuesta_correcta = pregunta_actual["respuesta"]
    mostrar_texto = True

    while mostrar_texto:
        ventana.fill((0, 3, 20))
        #player.dibujar(ventana)
        #opstaculo.dibujar(ventana)
        ventana.blit(texto_pregunta, (40, 40))

        for idx, opcion_texto in enumerate(opciones_texto):
            ventana.blit(opcion_texto, (90, 140 + (idx * 50)))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if pregunta_actual["opciones"][0] == respuesta_correcta:
                        opstaculo.visible = False
                        mostrar_texto = False
                elif event.key == pygame.K_2:
                    if pregunta_actual["opciones"][1] == respuesta_correcta:
                        opstaculo.visible = False
                        mostrar_texto = False
                elif event.key == pygame.K_3:
                    if pregunta_actual["opciones"][2] == respuesta_correcta:
                        opstaculo.visible = False
                        mostrar_texto = False
                elif event.key == pygame.K_ESCAPE:
                    mostrar_texto = False

