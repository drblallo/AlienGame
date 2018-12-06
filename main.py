import pygame
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255) ]

pygame.init()


matrix = []
rectSize = 70
offset = 10
rectCount = 7
extendedSize = offset + rectSize
windowSize = extendedSize * rectCount - offset

win = pygame.display.set_mode((windowSize, windowSize))
pygame.display.set_caption("Alien Tile")

for num in range(0, rectCount):
    raw = []

    for num2 in range(0, rectCount):
        raw.append(0)

    matrix.append(raw)

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            x = pos[0] / extendedSize
            y = pos[1] / extendedSize
            
            for num in range(0, rectCount):
                if num != x:
                    matrix[num][y] = (matrix[num][y] + 1) % 4
                if num != y:
                    matrix[x][num] = (matrix[x][num] + 1) % 4

            matrix[x][y] = (matrix[x][y] + 1)%4
            


    for x in range(0, rectCount):
        for y in range(0, rectCount):
            pygame.draw.rect(win, colors[matrix[x][y]], (x * extendedSize, y * extendedSize, rectSize, rectSize))
    pygame.display.update()

pygame.quit()
