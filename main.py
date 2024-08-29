import pygame
pygame.init()

screen = pygame.display.set_mode((1250,690))

class Circle:
    def __init__(self,x,y,radius,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
    def draw(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)
    def grow(self):
        self.radius += 5
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)
c1 = Circle(700,300,100,"green")

screen.fill("white")
    

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            c1.draw()
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONUP:
            c1.grow()
            pygame.display.update()
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            c2 = Circle(pos[0],pos[1],10,"black")
            c2.draw()
            pygame.display.update()