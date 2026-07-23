import pygame, sys, math

# pygame setup
pygame.init()
size = width, height = 1080, 720
speed = 5
white = 255,255,255
black = 0,0,0
x, y = 540, 360
food_size = 20

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Saliendo del juego......")
                running = False
            
    screen.fill(black)

    pygame.draw.circle(screen, white, [x, y], food_size)
    pygame.display.flip()

pygame.quit()
sys.exit()