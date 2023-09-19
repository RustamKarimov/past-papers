from manim import *


def draw_a_part(diagram_part):
    function = diagram_part.function
    function_args = diagram_part.function_args
    function_kwargs = diagram_part.function_kwargs
    return function(*function_args, **function_kwargs)


def position_the_part(part, diagram_part, diagram_dict):
    function = diagram_part.position_function
    if function is None:
        return

    function_kwargs = diagram_part.position_kwargs
    reference_label = diagram_part.reference
    reference_mobject = diagram_dict[reference_label]

    if function == "point_from_proportion":
        if reference_mobject is None:
            raise ValueError("Can't take proportion from an unspecified target mobject")
        point = getattr(reference_mobject, function)(**function_kwargs)
        part.move_to(point)

    else:
        getattr(part, function)(reference_mobject, **function_kwargs)


def rotate_the_part(part, diagram_part):
    rotation_angle = diagram_part.rotation_angle
    if rotation_angle:
        rotation_kwargs = diagram_part.rotation_kwargs
        part.rotate(rotation_angle * DEGREES, **rotation_kwargs)


def scale_the_part(part, diagram_part):
    scale = diagram_part.scale
    part.scale(scale)


def generate_part_of_the_diagram(diagram_part, diagram_dict):
    part = draw_a_part(diagram_part)
    scale_the_part(part, diagram_part)
    rotate_the_part(part, diagram_part)
    position_the_part(part, diagram_part, diagram_dict)

    return part


def apply_individual_actions(section, diagram_dict):
    pass


def apply_actions(section, diagram_dict):
    pass


def generate_diagram(sections):
    diagram = VGroup()
    diagram_dict = {}

    for section in sections:
        for part in section.parts:
            diagram_part = generate_part_of_the_diagram(part, diagram_dict)
            diagram_dict[part.label] = diagram_part
            diagram.add(diagram_part)

        apply_individual_actions(section, diagram_dict)
        apply_actions(section, diagram_dict)

    return diagram, diagram_dict
