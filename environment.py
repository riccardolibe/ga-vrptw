from roadmap import RoadMap


class Environment:
    def __init__(self, n):
        self.roadmap = RoadMap(n)
        self.time = 0

    def tic(self, h = 1):
        self.time = (self.time + h) % 24
