import random
import pygame

pygame.init()

def visualize(A):
    win.fill((0,0,0))
    show(A)
    pygame.display.update()
    #Delay option for slower visualitation
    #pygame.time.delay(10)

#Merge sort recursive function
def mergesort(A):
    visualize(A)
    if len(A) > 1:
        mid = len(A)//2
        left = A[:mid]
        right = A[mid:]

        mergesort(left)
        mergesort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1
            visualize(A)

        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1
            visualize(A)

        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1
            visualize(A)


#Setting Parameters
win = pygame.display.set_mode((840,500))
pygame.display.set_caption("MergeSort")

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
        mergesort(randomlist)
            
    #if execute == True:
    #     run = False

pygame.quit()