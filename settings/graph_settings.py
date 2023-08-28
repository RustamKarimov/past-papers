from manim import *

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
    "x_label_font_size": ss.MEDIUM_TEX_SIZE,
    "x_label_rotation": 0,
}

Y_LABEL_SETTINGS = {
    "y_label": "y",
    "y_label_edge": UR,
    "y_label_direction": UR,
    "y_label_buff": 0.1,
    "y_label_font_size": ss.MEDIUM_TEX_SIZE,
    "y_label_rotation": 0,
}

PLOT_SETTINGS = {
    "x_range": [0, 1],
    "y_range": [0, 1],
    "function": lambda x: x,
}