from models.explorer_robot import ExplorerRobot
from models.mission_report import MissionReport

def main():
    robot = ExplorerRobot("Xablau", "Mars", 87)
    print(robot) 

    readings = (
        ("temperature", -50),
        ("radiation", 2.5),
    )
    report = MissionReport("Xablau", "Mars", 87, readings)
    print(report.summary())         
    print(report.readings_count())

if __name__ == "__main__":
    main()