import numpy as np
from manim import *

from dataclasses import dataclass, field

from typing import List

from settings import stage_settings as ss


@dataclass
class IndividualAction:
    name: str
    target: str
    function: str
    function_kwargs: dict = field(default_factory=lambda: {})


@dataclass
class Action:
    function: str
    kwargs: dict


@dataclass
class Section:
    parts: list
    individual_actions: List[IndividualAction] = field(default_factory=lambda: [])
    actions: List[Action] = field(default_factory=lambda: [])


@dataclass
class DiagramPart:
    label: str
    function: type = None
    position_function: str = None
    rotation_angle: float = 0
    scale: float = 1
    actions_to_take: List = field(default_factory=lambda: [])
    reference: str = None

    function_args: list = field(default_factory=lambda: [])
    position_args: list = field(default_factory=lambda: [])
    rotation_args: list = field(default_factory=lambda: [])

    function_kwargs: dict = field(default_factory=lambda: {})
    position_kwargs: dict = field(default_factory=lambda: {})
    rotation_kwargs: dict = field(default_factory=lambda: {})

