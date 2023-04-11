class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def get_width(self):
        return self._width

    def set_width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self._width = width

    def get_height(self):
        return self._height

    def set_height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self._height = height

    width = property(get_width, set_width)
    height = property(get_height, set_height)
