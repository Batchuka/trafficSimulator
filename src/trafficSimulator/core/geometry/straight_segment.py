from .segment import Segment

CURVE_RESOLUTION = 50

class StraightSegment(Segment):

    def __init__(self, start, end):
        # Store characteristic points
        self.start = start
        self.end = end

        # Generate path
        path = [self.start, self.end]
        for i in range(CURVE_RESOLUTION):
            t = i / (CURVE_RESOLUTION - 1)
            x = (1 - t) * self.start[0] + t * self.end[0]
            y = (1 - t) * self.start[1] + t * self.end[1]
            path.append((x, y))

        super().__init__(path)

        # # Arc-length parametrization
        # normalized_path = self.find_normalized_path(CURVE_RESOLUTION)
        # super().__init__(normalized_path)

        # Arc-length parametrization
        normalized_path = self.find_normalized_path(CURVE_RESOLUTION)
        super().__init__(normalized_path)

    def compute_x(self, t):
        return (1 - t) * self.points[0][0] + t * self.points[1][0]

    def compute_y(self, t):
        return (1 - t) * self.points[0][1] + t * self.points[1][1]

    def compute_dx(self, t):
        return self.points[1][0] - self.points[0][0]

    def compute_dy(self, t):
        return self.points[1][1] - self.points[0][1]