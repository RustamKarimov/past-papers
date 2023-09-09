import numpy as np
from manim import *

from dataclasses import dataclass, field

from settings import stage_settings as ss


@dataclass
class DiagramPart:
    label: str
    function: type = None
    position_function: str = None
    rotation_angle: float = 0
    scale: float = 1

    function_kwargs: dict = field(default_factory=lambda: {})
    position_kwargs: dict = field(default_factory=lambda: {})
    rotation_kwargs: dict = field(default_factory=lambda: {})

