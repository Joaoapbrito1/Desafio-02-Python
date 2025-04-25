import pytest
from models.explorer_robot import ExplorerRobot
from models.mission_report import MissionReport

def test_explorer_robot_str():
    robot = ExplorerRobot("Xablau", "Mars", 87)
    assert str(robot) == "Robot Xablau - Destination: Mars - Energy: 87%"

def test_mission_report_inheritance():
    report = MissionReport("Xablau", "Mars", 87, ())
    assert isinstance(report, ExplorerRobot)

def test_mission_report_summary_and_count():
    readings = (
        ("temperature", -50),
        ("radiation", 2.5),
    )
    report = MissionReport("Xablau", "Mars", 87, readings)
    assert report.summary() == ["temperature: -50", "radiation: 2.5"]
    assert report.readings_count() == 2