import numpy as np
from manim import *

from dataclasses import dataclass, field

from settings import stage_settings as ss


class Label:
    label: str
    position: np.ndarray = ORIGIN
    color: str = ss.TEXT_COLOR
    font_size: int = ss.MEDIUM_TEX_SIZE
    buff: float = 0
    angle: float = 0


@dataclass
class Surface:
    shape: object = field(default_factory=Line)

