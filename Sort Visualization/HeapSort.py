import random
import pygame

pygame.init()

#Visualize code for update the plot
def visualize(A):
    win.fill((0,0,0))
    show(A)
    pygame.display.update()
    #Delay option for slower visualitation
    #pygame.time.delay(5)

def heapify(A, N, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < N and A[largest] < A[l]:
        largest = l

    if r < N and A[largest] < A[r]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        visualize(A)
        heapify(A, N, largest)

#Heap sort recursive function
def heapsort(A):
    N = len(A)

    for i in range(N//2 -1, -1, -1):
        heapify(A, N, i)

    for i in range(N-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        visualize(A)
        heapify(A, i, 0)


#Setting Parameters
win = pygame.display.set_mode((840,500))
pygame.display.set_caption("HeapSort")

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
        heapsort(randomlist)
            
    #if execute == True:
    #     run = False

pygame.quit()