import pygame
import math

WHITE = (255,255,255)


class main:
    def __init__(self):
        (width, height) = (400,400)
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.unformated = 120
        self.heading = math.radians(self.unformated)
        self.createform()
        self.transform = Matrix([math.cos(self.heading),0, -math.sin(self.heading),
                                 0,1,0,
                                 math.sin(self.heading), 0, math.cos(self.heading)])


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

    def updatetransform(self, heading):
        self.transform = Matrix([math.cos(heading), 0, -math.sin(heading),
                                 0, 1, 0,
                                 math.sin(heading), 0, math.cos(heading)])

    def draw(self):
        self.screen.fill((0, 0, 0))
        for t in self.tris:
            v1 = self.transform.transform(t.v1)
            v2 = self.transform.transform(t.v2)
            v3 = self.transform.transform(t.v3)
            pygame.draw.line(self.screen, WHITE, (v1.x+200, v1.y+200), (v2.x+200, v2.y+200))
            pygame.draw.line(self.screen, WHITE, (v2.x+200, v2.y+200), (v3.x+200, v3.y+200))
            pygame.draw.line(self.screen, WHITE, (v1.x+200, v1.y+200), (v3.x+200, v3.y+200))

    def run(self):
        running = True
        while running:
            self.draw()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.unformated += 0.01
                self.heading = math.radians(self.unformated)
                self.updatetransform(self.heading)
            if keys[pygame.K_RIGHT]:
                self.unformated -= 0.01
                self.heading = math.radians(self.unformated)
                self.updatetransform(self.heading)



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

class Matrix:
    def __init__(self, values):
        self.values = values
    def muliply(self, other):
        result = []
        for row in range(3):
            for col in range(3):
                for i in range(3):
                    result[row * 3 + col] += self.values[row * 3 + i] * other.values[i * 3 + col]
        return Matrix(result)

    def transform(self, input):
        return vertex(
            input.x * self.values[0] + input.y * self.values[3] + input.z * self.values[6],
            input.x * self.values[1] + input.y * self.values[4] + input.z * self.values[7],
            input.x * self.values[2] + input.y * self.values[5] + input.z * self.values[8],
        )



if __name__ == "__main__":
    main = main()
    main.run()




