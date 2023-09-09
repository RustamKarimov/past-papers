from manim import *

from settings.diagram_settings import DiagramPart
from settings import stage_settings as ss

from utilitites.diagram_utilities import generate_diagram


ceiling = DiagramPart(
    label="ceiling",
    function=Rectangle,
    function_kwargs={
        "height": 0.2,
        "width": 6,
        "stroke_color": ss.TEXT_COLOR,
        "stroke_width": 1,
        "fill_color": ss.TEXT_COLOR,
        "fill_opacity": 0.2
    }
)

string = DiagramPart(
    label="string",
    function=Line,
    position_function="next_to",
    position_kwargs={
        "reference": "ceiling",
        "direction": DOWN,
        "buff": 0
    },
    scale=0.6,
    rotation_angle=90
)

sphere_m = DiagramPart(
    label="sphere_m",
    function=LabeledDot,
    function_kwargs={
        "label": "M",
        "radius": 0.4
    },
    position_function="next_to",
    position_kwargs={
        "reference": "string",
        "direction": DOWN,
        "buff": 0
    }
)

sphere_n = DiagramPart(
    label="sphere_n",
    function=LabeledDot,
    function_kwargs={
        "label": "N",
        "radius": 0.4
    },
    position_function="next_to",
    position_kwargs={
        "reference": "sphere_m",
        "direction": DOWN,
        "buff": 1
    }
)


diagram_parts = [ceiling, string, sphere_m, sphere_n]

diagram, diagram_dict = generate_diagram(diagram_parts)
