import pygame
import math

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


class main:
    def __init__(self):
        self.width = 1600
        self.height = 900
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.unformated = 68
        self.pitchunformated = 170
        self.heading = math.radians(self.unformated)
        self.pitch = math.radians(self.pitchunformated)
        self.createform()
        self.headingTransform = Matrix([math.cos(self.heading),0,math.sin(self.heading),
                                        0,1,0,
                                        -math.sin(self.heading),0, math.cos(self.heading)])
        self.pitchtransform = Matrix([1,0,0,
                                      0,math.cos(self.pitch), math.sin(self.pitch),
                                      0, -math.sin(self.pitch), math.cos(self.pitch)])
        self.transform = self.headingTransform.muliply(self.pitchtransform)


    def createform(self):
        self.tris = []
        t1v1 = vertex(100, 100, 100)
        t1v2 = vertex(-100, -100, 100)
        t1v3 = vertex(-100, 100, -100)
        t1 = Triangle(t1v1,t1v2,t1v3, WHITE)
        self.tris.append(t1)

        t2v1 = vertex(100, 100, 100)
        t2v2 = vertex(-100, -100, 100)
        t2v3 = vertex(100, -100, -100)
        t2 = Triangle(t2v1, t2v2, t2v3, RED)
        self.tris.append(t2)

        t3v1 = vertex(-100, 100, -100)
        t3v2 = vertex(100, -100, -100)
        t3v3 = vertex(100, 100, 100)
        t3 = Triangle(t3v1, t3v2, t3v3, GREEN)
        self.tris.append(t3)

        t4v1 = vertex(-100, 100, -100)
        t4v2 = vertex(100, -100, -100)
        t4v3 = vertex(-100, -100, 100)
        t4 = Triangle(t4v1, t4v2, t4v3, BLUE)
        self.tris.append(t4)





    def updatetransform(self, heading, pitch):
        self.headingTransform = Matrix([math.cos(heading), 0, math.sin(heading),
                                        0, 1, 0,
                                        -math.sin(heading), 0, math.cos(heading)])
        self.pitchtransform = Matrix([1, 0, 0,
                                      0, math.cos(pitch), math.sin(pitch),
                                      0, -math.sin(pitch), math.cos(pitch)])
        self.transform = self.headingTransform.muliply(self.pitchtransform)



    def draw(self):
        self.screen.fill((0, 0, 0))
        for t in self.tris:
            v1 = self.transform.transform(t.v1)
            v2 = self.transform.transform(t.v2)
            v3 = self.transform.transform(t.v3)
            pygame.draw.line(self.screen, WHITE, (v1.x+self.width/2, v1.y+self.height/2), (v2.x+self.width/2, v2.y+self.height/2))
            pygame.draw.line(self.screen, WHITE, (v2.x+self.width/2, v2.y+self.height/2), (v3.x+self.width/2, v3.y+self.height/2))
            pygame.draw.line(self.screen, WHITE, (v1.x+self.width/2, v1.y+self.height/2), (v3.x+self.width/2, v3.y+self.height/2))

        blockvector = vertex(200,200,200)
        block = Block(blockvector, WHITE)
        vu1 = self.transform.transform(block.v1)
        vu2 = self.transform.transform(block.v2)
        vu3 = self.transform.transform(block.v3)
        vu4 = self.transform.transform(block.v4)
        vu5 = self.transform.transform(block.v5)
        vu6 = self.transform.transform(block.v6)
        vu7 = self.transform.transform(block.v7)
        vu8 = self.transform.transform(block.v8)


    def coloreddrawing(self):
        self.screen.fill((0, 0, 0))

        zBuffer = [0] * 160000
        for q in range (len(zBuffer)):
            zBuffer[q] = -math.inf

        for t in self.tris:
            v1 = self.transform.transform(t.v1)
            v2 = self.transform.transform(t.v2)
            v3 = self.transform.transform(t.v3)

            v1.x += 200
            v1.y += 200
            v2.x += 200
            v2.y += 200
            v3.x += 200
            v3.y += 200

            minX = max(0, math.ceil(min(v1.x, min(v2.x, v3.x))))
            maxX = min(400 - 1, math.floor(max(v1.x, max(v2.x, v3.x))))
            minY = max(0, math.ceil(min(v1.y, min(v2.y, v3.y))))
            maxY = min(400 - 1, math.floor(max(v1.y, max(v2.y, v3.y))))

            triangleArea = (v1.y - v3.y) * (v2.x - v3.x) + (v2.y - v3.y) * (v3.x - v1.x)

            for y in range(minY, maxY):
                for x in range(minX, maxX):
                    b1 = ((y - v3.y) * (v2.x - v3.x) + (v2.y - v3.y) * (v3.x - x)) / triangleArea
                    b2 = ((y - v1.y) * (v3.x - v1.x) + (v3.y - v1.y) * (v1.x - x)) / triangleArea
                    b3 = ((y - v2.y) * (v1.x - v2.x) + (v1.y - v2.y) * (v2.x - x)) / triangleArea
                    if b1 >= 0 and b1 <= 1 and b2 >= 0 and b2 <= 1 and b3 >= 0 and b3 <= 1:
                        depth = b1 * v1.z + b2 * v2.z + b3 * v3.z
                        zIndex = y * 400 + x
                        if(zBuffer[zIndex] < depth):
                            self.screen.set_at((x,y), t.color)
                            zBuffer[zIndex] = depth

    def run(self):
        running = True
        while running:
            #self.coloreddrawing()
            self.draw()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.unformated += 0.1
                self.heading = math.radians(self.unformated)
                self.updatetransform(self.heading, self.pitch)
            if keys[pygame.K_RIGHT]:
                self.unformated -= 0.1
                self.heading = math.radians(self.unformated)
                self.updatetransform(self.heading, self.pitch)
            if keys[pygame.K_DOWN]:
                self.pitchunformated += 0.1
                self.pitch = math.radians(self.pitchunformated)
                self.updatetransform(self.heading, self.pitch)
            if keys[pygame.K_UP]:
                self.pitchunformated -= 0.1
                self.pitch = math.radians(self.pitchunformated)
                self.updatetransform(self.heading, self.pitch)



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

class Block:
    def __init__(self, v ,color):
        self.v = v
        self.color = color
        self.v1 = vertex(v.x - 50, v.y - 50, v.z - 50)
        self.v2 = vertex(v.x + 50, v.y + 50, v.z - 50)
        self.v3 = vertex(v.x + 50, v.y + 50, v.z - 50)
        self.v4 = vertex(v.x + 50, v.y + 50, v.z + 50)
        self.v5 = vertex(v.x - 50, v.y - 50, v.z + 50)
        self.v6 = vertex(v.x - 50, v.y + 50, v.z + 50)
        self.v7 = vertex(v.x - 50, v.y + 50, v.z - 50)
        self.v8 = vertex(v.x + 50, v.y - 50, v.z + 50)

class Matrix:
    def __init__(self, values):
        self.values = values
    def muliply(self, other):
        result = [0] * 9
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




