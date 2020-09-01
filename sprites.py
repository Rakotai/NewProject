import pygame, sys
# <-- Init --> 
pygame.init()
clock = pygame.time.Clock()
width = 500
height = 500
left = width/2 - 10 
top =  height/2 - 20
screen = pygame.display.set_mode((width, height))

# Functions 


# <-- Colors -->

color_red = (194,24,7)
color_blue = (0,0,255)
color_orange = (255,165,0)
light_grey = (200,200,200)
background = pygame.Color('grey12')
screen.fill(background)

# <--- Drawing Objects --->


# start
run = True
while run:
    keyPressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            sys.exit()
            run = False

    
    pygame.display.flip()
    clock.tick(60)