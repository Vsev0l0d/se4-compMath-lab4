from dataclasses import dataclass
from typing import Callable


@dataclass
class Function:
    function: Callable
    text: str
    S: float
