from manim import *

from settings import stage_settings as ss

GRAPH_SETTINGS = {
    "x_range": [0, 1],
    "x_plot_range": [0, 1],
    "y_plot_range": [0, 1],
    "y_range": [0, 1],
    "x_length": 2,
    "y_length": 2,
    "x_label": "x",
    "x_label_edge": UR,
    "x_label_direction": UR,
    "x_label_buff": 0.1,
    "x_label_font_size": ss.MEDIUM_TEX_SIZE,
    "y_label": "y",
    "y_label_edge": UR,
    "y_label_direction": UR,
    "y_label_buff": 0.1,
    "y_label_font_size": ss.MEDIUM_TEX_SIZE,
    "axis_config": {
        "include_numbers": False,
        "include_ticks": False,
        "tip_width": 0.1,
        "tip_height": 0.1
    },
    "x_axis_config": None,
    "y_axis_config": None,
    "function": lambda x: x,
}
