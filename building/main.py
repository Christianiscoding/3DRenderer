import pygame


WHITE = (255,255,255)

class main:
    def __init__(self):
        (width, height) = (400,400)
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.flip()
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    def createform(self):
        self.tris = []
        t1v1 = vertex(100, 100, 100)
        t1v2 = vertex(-100, -100, 100)
        t1v3 = vertex(-100, 100, -100)
        t1 = Triangle(t1v1,t1v2,t1v3,WHITE)
        self.tris.append(t1)

        t2v1 = vertex(100, 100, 100)
        t2v2 = vertex(-100, -100, 100)
        t2v3 = vertex(100, -100, -100)
        t2 = Triangle(t2v1, t2v2, t2v3, WHITE)
        self.tris.append(t2)

        t3v1 = vertex(-100, 100, -100)
        t3v2 = vertex(100, -100, -100)
        t3v3 = vertex(100, 100, 100)
        t3 = Triangle(t3v1, t3v2, t3v3, WHITE)
        self.tris.append(t3)

        t4v1 = vertex(-100, 100, -100)
        t4v2 = vertex(100, -100, -100)
        t4v3 = vertex(-100, -100, 100)
        t4 = Triangle(t4v1, t4v2, t4v3, WHITE)
        self.tris.append(t4)

    def draw(self):
        for t in self.tris:
            pygame.draw.line(self.screen, WHITE, (t.v1.x+200, t.v1.y+200), (t.v2.x+200, t.v2.y+200))
            pygame.draw.line(self.screen, WHITE, (t.v2.x+200, t.v2.y+200), (t.v3.x+200, t.v3.y+200))
            pygame.draw.line(self.screen, WHITE, (t.v1.x+200, t.v1.y+200), (t.v3.x+200, t.v3.y+200))
            pygame.display.flip()

    def printit(self):
        print(self.tris[0].v1.x)



class vertex:
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

class Triangle:
    def __init__(self, v1, v2, v3, color):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.color = color


if __name__ == "__main__":
    main = main()
    main.createform()
    main.printit()
    main.draw()
    main.run()




