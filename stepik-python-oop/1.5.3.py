class Point:
    def __init__(self, x, y, z='black'):
        self.x = x
        self.y = y
        self.color = z


points = [Point(2*i+1, 2*i+1) for i in range(0, 1000)]
points[1].color = 'yellow'
