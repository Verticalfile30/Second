import pygame
import random
pygame.init()

#Graphics and constants

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Race')
clock = pygame.time.Clock()

carImg = pygame.image.load('Racecar.png')
#definitions
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
car_width = 53

def car(x,y):
    gameDisplay.blit(carImg,(x,y))
#game manager
def game_loop(): 

    x = (display_width * 0.45)

    y = (display_height * 0.45)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    crashed = False
    #event manager
    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        
        gameDisplay.fill(white)

        #AI Manager
        things(thing_startx, thing_starty, thing_height, thing_width, black)
        thing_starty += thing_speed
        car(x,y,)   
        
        if x > display_width or x < 0:
            crashed = True
        
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
        if y < thing_starty+thing_height:
            print ('y cross')
            
            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                print ('x')
                crashed = True
        pygame.display.update()
        clock.tick(60)
game_loop()
pygame.quit()
quit()

