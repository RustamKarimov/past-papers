from manim import *

from collections.abc import Sequence, Callable
from dataclasses import dataclass, field, asdict
from numpy import ndarray

from settings import stage_settings as ss


def direct_proportion_function():
    return lambda x: x


@dataclass
class PlotSettings:
    """
    A Dataclass consisting of x_range and function fields which are required to plot a graph.
    x_range: range for which graph will be plotted.
    function: function used to plot the graph
    """
    x_range: Sequence[float] = field(default_factory=lambda: (0, 0.8))
    function: Callable = field(default_factory=direct_proportion_function)

    def as_dict(self):
        """
        Converts the fields of the class to a dictionary
        :return: dictionary version of the class
        """
        return asdict(self)


@dataclass
class AxisLabelSettings:
    """
    A dataclass consisting of fields required for the labeling an axis of a graph.
    axis: axis to tbe labeled (by default it is "x" axis)
    label: The label of the given axis
    edge: Position of the label due to the axis
    direction: Direction of the label due to the axis
    buff: Distance of the label from the axis
    font_size: The font size of the label
    angle: An angle of rotation for the label
    """
    axis: str = "x"
    label: str = "x"
    edge: ndarray = field(default_factory=lambda: UR)
    direction: ndarray = field(default_factory=lambda: UR)
    buff: float = 0.1
    font_size: int = ss.SMALL_TEX_SIZE
    angle: float = 0


@dataclass
class AxisConfig:
    """
    Axis configuration settings for the graph.
    include_numbers: If numbers will be displayed or not (by default they are not displayed)
    include_numbers: If ticks will be displayed or not (by default they are not displayed)
    tip_width: width of the tip of the axis (by default it's 0.1)
    tip_height: height of the tip of the axis (by default it's 0.1)
    """
    include_numbers: bool = False
    include_ticks: bool = False
    tip_width: float = 0.1
    tip_height: float = 0.1

    def as_dict(self):
        """
        Converts the fields of the class to a dictionary
        :return: dictionary version of the class
        """
        return asdict(self)


@dataclass
class AxesSettings:
    """
    A dataclass consisting of settings to draw an axes for a graph.
    x_range: range of x values to be represented on the graph
    y_range: range of y values to be represented on the graph
    x_length: length of x axis
    y_length: length of y axis
    axis_config: Configurations for both axes
    """
    x_range: Sequence[float] = field(default_factory=lambda: (0, 1))
    y_range: Sequence[float] = field(default_factory=lambda: (0, 1))
    x_length: int = 2
    y_length: int = 2
    axis_config: AxisConfig = field(default_factory=AxisConfig)

    def as_dict(self):
        """
        Converts the fields of the class to a dictionary
        :return: dictionary version of the class
        """
        return asdict(self)


@dataclass
class GraphSettings:
    """
    A dataclass consisting of settings for various parts of a graph.
    axes_settings: settings for axes
    x_label_settings: settings for the label of x axis
    y_label_settings: settings for the label of y axis
    plot_settings: settings of the plot on the graph
    """
    axes_settings: AxesSettings = field(default_factory=AxesSettings)
    x_label_settings: AxisLabelSettings = field(default_factory=AxisLabelSettings)
    y_label_settings: AxisLabelSettings = field(default_factory=AxisLabelSettings)
    plot_settings: PlotSettings = field(default_factory=PlotSettings)


@dataclass
class GraphParts:
    """
    A dataclass to keep record of the various parts of the graph.
    axes: an Axes object
    x_label: Label generated for the label of x axis on the graph
    y_label: Label generated for the label of y axis on the graph
    plot: the plot mobject
    """
    axes: Axes
    x_label: Mobject
    y_label: Mobject
    plot: Mobject
