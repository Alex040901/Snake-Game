import pygame, sys, math, random

# pygame setup
pygame.init()
size = width, height = 1000, 700
dx = 20
dy = 0
white = 255,255,255
black = 0,0,0
grey = 128,128,128
x, y = 100, 100
radio = 10
thickness = 20

minX = thickness + radio
maxX = width - thickness - radio
minY = thickness + radio
maxY = height - thickness - radio

foodX = random.randrange(minX, maxX, 20)
foodY = random.randrange(minY, maxY, 20)

food = (foodX, foodY)

cuerpo = [(150, 500)]

fps = 10

largo_snk = 1

colision = pygame.Rect(100, 100, 20, 20)

colision_center = (x, y)

wallUp = pygame.Rect(0, 0, width, thickness)
wallDown = pygame.Rect(0, height - thickness, width, thickness)
wallRight = pygame.Rect(0, 0, thickness, height)
wallLeft = pygame.Rect(width - thickness, 0, thickness, height)
wallScreen = [wallUp, wallDown, wallRight, wallLeft]

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(fps)

    # Movimiento con teclas
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and dx != 20:
        dx = -20
        dy = 0
    if keys[pygame.K_RIGHT] and dx != -20:
        dx = 20
        dy = 0
    if keys[pygame.K_UP] and dy != 20:
        dy = -20
        dx = 0
    if keys[pygame.K_DOWN] and dy != -20:
        dy = 20
        dx = 0

    colision = colision.move(dx, dy)

    cuerpo.insert(0, colision.center)

    if len(cuerpo) > largo_snk:
        cuerpo.pop()

    hit_wall = (colision.left < thickness or colision.right > (width - thickness) or
                 colision.top < thickness or colision.bottom > (height - thickness))

    hit_body = colision.center in cuerpo[1:]

    if hit_wall or hit_body:
        print("Game Over - Reiniciando")

        colision.center = (width // 2, height // 2)
        dx = 20
        dy = 0
        fps = 10
        cuerpo = []
        largo_snk = 1
        foodX = random.randrange(minX, maxX, 20)
        foodY = random.randrange(minY, maxY, 20)
        food = (foodX, foodY)
    
    if colision.collidepoint(food):
        fps += 0.5
        print("velocidad",fps)
        largo_snk += 1
        foodX = random.randrange(minX, maxX, 20)
        foodY = random.randrange(minY, maxY, 20)
        food = (foodX, foodY)
        print("Cambiando la fruta a", food)  
        print("Eat apple!")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Saliendo del juego......")
                running = False            
            
    screen.fill(black)

    for parte in cuerpo:
        pygame.draw.circle(screen, white, parte, radio)
        
    #pygame.draw.rect(screen, (255,0,0), colision, 2)

    pygame.draw.circle(screen, (0,0,255), food, radio)

    # Dibujar las paredes
    for wall in wallScreen:
        pygame.draw.rect(screen, grey, wall)
   
    pygame.display.flip()

pygame.quit()
sys.exit()