import pygame, sys, math

# pygame setup
pygame.init()
size = width, height = 1000, 700
dx = 1
dy = 0
white = 255,255,255
black = 0,0,0
grey = 128,128,128
x, y = 100, 100
radio = 20
thickness = 20

cuerpo = [(100, 50), (90, 50), (80, 50)]

colision = pygame.Rect(100, 100, 40, 40)

colision_center = (x, y)

wallUp = pygame.Rect(0, 0, width, thickness)
wallDown = pygame.Rect(0, 680, width, thickness)
wallRight = pygame.Rect(0, 0, thickness, height)
wallLeft = pygame.Rect(980, 0, thickness, height)
wallScreen = [wallUp, wallDown, wallRight, wallLeft]

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        dx = -1
        dy = 0
    if keys[pygame.K_RIGHT]:
        dx = 1
        dy = 0
    if keys[pygame.K_UP]:
        dy = -1
        dx = 0
    if keys[pygame.K_DOWN]:
        dy = 1
        dx = 0

    colision = colision.move(dx, dy)

    if colision.left < thickness or colision.right > (width - thickness):
        dx = -dx
        print("GAME OVER")
        #running = False
    if colision.top < thickness or colision.bottom > (height - thickness):
        dy = -dy
        print("GAME OVER")
        #running = False


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
        
    pygame.draw.rect(screen, (255,0,0), colision, 2)

    for wall in wallScreen:
        pygame.draw.rect(screen, grey, wall)
   
    pygame.display.flip()

pygame.quit()
sys.exit()