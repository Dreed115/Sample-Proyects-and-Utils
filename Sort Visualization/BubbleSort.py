import random
import pygame

pygame.init()

#Setting Parameters
win = pygame.display.set_mode((840,500))
pygame.display.set_caption("BubbleSort")

y = 500
width = 1

#Generate a random list of numbers to be sort
randomlist = []
run = True

for i in range(0, 200):
    n = random.randint(0,450)
    randomlist.append(n)

def show(heigh):
    for i in range(len(heigh)):
        pygame.draw.rect(win, (255,255,255), (4*i+20, y-heigh[i], width, heigh[i]))

while run:
    execute = False
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if keys[pygame.K_SPACE]:
        execute = True

    if execute == False:
        win.fill((0,0,0))
        show(randomlist)
        pygame.display.update()
    else:
        for i in range(len(randomlist)-1):
            for j in range(len(randomlist)-1):
                if randomlist[j] > randomlist[j+1]:
                    randomlist[j], randomlist[j+1] = randomlist[j+1], randomlist[j]
                
                win.fill((0,0,0))
                show(randomlist)
                pygame.display.update()
                #Delay option for slower visualitation
                #pygame.time.delay(50)
    #if execute == True:
    #     run = False

pygame.quit()
