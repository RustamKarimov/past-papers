from manim import *

from settings import graph_settings as gs


def generate_axis_label(axes: Axes, label_settings: gs.AxisLabelSettings) -> Mobject:
    """
    Generates label for the specified axis.
    :param axes: an Axes object for which the labels are generated
    :param label_settings: label settings of the required axis
    :return: a mobject containing the label of the axis
    """

    get_label = getattr(axes, f"get_{label_settings.axis}_axis_label")

    return get_label(
        MathTex(label_settings.label, font_size=label_settings.font_size),
        edge=label_settings.edge,
        direction=label_settings.direction,
        buff=label_settings.buff
    ).rotate(label_settings.angle)


def generate_plot(plot_settings: gs.PlotSettings) -> dict:
    """
    Generates the parameters for the plot function by merging the default plot settings and the settings
    provided by the user.
    :param plot_settings: Settings provided by the user
    :return: A dictionary of merged settings
    """
    return {
        "function": plot_settings.function,
        "x_range": plot_settings.x_range
    }


def generate_the_graph(graph_settings: gs.GraphSettings) -> (VGroup, gs.GraphParts):
    """
    Generates a graph based on the provided graph settings
    :param graph_settings: graph settings required to draw a graph.
    :return: Vgroup mobject consisting of different parts of the graph and a dataclass keeping track of these parts
    """
    axes_settings = graph_settings.axes_settings
    x_label_settings = graph_settings.x_label_settings
    y_label_settings = graph_settings.y_label_settings
    plot_settings = graph_settings.plot_settings

    axes = Axes(**axes_settings.as_dict())
    x_label = generate_axis_label(axes, x_label_settings)
    y_label = generate_axis_label(axes, y_label_settings)
    plot = axes.plot(**generate_plot(plot_settings))

    graph = VGroup(axes, x_label, y_label, plot)
    graph_parts = gs.GraphParts(
        axes=axes,
        x_label=x_label,
        y_label=y_label,
        plot=plot
    )

    return graph, graph_parts
