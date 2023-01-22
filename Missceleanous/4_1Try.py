import math

import matplotlib.pyplot as plt

def solution(dimensions, your_position, trainer_position, distance):
    boundingBox = []
    topRight = Point(dimensions[0], dimensions[1])
    boundingBox.append(Line(Point(0, 0), Point(dimensions[0], 0)))          # Bottom edge
    boundingBox.append(Line(Point(0, 0), Point(0, dimensions[1])))          # Left edge
    boundingBox.append(Line(Point(0, dimensions[1]), topRight))             # Top edge
    boundingBox.append(Line(Point(dimensions[0], 0), topRight))             # Right edge
    # plt.figure(figsize=(14, 9))
    [plt.plot([wall.point1.x, wall.point2.x], [wall.point1.y, wall.point2.y], color="blue") for wall in boundingBox]

    yourPos = Point(your_position[0], your_position[1])
    trnPos = Point(trainer_position[0], trainer_position[1])
    plt.plot(yourPos.x, yourPos.y, color="green", marker="o")
    plt.plot(trnPos.x, trnPos.y, color="red", marker="o")
    direction = Point(-3,-1)

    # plt.plot([yourPos.x, direction.x], [yourPos.y, direction.y], color="black")
    lineToDir = Line(direction,yourPos)
    reflection = boundingBox[0].getReflection(lineToDir,yourPos)
    intersection = boundingBox[0].getIntersectionWithLine(lineToDir)
    print(reflection)
    plt.plot([yourPos.x, direction.x], [yourPos.y, direction.y], color="black")
    plt.plot([reflection.point1.x,reflection.point2.x], [reflection.point1.y,reflection.point2.y], color="black")
    # plt.plot([reflection.point1.x], [reflection.point1.y],'o', color="black")
    # plt.plot([reflection.point2.x], [reflection.point2.y],'o', color="black")
    # normal = boundingBox[3].getNormal(boundingBox[3].getIntersectionWithLine(lineToDir),yourPos)
    # print(normal)
    # plt.plot([normal.point1.x,normal.point2.x],[normal.point1.y,normal.point2.y])

    # colors= ["red", "green", "blue", "yellow", "purple", "orange", "pink", "black", "brown", "gray", "olive", "cyan"]
    # for i in range(-dimensions[0] ,dimensions[0]+1):
    #     for j in range(-dimensions[1], dimensions[1]+1):
    #         direction = Point(i, j)
    #         intersections = simulateRay(boundingBox, yourPos, direction, distance)
    #         for normal in intersections:
    #         # for point in intersections:
    #             # xList.append(point.x)
    #             # yList.append(point.y)
    #             xList = []
    #             yList = []
    #             xList.append(normal.point1.x)
    #             xList.append(normal.point2.x)
    #             yList.append(normal.point1.y)
    #             yList.append(normal.point2.y)
    #             plt.plot(xList, yList, colors[((i*dimensions[0])+j)%len(colors)])
    plt.show()


def simulateRay(boundingBox, startPos, direction, distance):
    direction.add(startPos)
    bullet = Line(startPos, direction)

    intersects = []
    normals = []
    for wall in boundingBox:
        intersect = wall.getIntersectionWithLine(Line(startPos, direction))
        if intersect is not None and isInBounds(wall, intersect):
            normal = wall.getNormal(intersect,startPos)
            if normal is not None:
                normals.append(normal)
            intersects.append(intersect)
    return normals

def isInBounds(wall,point):
    return wall.point1.x <= point.x <= wall.point2.x and wall.point1.y <= point.y <= wall.point2.y


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def add(self, other):
        self.x += other.x
        self.y += other.y

    def getDistance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    def getVector(self, other):
        return other.x - self.x, other.y - self.y

    def getUnitVector(self, other):
        x, y = self.getVector(other)
        dist = self.getDistance(other)
        return x/dist, y/dist

    def getPoint(self, vector, distance):
        x, y = vector
        return Point(self.x + x*distance, self.y + y*distance)

    def getIntersection(self, other, distance):
        vector = self.getUnitVector(other)
        return self.getPoint(vector, distance)


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def __str__(self):
        return "{0} - {1}".format(self.point1, self.point2)

    def getDistance(self, point):
        return point.getDistance(self.point1)

    def getIntersection(self, point, distance):
        return self.point1.getIntersection(point, distance)

    def getIntersectionWithLine(self, other):
        # Returns the intersection of the two lines
        # Returns None if the lines are parallel
        x1, y1 = self.point1.x, self.point1.y
        x2, y2 = self.point2.x, self.point2.y
        x3, y3 = other.point1.x, other.point1.y
        x4, y4 = other.point2.x, other.point2.y
        denom = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
        if denom == 0:
            return None
        x = ((x1*y2 - y1*x2)*(x3-x4) - (x1-x2)*(x3*y4 - y3*x4))/denom
        y = ((x1*y2 - y1*x2)*(y3-y4) - (y1-y2)*(x3*y4 - y3*x4))/denom
        if x==-0:
            x = 0
        if y==-0:
            y = 0
        return Point(x, y)

    def getReflection(self, otherLine, yourPos):
        # Returns the reflection of the line off of the other line
        # Returns None if the lines are parallel
        intersection = self.getIntersectionWithLine(otherLine)
        if intersection is None:
            return None
        normal = self.getNormal(intersection, yourPos)
        m1 = otherLine.getSlope()
        m2 = normal.getSlope()
        print("m1: {0}, m2: {1}".format(m1,m2))
        # Since angle of incidence between self's normal and otherLine is same as angle b/w normal and newLine
        m3 = m1 - (2*m2) - (m1*m2*m2)/((m2*m2) - 2*(m1*m2) - 1)
        if m2==math.inf or m1==math.inf:
            m3= 0
        b = intersection.y - (m3 * intersection.x)  # y = mx + b => b = y - mx
        anotherPointOnReflection = Point(yourPos.x, (yourPos.x * m3) + b)
        return Line(intersection, anotherPointOnReflection)

    def getSlope(self):
        if self.point2.x - self.point1.x != 0:
            return (self.point2.y-self.point1.y)/(self.point2.x-self.point1.x)
        else:
            return math.inf

    def getNormal(self, intersection, yourPosition):
        if self.point2.x-self.point1.x!=0:
            slope = self.getSlope()
            if slope == 0:
                return Line(intersection,Point(intersection.x,yourPosition.y))
            normalSlope = 1/slope
        else:
            normalSlope=0

        b = intersection.y - (normalSlope*intersection.x)                    # y = mx + b => b = y - mx
        # print(normalSlope)
        anotherPointOnNormal = Point(yourPosition.x,(yourPosition.x*normalSlope)+b)
        # print(anotherPointOnNormal)
        return Line(intersection,anotherPointOnNormal)



if __name__ == '__main__':
    solution([3, 2], [1, 1], [2, 1], 4)
