import random
import pygame

pygame.init()

#Setting Parameters
win = pygame.display.set_mode((840,500))
pygame.display.set_caption("SelectionSort")

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

    #Quit the loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #Starts when space key is pressed
    if keys[pygame.K_SPACE]:
        execute = True

    if execute == False:
        win.fill((0,0,0))
        show(randomlist)
        pygame.display.update()
    else:
        for i in range(len(randomlist)):
            min_index = i
            for j in range(i+1, len(randomlist)):
                if randomlist[min_index] > randomlist[j]:
                    min_index = j

            randomlist[i], randomlist[min_index] = randomlist[min_index], randomlist[i]
            win.fill((0,0,0))
            show(randomlist)
            pygame.display.update()
            #Delay option for slower visualitation
            #pygame.time.delay(50)
            
    #if execute == True:
    #     run = False

pygame.quit()
