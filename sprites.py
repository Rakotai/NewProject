import pygame, sys, random
pygame.init()
screen = pygame.display.set_mode((820, 500), pygame.RESIZABLE)
caption = pygame.display.set_caption('Space Invades V2')

walkRight = [pygame.image.load(r'C:\Users\61404\Desktop\learnpygame\Game\R1.png'), 
            pygame.image.load(r'C:\Users\61404\Desktop\learnpygame\Game\R2.png'), 
            pygame.image.load(r'C:\Users\61404\Desktop\learnpygame\Game\R3.png'), 
            pygame.image.load(r'C:\Users\61404\Desktop\learnpygame\Game\R4.png'), 
            pygame.image.load(r'C:\Users\61404\Desktop\learnpygame\Game\R5.png'), 
            pygame.image.load(r'C:\Users\61404\Desktop\learnpygame\Game\R6.png'), 
            pygame.image.load(r'C:\Users\61404\Desktop\learnpygame\Game\R7.png'), 
            pygame.image.load(r'C:\Users\61404\Desktop\learnpygame\Game\R8.png'),
            pygame.image.load(r'C:\Users\61404\Desktop\learnpygame\Game\R9.png')]

walkLeft = [pygame.image.load(r'C:\Users\61404\Desktop\learnpygame\Game\L1E.png'),
            pygame.image.load(r'C:\Users\61404\Desktop\learnpygame\Game\L2E.png'), 
            pygame.image.load(r'C:\Users\61404\Desktop\learnpygame\Game\L3E.png'), 
            pygame.image.load(r'C:\Users\61404\Desktop\learnpygame\Game\L4E.png'), 
            pygame.image.load(r'C:\Users\61404\Desktop\learnpygame\Game\L5E.png'), 
            pygame.image.load(r'C:\Users\61404\Desktop\learnpygame\Game\L6E.png'), 
            pygame.image.load(r'C:\Users\61404\Desktop\learnpygame\Game\L7E.png'), 
            pygame.image.load(r'C:\Users\61404\Desktop\learnpygame\Game\L8E.png'), 
            pygame.image.load(r'C:\Users\61404\Desktop\learnpygame\Game\L9E.png')]

background_image = pygame.image.load(r'C:\Users\61404\Desktop\Game\background_img.jpg')
standing_image = pygame.image.load(r'C:\Users\61404\Desktop\learnpygame\Game\standing.png')

clock = pygame.time.Clock()


class Player():
    def __init__(self,x,y,width,height,screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 5
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 20, self.y + 20, 30, 52)
        self.screen = screen

        #colo
        self.color_red = (194,24,7)
        self.color_blue = (0,0,255)
        self.color_orange = (255,165,0)
        self.color_yellow = (255,255,100)
        self.light_grey = (200,200,200)
        self.background = pygame.Color('grey12')
        self.new_bg = pygame.image.load(r'C:\Users\61404\Desktop\Game\background_img.jpg')
        pygame.transform.scale(self.new_bg, (850,510))
        self.box1 = pygame.Rect((self.width/2 - 100, self.height/2 - 100), (60,60))
        self.box2 = pygame.Rect((self.width/2 - 100, self.height/2 - 100), (60,60))
        self.box3 = pygame.Rect((self.width/2 - 100, self.height/2 - 100), (60,60))
        self.box_speed = 8

    def draw(self, screen):
        screen.blit(self.new_bg, (20,20))
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            screen.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            screen.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            screen.blit(standing_image, (self.x,self.y))

        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        pygame.draw.rect(screen, self.color_orange, self.hitbox,2)

    def moving_box(self, screen):
            self.box1.y += self.box_speed
            self.box2.y += self.box_speed - 1
            self.box3.y += self.box_speed + 1
            if self.box1.y and self.box2.y and self.box3.y > self.height and self.x > 100:
                self.box1.x = random.randrange(0, self.width-400)
                self.box1.y = -100
                self.box2.x = random.randrange(0, self.width-400)
                self.box2.y = -100
                self.box3.x = random.randrange(0, self.width-400)
                self.box3.y = -100
            pygame.draw.rect(self.screen, self.light_grey, self.box1)
            pygame.draw.rect(self.screen,self.light_grey, self.box2)
            pygame.draw.rect(self.screen,self.light_grey, self.box3)
            pygame.draw.rect(self.screen, self.light_grey, (0, 0, self.width,30))

man = Player(0,440,850,500, screen)


run = True
while run:
    clock.tick(30)
    keyPressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            sys.exit()
            run = False
    if keyPressed[pygame.K_a] and man.x > 15:
        man.left = True
        man.right = False
        man.x  -= man.speed
    elif keyPressed[pygame.K_d] and man.x < man.width - 85:
        man.right = True
        man.left = False
        man.x += man.speed
    else:
        man.right = False
        man.left = False
        man.walkCount = 0

        if keyPressed[pygame.K_SPACE]:
            man.speed = 15
        else:
            man.speed = 8
            
    
    if man.box1.colliderect(man.hitbox) or man.box2.colliderect(man.hitbox) or man.box3.colliderect(man.hitbox):
        sys.exit()

    pygame.display.update()

    man.draw(screen)
    man.moving_box(screen)

