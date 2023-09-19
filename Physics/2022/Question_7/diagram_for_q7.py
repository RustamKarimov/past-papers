from manim import *

from settings import diagram_settings as ds
from settings import stage_settings as ss

from utilitites import diagram_utilities as du


tex_kwargs = {
    "font_size": ss.MEDIUM_TEX_SIZE,
    "color": ss.TEXT_COLOR
}

ground = ds.DiagramPart(
    label="ground",
    function=Line
)

point_a = ds.DiagramPart(
    label="point_a",
    function=Dot,
    position_function="point_from_proportion",
    reference="ground",
    position_kwargs={
        "alpha": 0.1
    }
)

label_a = ds.DiagramPart(
    label="label_a",
    function=Tex,
    position_function="next_to",
    reference="point_a",
    position_kwargs={
        "direction": DL,
        "buff": 0.1
    },
    function_args=["A"],
    function_kwargs=tex_kwargs,
)

point_b = ds.DiagramPart(
    label="point_b",
    function=Dot,
    position_function="point_from_proportion",
    reference="ground",
    position_kwargs={
        "alpha": 0.9
    }
)

label_b = ds.DiagramPart(
    label="label_b",
    function=Tex,
    position_function="next_to",
    reference="point_b",
    position_kwargs={
        "direction": DR,
        "buff": 0.1
    },
    function_args=["B"],
    function_kwargs=tex_kwargs,
)

ground_friction = ds.DiagramPart(
    label="ground_friction",
    function=MathTex,
    position_function="next_to",
    reference="ground",
    position_kwargs={
        "direction": DOWN,
        "buff": 0.1
    },
    function_args=["\\mu =0,2"],
    function_kwargs=tex_kwargs,)

section_1 = ds.Section(
    parts=[ground, point_a, point_b, label_a, label_b, ground_friction]
)

incline = ds.DiagramPart(
    label="incline",
    function=Line,
    scale=1.5,
    position_function="next_to",
    reference="ground",
    position_kwargs={
        "direction": RIGHT,
        "buff": 0
    },

)

section_2 = ds.Section(
    parts=[incline],

)

diagram_sections = [section_1, section_2]

diagram, diagram_dict = du.generate_diagram(diagram_sections)
# point_a = ds.DiagramPart("point_a")
# point_b = ds.DiagramPart("point_b")
# label_a = ds.DiagramPart("label_a")
# label_b = ds.DiagramPart("label_b")
# ground_friction = ds.DiagramPart("ground_friction")
#
# section_1 = {
#     "parts": [ground, point_a, point_b, label_a, label_b, ground_friction]
# }
#
# incline = ds.DiagramPart("incline")
# box_a = ds.DiagramPart("box_a")
# mass_of_box_a = ds.DiagramPart("mass_of_box_a")
# pulley = ds.DiagramPart("pulley")
# tension = ds.DiagramPart("tension")
# incline_friction = ds.DiagramPart("incline_friction")
#
# section_2 = {
#     "parts": [incline, box_a, mass_of_box_a, pulley, tension, incline_friction],
#     "individual_actions": {
#         "name": "starting_point",
#         "target": "incline",
#         "function": "get_start",
#     },
#     "actions": {
#         "function": "rotate",
#         "function_kwargs": {
#             "angle": 40,
#             "about_point": "starting_point"
#         }
#     }
# }

