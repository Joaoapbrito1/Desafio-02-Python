# Planetary Robot Mission Control

This project is a simple system to control explorer robots that perform missions on planets and send reports with collected data to the command base.

## Features

- Define explorer robots with name, destination planet, and energy level.
- Create mission reports with sensor readings.
- Summarize and count collected data.
- Unit tests using pytest.

## Project Structure

- explorer_robot.py     # ExplorerRobot class
- mission_report.py     # MissionReport class (inherits from ExplorerRobot)
- main.py               # Example usage of the classes
- test_robot.py         # Unit tests with pytest
- README.md             # Project documentation

## Usage
1. Clone the repository:
 ```bash
 git clone [https://github.com/Joaoapbrito1/Desafio-02-Python.git](https://github.com/Joaoapbrito1/Desafio-02-Python.git)

```
2. Install dependencies (for testing):
```bash
pip install pytest
```
3. Run the main example:
```bash
python main.py
```
4. Run the tests:
```bash
pytest test_robot.py
```
## Tests

The project includes tests to verify:

- The correct behavior of the ExplorerRobot class.
- Proper inheritance in the MissionReport class.
- The summary and readings_count methods.

Run all tests with:

```bash
pytest test_robot.py
```
## License

MIT License