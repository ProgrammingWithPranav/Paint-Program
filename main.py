import pygame
import random

print("This is a paint program I wrote using Python and Pygame")
print("There are nine colours in this program. Red is the default colour.")
print("Press the following keys for the spesific colours:")
print("Red = r")
print("Green = g")
print("Yellow = y")
print("Blue = b")
print("Black = l")
print("White = w")
print("Purple = p")
print("Brown = a")
print("Grey = x")
input("press enter to continue")
screen = pygame.display.set_mode((1200,700))

draw_on = False
last_pos = (0, 0)
color = (0,0,0)
radius = 10

screen.fill((255,255,255))
pygame.draw.rect(screen, (0,0,0), (0,0,1200,600))

def roundline(srf, color, start, end, radius=1):
    dx = end[0]-start[0]
    dy = end[1]-start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int( start[0]+float(i)/distance*dx)
        y = int( start[1]+float(i)/distance*dy)
        pygame.draw.circle(srf, color, (x, y), radius)

try:
    while True:
        clr = (255,0,0)
        e = pygame.event.wait()
        if e.type == pygame.QUIT:
            raise StopIteration
        if e.type == pygame.KEYDOWN:
            if e.type == pygame.K_r:
                if e.type == pygame.MOUSEBUTTONDOWN:
                    color = (255,0,0)
                    pygame.draw.circle(screen, color, e.pos, radius)
                    draw_on = True
                pygame.display.update()
            if e.type == pygame.K_g:
                if e.type == pygame.MOUSEBUTTONDOWN:
                    color = (clr)
                    pygame.draw.circle(screen, color, e.pos, radius)
                    draw_on = True
                pygame.display.update()
        if e.type == pygame.MOUSEBUTTONDOWN:
            color = (clr)
            pygame.draw.circle(screen, color, e.pos, radius)
            draw_on = True
        if e.type == pygame.MOUSEBUTTONUP:
            draw_on = False
        if e.type == pygame.MOUSEMOTION:
            if draw_on:
                pygame.draw.circle(screen, color, e.pos, radius)
                roundline(screen, color, e.pos, last_pos,  radius)
            last_pos = e.pos
        pygame.display.flip()

except StopIteration:
    pass

pygame.quit()