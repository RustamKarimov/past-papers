from manim import *

from collections.abc import Sequence, Callable
from dataclasses import dataclass, field, asdict
from numpy import ndarray

from settings import stage_settings as ss

GRAPH_SETTINGS = {
    "x_range": [0, 1],
    "y_range": [0, 1],
    "x_length": 2,
    "y_length": 2,
    "axis_config": {
        "include_numbers": False,
        "include_ticks": False,
        "tip_width": 0.1,
        "tip_height": 0.1
    },
    "x_axis_config": {},
    "y_axis_config": {},
}

X_LABEL_SETTINGS = {
    "x_label": "x",
    "x_label_edge": UR,
    "x_label_direction": UR,
    "x_label_buff": 0.1,
    "x_label_font_size": ss.SMALL_TEX_SIZE,
    "x_label_rotation": 0,
}

Y_LABEL_SETTINGS = {
    "y_label": "y",
    "y_label_edge": UR,
    "y_label_direction": UR,
    "y_label_buff": 0.1,
    "y_label_font_size": ss.SMALL_TEX_SIZE,
    "y_label_rotation": 0,
}


def direct_proportion_function():
    return lambda x: x


@dataclass
class PlotSettings:
    x_range: Sequence[float] = field(default_factory=lambda: (0, 0.8))
    function: Callable = field(default_factory=direct_proportion_function)

    def as_dict(self):
        return asdict(self)


@dataclass
class AxisLabelSettings:
    axis: str = "x"
    label: str = "x"
    edge: ndarray = field(default_factory=lambda: UR)
    direction: ndarray = field(default_factory=lambda: UR)
    buff: float = 0.1
    font_size: int = ss.SMALL_TEX_SIZE
    angle: float = 0


@dataclass
class AxisConfig:
    include_numbers: bool = False
    include_ticks: bool = False
    tip_width: float = 0.1
    tip_height: float = 0.1

    def as_dict(self):
        return asdict(self)


@dataclass
class AxesSettings:
    x_range: Sequence[float] = field(default_factory=lambda: (0, 1))
    y_range: Sequence[float] = field(default_factory=lambda: (0, 1))
    x_length: int = 2
    y_length: int = 2
    axis_config: AxisConfig = field(default_factory=AxisConfig)

    def as_dict(self):
        return asdict(self)


@dataclass
class GraphSettings:
    axes_settings: AxesSettings = field(default_factory=AxesSettings)
    x_label_settings: AxisLabelSettings = field(default_factory=AxisLabelSettings)
    y_label_settings: AxisLabelSettings = field(default_factory=AxisLabelSettings)
    plot_settings: PlotSettings = field(default_factory=PlotSettings)


@dataclass
class GraphParts:
    axes: Axes
    x_label: Mobject
    y_label: Mobject
    plot: Mobject
