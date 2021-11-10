from window import LabelObject


class Airport(LabelObject):
    def __init__(self, airPortName, horizontal_position, vertical_position):
        self.id = airPortName
        self.x = horizontal_position
        self.y = vertical_position
