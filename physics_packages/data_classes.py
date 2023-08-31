from manim import *
from dataclasses import dataclass

from settings import stage_settings as ss


# Electrostatics
@dataclass
class PartOfDiagram:
    height: int = 0.5
    width: int = 4
    stroke_color: color = ss.TEXT_COLOR
    stroke_width: int = 1
    fill_color: color = ss.TEXT_COLOR
    fill_opacity: int = 1
    rotation: int = 90
