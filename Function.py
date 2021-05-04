from dataclasses import dataclass
from typing import Callable


@dataclass
class Function:
    function: Callable
    text: str
    s: float
    root_mean_square_deviation: float
