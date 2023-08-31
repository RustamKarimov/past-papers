from manim import *

from settings.stage_settings import TEXT_COLOR

from physics_packages.data_classes import PartOfDiagram


def get_part_of_a_diagram(features: PartOfDiagram) -> Mobject:
    if features is None:
        return None

    return Rectangle(
        width=features.width,
        height=features.height,
        stroke_width=features.stroke_width,
        stroke_color=features.stroke_color,
        fill_opacity=features.fill_opacity,
        fill_color=features.fill_color,
    ).rotate(features.rotation * DEGREES)


def get_charges(features):
    return 1


def draw_a_diagram(
        features_of_top_part: PartOfDiagram,
        features_of_middle_part: PartOfDiagram,
        features_of_bottom_part: PartOfDiagram,
        features_of_charges: dict = {},
) -> (VGroup, dict):
    """
    Draw a diagram consisting of the following parts:
        1. Top of a diagram (Rectangle)
        2. Middle part of a diagram (Rectangle)
        3. Bottom part of a diagram (Rectangle)
        4. Charges (Spheres which may or may not be connected to one of the parts above)
    :param features_of_top_part: Features of a rectangle for the top part
    :param features_of_middle_part: Features of a rectangle for the middle part
    :param features_of_bottom_part: Features of a rectangle for the bottom part
    :param features_of_charges: A dictionary containing the features of each charge in the diagram
    :return: Vgroup containing final result of each of the parameters above and
            a dictionary to access each part individually
    """
    top = get_part_of_a_diagram(features_of_top_part)
    middle = get_part_of_a_diagram(features_of_middle_part)
    bottom = get_part_of_a_diagram(features_of_bottom_part)
    charges = get_charges(features_of_charges)

    diagram = VGroup()
    diagram_dict = {}

    for part, part_name in zip([top, middle, bottom, charges], ["top", "middle", "bottom", "charges"]):
        if part[0]:
            diagram.add(part[0])
            diagram_dict[part_name] = part[1]

    return diagram, diagram_dict
