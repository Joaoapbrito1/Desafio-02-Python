from models.explorer_robot import ExplorerRobot

class MissionReport(ExplorerRobot):
    def __init__(self, name, destination_planet, energy, readings):
        super().__init__(name, destination_planet, energy)
        self.readings = readings

    def summary(self):
        return [f"{data_type}: {value}" for data_type, value in self.readings]

    def readings_count(self):
        return len(self.readings)