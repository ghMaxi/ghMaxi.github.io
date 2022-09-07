from airport import Airport
from window import AirportProgramWindow
from plane import Plane


if __name__ == "__main__":
    window = AirportProgramWindow()
    sheremetyevo = Airport("Шереметьево", -1, -5)
    vnukovo = Airport("Внуково", -4, 4)
    plane1 = Plane("AN2022", sheremetyevo)

    window.display(sheremetyevo)
    window.display(vnukovo)

    plane1.fly_to(vnukovo, window)

    window.mainloop()
