class Target:
    def __init__(self, found, click_point):
        self.found = found
        self.click_point = click_point

    def __str__(self):
        return f'Target({self.found}, {self.click_point})'

class Monitor:
    def __init__(self, left, top, width, height, image):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.image = image
