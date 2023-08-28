from manim import *

from settings import graph_settings as gs


def get_axes_kwargs(kwargs: dict) -> dict:
    """
    Merges the default graph settings dictionary with the provided settings dictionary.
    :param kwargs: the settings dictionary provided in the question
    :return: Merged dictionary
    """
    return gs.GRAPH_SETTINGS | kwargs


def get_axis_label(axes: Axes, axis: str, label_settings,  label_kwargs: dict) -> Mobject:
    """
    Get label for the specified axis. This is done by merging the default axis settings and
    the settings provided by the user
    :param axes: Axes mobject on which the labels will be added to
    :param axis: X or Y axis.
    :param label_settings: Default settings for the label
    :param label_kwargs: axis settings provided by the useer.
    :return: label Mobject for the given axis.
    """
    label = label_kwargs.get(f"{axis}_label", label_settings[f"{axis}_label"])
    label_edge = label_kwargs.get(f"{axis}_label_edge", label_settings[f"{axis}_label_edge"])
    label_direction = label_kwargs.get(f"{axis}_label_direction", label_settings[f"{axis}_label_direction"])
    label_buff = label_kwargs.get(f"{axis}_label_buff", label_settings[f"{axis}_label_buff"])
    label_font_size = label_kwargs.get(f"{axis}_label_font_size", label_settings[f"{axis}_label_font_size"])
    label_rotation = label_kwargs.get(f"{axis}_label_rotation", label_settings[f"{axis}_label_rotation"])

    get_label = getattr(axes, f"get_{axis}_axis_label")

    return get_label(
        MathTex(label, font_size=label_font_size),
        edge=label_edge,
        direction=label_direction,
        buff=label_buff
    ).rotate(label_rotation)


def get_plot_kwargs(plot_kwargs: dict) -> dict:
    """
    Generates the parameters for the plot function by merging the default plot settings and the settings
    provided by the user.
    :param plot_kwargs: Settings provided by the user
    :return: A dictionary of merged settings
    """
    return {
        "function": plot_kwargs.get("function", gs.PLOT_SETTINGS["function"]),
        "x_range": plot_kwargs.get("x_range", gs.PLOT_SETTINGS["x_range"])
    }


def get_the_graph(kwargs: dict) -> (VGroup, dict):
    """
    Generates a graph based on the provided settings. If no settings are given, the default values will be used
    :param kwargs: Graph settings provided by the user
    :return: Vgroup consisting of x and y labels as well as the axes as the plot of the graph.
            A dictionary to control each of the parts above separately.
    """
    axes_kwargs = get_axes_kwargs(kwargs["graph_kwargs"])
    print(axes_kwargs)
    axes = Axes(**axes_kwargs)

    x_label = get_axis_label(
        axes=axes,
        axis="x",
        label_settings=gs.X_LABEL_SETTINGS,
        label_kwargs=kwargs["x_label_kwargs"]
    )
    y_label = get_axis_label(
        axes=axes,
        axis="y",
        label_settings=gs.Y_LABEL_SETTINGS,
        label_kwargs=kwargs["y_label_kwargs"])

    plot = axes.plot(**get_plot_kwargs(kwargs["plot_kwargs"]))
    graph_dict = {
        "axes": axes,
        "plot": plot,
        "x_label": x_label,
        "y_label": y_label
    }

    return VGroup(y_label, x_label, axes, plot), graph_dict
