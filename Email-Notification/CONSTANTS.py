from enum import Enum
import pathlib


class CONSTANTS(Enum):
    path = str(pathlib.Path(__file__).parent.absolute())
    email = "YourEmail"
    password = "YourPassword"
