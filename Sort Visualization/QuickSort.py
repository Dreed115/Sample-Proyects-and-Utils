import random
import pygame

pygame.init()

#Visualize code for update the plot
def visualize(A):
    win.fill((0,0,0))
    show(A)
    pygame.display.update()
    #Delay option for slower visualitation
    #pygame.time.delay(10)

#Partition function to 
def partition(A, low, high):
    #Right pivot
    pivot = A[high]
    i = low-1

    for j in range(low, high):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
            visualize(A)

    A[i+1], A[high] = A[high], A[i+1]
    visualize(A)
    return i+1

#Quick sort recursive function
def quicksort(A, low, high):
    if low < high:
        pi = partition(A, low, high)
        quicksort(A, low, pi-1)
        quicksort(A, pi+1, high)


#Setting Parameters
win = pygame.display.set_mode((840,500))
pygame.display.set_caption("QuickSort")

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
        quicksort(randomlist, 0, len(randomlist)-1)
            
    #if execute == True:
    #     run = False

pygame.quit()