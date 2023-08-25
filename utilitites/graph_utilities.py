from manim import *

from settings.graph_settings import GRAPH_SETTINGS


def get_axes_kwargs(kwargs: dict) -> dict:
    """
    Merges the default graph settings dictionary with the provided settings dictionary.
    :param kwargs: the settings dictionary provided in the question
    :return: Merged dictionary
    """
    return GRAPH_SETTINGS | kwargs


def get_axis_label(axes: Axes, axis: str, graph_kwargs: dict) -> Mobject:
    """
    Get label for the specified axis. This is done by merging the default axis settings and
    the settings provided by the user
    :param axes: Axes mobject on which the labels will be added to
    :param axis: X or Y axis.
    :param graph_kwargs: axis settings provided by the useer.
    :return: label Mobject for the given axis.
    """
    label = graph_kwargs.get(f"{axis}_label", GRAPH_SETTINGS[f"{axis}_label"])
    label_edge = graph_kwargs.get(f"{axis}_label_edge", GRAPH_SETTINGS[f"{axis}_label_edge"])
    label_direction = graph_kwargs.get(f"{axis}_label_direction", GRAPH_SETTINGS[f"{axis}_label_direction"])
    label_buff = graph_kwargs.get(f"{axis}_label_buff", GRAPH_SETTINGS[f"{axis}_label_buff"])
    label_font_size = graph_kwargs.get(f"{axis}_label_font_size", GRAPH_SETTINGS[f"{axis}_label_font_size"])

    get_label = getattr(axes, f"get_{axis}_axis_label")

    return get_label(
        MathTex(label, font_size=label_font_size).scale(0.5),
        edge=label_edge,
        direction=label_direction,
        buff=label_buff
    )


def get_plot_kwargs(graph_kwargs: dict) -> dict:
    """
    Generates the parameters for the plot function by merging the default plot settings and the settings
    provided by the user.
    :param graph_kwargs: Settings provided by the user
    :return: A dictionary of merged settings
    """
    return {
        "function": graph_kwargs.get("function", GRAPH_SETTINGS["function"]),
        "x_range": graph_kwargs.get("plot_x_range", GRAPH_SETTINGS["plot_x_range"])
    }


def get_the_graph(graph_kwargs: dict) -> (VGroup, dict):
    """
    Generates a graph based on the provided settings. If no settings are given, the default values will be used
    :param graph_kwargs: Graph settings provided by the user
    :return: Vgroup consisting of x and y labels as well as the axes as the plot of the graph.
            A dictionary to control each of the parts above separately.
    """
    axes = Axes(get_axes_kwargs(graph_kwargs))

    x_label = get_axis_label(axes=axes, axis="x", graph_kwargs=graph_kwargs)
    y_label = get_axis_label(axes=axes, axis="y", graph_kwargs=graph_kwargs)

    plot = axes.plot(**get_plot_kwargs(graph_kwargs))
    graph_dict = {
        "axes": axes,
        "plot": plot,
        "x_label": x_label,
        "y_label": y_label
    }

    return VGroup(y_label, x_label, axes, plot), graph_dict
