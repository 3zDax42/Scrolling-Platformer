import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Side-Scrolling Game')
clock = pygame.time.Clock()

White = (255,255,255)
Green = (0,160,0)
Darkgreen = (20,80,20)
platforms = [(500, 400), (700, 300), (900, 200), (700, 100)]

player = [100, 450, 0, 0] #xpos, ypos, xvel, yvel
OnGround = False
offset = 0
def draw_platforms():
    for i in range(len(platforms)):
        pygame.draw.rect(screen, (150, 10, 10), (platforms[i][0] + offset, platforms[i][1], 100, 30))
def move_player():
    global OnGround
    global offset
    
    if player[1] >= 450: # Checks if on ground
        player[1] = 450
        OnGround = True
    for i in range(len(platforms)):
        if player[0]+50>platforms[i][0]+offset and player[0]<platforms[i][0]+100+offset and player[1]+50>platforms[i][1] and player[1]+50<platforms[i][1]+50:
            OnGround = True
            player[1] = platforms[i][1]-50
            player[3] = 0
    if keys[pygame.K_LEFT]:  # Move left
        if offset > 260 and player[0] > 0:
            player[2] = -5
        elif player[0] > 400 and offset < -1500:
            player[2] = -5
        elif player[0] > 0:
            offset+=5
            player[2]=0
        else:
            player[2]=0
    elif keys[pygame.K_RIGHT]: # Move right
        if offset < -1500 and player[0] < 750:
            player[2] = 5
        elif player[0] < 400 and offset > 260:
            player[2] = 5
        elif player[0] < 750:
            offset -= 5
            player[2] = 0
        else:
            player[2]=0
    else:
        player[2] = 0
    if OnGround == True and keys[pygame.K_UP]: # Jumps
        player[3] = -15
        OnGround = False
    if OnGround == False: # Gravity
        player[3] += 1
    player[0]+=player[2]
    player[1]+=player[3]

def Clouds():
    for x in range(100, 3200, 300):
        pygame.draw.circle(screen, (White), (x+offset, 100), 40)
        pygame.draw.circle(screen, (White), (x-50+offset, 125), 40)
        pygame.draw.circle(screen, (White), (x+50+offset, 125), 40)
        pygame.draw.rect(screen, (White), (x-50+offset, 100, 100, 65))
def Trees():
    for x in range(-250, 3200, 300):
        pygame.draw.rect(screen, (Darkgreen), (x-10+offset, 300, 20, 300))
        pygame.draw.circle(screen, (Green), (x+offset, 300), 40)
        pygame.draw.circle(screen, (Green), (x-35+offset, 325), 40)
        pygame.draw.circle(screen, (Green), (x+35+offset, 325), 40)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(60)
    keys = pygame.key.get_pressed()
    
    #Physics section
    move_player()
    #Render section
    screen.fill((135,206,235))
    Clouds()
    Trees()
    draw_platforms()
    pygame.draw.rect(screen, Green, (0, 500, 800, 100))

    pygame.draw.rect(screen, (White), (player[0], player[1], 50, 50))
    
    
    pygame.display.flip()
pygame.quit()
