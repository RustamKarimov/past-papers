from manim import *

from settings import diagram_settings as ds

from utilitites import diagram_utilities as du


ground = ds.DiagramPart("ground")
point_a = ds.DiagramPart("point_a")
point_b = ds.DiagramPart("point_b")
label_a = ds.DiagramPart("label_a")
label_b = ds.DiagramPart("label_b")
ground_friction = ds.DiagramPart("ground_friction")

section_1 = {
    "parts": [ground, point_a, point_b, label_a, label_b, ground_friction]
}

incline = ds.DiagramPart("incline")
box_a = ds.DiagramPart("box_a")
mass_of_box_a = ds.DiagramPart("mass_of_box_a")
pulley = ds.DiagramPart("pulley")
tension = ds.DiagramPart("tension")
incline_friction = ds.DiagramPart("incline_friction")

section_2 = {
    "parts": [incline, box_a, mass_of_box_a, pulley, tension, incline_friction],
    "individual_actions": {
        "name": "starting_point",
        "target": "incline",
        "function": "get_start",
    },
    "actions": {
        "function": "rotate",
        "function_kwargs": {
            "angle": 40,
            "about_point": "starting_point"
        }
    }
}

diagram_sections = [section_1, section_2]

diagram, diagram_dict = du.generate_diagram(diagram_sections)
