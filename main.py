import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Side-Scrolling Game')
clock = pygame.time.Clock()

White = (255,255,255)
Green = (0,160,0)
Darkgreen = (20,80,20)

player = [100, 450, 0, 0] #xpos, ypos, xvel, yvel
OnGround = False
def move_player():
    global OnGround
    if keys[pygame.K_LEFT]:
        player[2] =- 5
    elif keys[pygame.K_RIGHT]:
        player[2] = 5
    else:
        player[2] = 0
    player[0]+=player[2]
    if OnGround == False:
        player[3] += 1
    player[0]+=player[2]
    player[1]+=player[3]

def Clouds():
    for x in range(100, 800, 300):
        pygame.draw.circle(screen, (White), (x, 100), 40)
        pygame.draw.circle(screen, (White), (x-50, 125), 40)
        pygame.draw.circle(screen, (White), (x+50, 125), 40)
        pygame.draw.rect(screen, (White), (x-50, 100, 100, 65))
def Trees():
    for x in range(100, 800, 300):
        pygame.draw.rect(screen, (Darkgreen), (x-10, 300, 20, 300))
        pygame.draw.circle(screen, (Green), (x, 300), 40)
        pygame.draw.circle(screen, (Green), (x-35, 325), 40)
        pygame.draw.circle(screen, (Green), (x+35, 325), 40)


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
    pygame.draw.rect(screen, Green, (0, 500, 800, 100))

    pygame.draw.rect(screen, (White), (player[0], player[1], 50, 50))
    
    
    pygame.display.flip()
pygame.quit()
