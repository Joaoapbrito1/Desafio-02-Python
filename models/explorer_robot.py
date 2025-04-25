class ExplorerRobot:
    def __init__(self, name, destination_planet, energy):
        self.name = name
        self.destination_planet = destination_planet
        self.energy = energy

    def __str__(self):
        return f"Robot {self.name} - Destination: {self.destination_planet} - Energy: {self.energy}%"