import tkinter


class LabelObject:
    x: int
    y: int
    id: str

    @property
    def symbol(self):
        return 'о'


class AirportProgramWindow(tkinter.Tk):
    scale = 10

    def display(self, to_draw: LabelObject):
        scale = AirportProgramWindow.scale
        label2 = tkinter.Label(self, text=to_draw.symbol)
        label2.place(x=100 + to_draw.x * scale, y=100 + to_draw.y * scale, anchor='center')
        label = tkinter.Label(self, text=to_draw.id)
        label.place(x=103 + to_draw.x * scale, y=90 + to_draw.y * scale)
