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

food_size = 8

game_state = "PLAYING"
causa_dead = ""

font = pygame.font.Font(None, 30)
font_state = pygame.font.Font(None, 60)
font_sub = pygame.font.Font(None, 60)
score = 0
high_score = 0

minX = thickness + radio
maxX = width - thickness - radio
minY = thickness + radio
maxY = height - thickness - radio

foodX = random.randrange(thickness, width - thickness, 20) + radio
foodY = random.randrange(thickness, height - thickness, 20) + radio

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

def draw_score(surface, score_value):
    score_text = font.render(f"Score: {score_value}", True, white)
    surface.blit(score_text, (thickness, thickness))

def draw_state(surface, state, causa):
    state_text = font_state.render(state, True, white)
    text_rect = state_text.get_rect()
    text_rect.center = (width // 2, 320)
    surface.blit(state_text, text_rect)

    causa_text = font_sub.render(causa, True, (255,100,100))
    causa_rect = causa_text.get_rect()
    causa_rect.center = (width // 2, 370)
    surface.blit(causa_text, causa_rect)

    restart_text = font_sub.render("Presiona ENTER para reiniciar", True, grey)
    restart_rect = restart_text.get_rect()
    restart_rect.center = (width // 2, 420)
    surface.blit(restart_text, restart_rect)

def draw_score(surface, score_value, high_score_value):
    score_text = font.render(f"Score: {score_value} | Record: {high_score_value}", True, white)
    surface.blit(score_text, (thickness, thickness))

try:
    with open("highscore.txt", "r") as file:
        high_score = int(file.read())
except:
    high_score = 0

while running:
    clock.tick(fps)

    # Movimiento con teclas
    if game_state == "PLAYING":
    
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
            if hit_wall:
                causa_dead = "Chocaste con la pared"
            elif hit_body:
                causa_dead = "Te comiste a ti mismo"

            if score > high_score:
                high_score = score

                with open("highscore.txt", "w") as file:
                    file.write(str(high_score))

            game_state = "GAME OVER"
       
    if colision.collidepoint(food):
        fps += 0.5
        score += 5
        largo_snk += 1
        foodX = random.randrange(thickness, width - thickness, 20) + radio
        foodY = random.randrange(thickness, height - thickness, 20) + radio
        food = (foodX, foodY)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False 

            if game_state == "GAME OVER" and event.key == pygame.K_RETURN:
                colision.center = (width // 2, height // 2)
                dx = 20
                dy = 0
                score = 0
                cuerpo = []
                fps = 10
                largo_snk = 1
                foodX = random.randrange(thickness, width - thickness, 20) + radio
                foodY = random.randrange(thickness, height - thickness, 20) + radio
                food = (foodX, foodY)

                game_state = "PLAYING"
            
    screen.fill(black)

    if game_state == "GAME OVER":
        draw_state(screen, "GAME OVER", causa_dead)

    for parte in cuerpo:
        pygame.draw.circle(screen, white, parte, radio)
        
    #pygame.draw.rect(screen, (255,0,0), colision, 2)

    pygame.draw.circle(screen, (0,0,255), food, 7)

    # Dibujar las paredes
    for wall in wallScreen:
        pygame.draw.rect(screen, grey, wall)

    draw_score(screen, score, high_score)
   
    pygame.display.flip()

pygame.quit()
sys.exit()