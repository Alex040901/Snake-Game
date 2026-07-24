import pygame, sys, math

# pygame setup
pygame.init()
size = width, height = 1000, 700
speed = [5,5]
white = 255,255,255
black = 0,0,0
grey = 128,128,128
x, y = 100, 100
radio = 20
thickness = 20

colision = pygame.Rect(0, 0, 40, 40)
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
        colision.x -= speed[0]
    if keys[pygame.K_RIGHT]:
        colision.x += speed[0]
    if keys[pygame.K_UP]:
        colision.y -= speed[1]
    if keys[pygame.K_DOWN]:
        colision.y += speed[1]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Saliendo del juego......")
                running = False

        if colision.x < 0 or colision.x >= (width-thickness):
            speed[0] = -speed[0]
        if colision.top < 0 or colision.bottom >= (height-thickness):
            speed[1] = -speed[1]

            print("GAME OVER")
            
            
    screen.fill(black)

    pygame.draw.circle(screen, white, colision.center, radio)
    pygame.draw.rect(screen, (255,0,0), colision, 2)

    for x in wallScreen:
        pygame.draw.rect(screen, grey, x)
   
    pygame.display.flip()

pygame.quit()
sys.exit()