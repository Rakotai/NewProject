import pygame, sys
pygame.init()
clock = pygame.time.Clock()
#init
x=250
y=250
width = 700
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tic Tak Toe')
# def 


# def draw_grid():
    # pygame.draw.rect(screen, color_light_grey,(350,250,60,60))
    #pygame.draw.rect(screen,color_light_grey,(420,250,60,60))
    #pygame.draw.rect(screen,color_light_grey, (490,250,60,60))
    #pygame.draw.rect(screen, color_light_grey,(350,320,60,60))
    #pygame.draw.rect(screen, color_light_grey, (420,320,60,60))
    #pygame.draw.rect(screen, color_light_grey, (490,320,60,60))
    #pygame.draw.rect(screen, color_light_grey,(350,390,60,60))
    #pygame.draw.rect(screen, color_light_grey, (420,390,60,60))
    #pygame.draw.rect(screen, color_light_grey, (490,390,60,60))
# colors

color_white = (255,255,255)
color_black = (0,0,0)
color_light_grey = (200,200,200)
bg_color = pygame.Color('grey12')
orange = (255,165,0)
# <-- objects -->
first = pygame.draw.rect(screen, color_light_grey,(350,250,60,60))
second = pygame.draw.rect(screen,color_light_grey,(420,250,60,60))
third = pygame.draw.rect(screen,color_light_grey, (490,250,60,60))
fourth = pygame.draw.rect(screen, color_light_grey,(350,320,60,60))
fifth = pygame.draw.rect(screen, color_light_grey, (420,320,60,60))
sixth = pygame.draw.rect(screen, color_light_grey, (490,320,60,60))
seventh = pygame.draw.rect(screen, color_light_grey,(350,390,60,60))
eight = pygame.draw.rect(screen, color_light_grey, (420,390,60,60))
nine = pygame.draw.rect(screen, color_light_grey, (490,390,60,60))
list_of_sq = [first, second, third, fourth, fifth, sixth, seventh, eight, nine]
# if list_of_rect[i] is clicked then drawCircle in list_of_rect[i]
# square and circle
'''
def draw_square():
    pygame.draw.rect(screen, orange, (50,50), 16)
def drawCircle():
    pygame.draw.circle(screen, orange, (30,30), 16)
'''
# test program

draw_object = 'rect'
first_open = True
second_open = True
third_open = True
fourth_open = True
fifth_open = True
sixth_open = True
seventh_open = True
eighth_open = True
ninth_open = True
board = [[0,0,0], [0,0,0], [0,0,0]]
def check(num):
    for row in board:
        for tile in row:
            if tile == num:
                continue
            else:
                break
        else:
            return True
    
    for column in range(3):
        for row in board:
            if row[column] == num:
                continue
            else:
                break
        else:
            return True
    
    for tile in range(3):
        if board[tile][tile] == num:
            continue
        else:
            break
    else:
        return True

    for tile in range(3):
        if board[tile][2-tile] == num:
            continue
        else:
            break
    else:
        return True
# main loop
run = True
won = False



while run:

    key_pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                first = pygame.draw.rect(screen, color_light_grey,(350,250,60,60))
                second = pygame.draw.rect(screen,color_light_grey,(420,250,60,60))
                third = pygame.draw.rect(screen,color_light_grey, (490,250,60,60))
                fourth = pygame.draw.rect(screen, color_light_grey,(350,320,60,60))
                fifth = pygame.draw.rect(screen, color_light_grey, (420,320,60,60))
                sixth = pygame.draw.rect(screen, color_light_grey, (490,320,60,60))
                seventh = pygame.draw.rect(screen, color_light_grey,(350,390,60,60))
                eight = pygame.draw.rect(screen, color_light_grey, (420,390,60,60))
                nine = pygame.draw.rect(screen, color_light_grey, (490,390,60,60))
                
                won = False
                board = [[0,0,0], [0,0,0], [0,0,0]]
                first_open = True
                second_open = True
                third_open = True
                fourth_open = True
                fifth_open = True
                sixth_open = True
                seventh_open = True
                eighth_open = True
                ninth_open = True

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            if won != True: 
                if list_of_sq[0].collidepoint(pos) and first_open :
                    if draw_object == 'rect': 
                        pygame.draw.rect(screen, bg_color, (365,270,30,30))
                        draw_object = 'circle'
                        board[0][0] = 1
                    else:
                        pygame.draw.circle(screen, orange, (375,280), 17)
                        draw_object = 'rect'
                        board[0][0] = 2
                    first_open = False
                    
                if list_of_sq[1].collidepoint(pos) and second_open:
                    if draw_object == 'rect': 
                        pygame.draw.rect(screen, bg_color, (435,270,30,30))
                        draw_object = 'circle'
                        board[0][1] = 1
                    else:
                        pygame.draw.circle(screen, orange, (445,280), 17)  
                        draw_object = 'rect' 
                        board[0][1] = 2
                    second_open = False
                if list_of_sq[2].collidepoint(pos) and third_open:
                    if draw_object == 'rect': 
                        pygame.draw.rect(screen, bg_color, (500,270,30,30))
                        draw_object = 'circle'
                        board[0][2] = 1
                    else:
                        pygame.draw.circle(screen, orange, (510,280), 17)
                        draw_object = 'rect'
                        board[0][2]
                    third_open = False
                if list_of_sq[3].collidepoint(pos) and fourth_open:
                    if draw_object == 'rect': 
                        pygame.draw.rect(screen, bg_color, (365,340,30,30))
                        draw_object = 'circle'
                        board[1][0] = 1
                    else:
                        pygame.draw.circle(screen, orange, (375,350), 17)
                        draw_object = 'rect'
                        board[1][0] = 2
                    fourth_open = False

                if list_of_sq[4].collidepoint(pos) and fifth_open:
                    if draw_object == 'rect': 
                        pygame.draw.rect(screen, bg_color, (435,340,30,30))
                        draw_object = 'circle'
                        board[1][1] = 1
                    else:
                        pygame.draw.circle(screen, orange, (445,350), 17)
                        draw_object = 'rect'
                        board[1][1] = 2
                    fifth_open = False

                if list_of_sq[5].collidepoint(pos) and sixth_open:
                    if draw_object == 'rect': 
                        pygame.draw.rect(screen, bg_color, (500,340,30,30))
                        draw_object = 'circle'
                        board[1][2] = 1
                    else:
                        pygame.draw.circle(screen, orange, (510,350), 17)
                        draw_object = 'rect'
                        board[1][2] = 2
                    sixth_open = False

                if list_of_sq[6].collidepoint(pos) and seventh_open:
                    if draw_object == 'rect': 
                        pygame.draw.rect(screen, bg_color, (365,405,30,30))
                        draw_object = 'circle'
                        board[2][0] = 1
                    else: 
                        pygame.draw.circle(screen, orange, (380,420), 17)
                        draw_object = 'rect'
                        board[2][0] = 2
                    seventh_open = False

                if list_of_sq[7].collidepoint(pos) and eighth_open:
                    if draw_object == 'rect': 
                        pygame.draw.rect(screen, bg_color, (435,405,30,30))
                        draw_object = 'circle'
                        board[2][1] = 1
                    else:
                        pygame.draw.circle(screen, orange, (450,420), 17)
                        draw_object = 'rect'
                        board[2][1] = 1
                    eighth_open = False
                if list_of_sq[8].collidepoint(pos) and ninth_open:
                    if draw_object == 'rect': 
                        pygame.draw.rect(screen, bg_color, (500,405,30,30))
                        draw_object = 'circle'
                        board[2][2] = 1
                    else:
                        pygame.draw.circle(screen, orange, (515,420), 17)
                        draw_object = 'rect'
                        board[2][2] = 2
                    ninth_open = False
            
    if check(1):
        won = True
        if won == True:
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render('Player 1, Won!', True, orange, color_black)
                textRect = text.get_rect()  
                textRect.center = ( 455, 228) 
                screen.blit(text, textRect ) 
    if check(2):
        won = True
        if won == True:
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render('Player 2, Won! ', True, orange, color_black)
                textRect = text.get_rect()  
                textRect.center = ( 455, 228) 
                screen.blit(text, textRect ) 
    #draw_grid()

    '''
    if any of the rect in the list of rect is click then for make range(1,10), 1 is player 1 and even numbers are player 2. 
    range is 1 then its player is player 1. the range = 2, then player 2 turn. 
    ''' 
    pygame.display.update()
    clock.tick(60)
